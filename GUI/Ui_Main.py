import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QGraphicsPixmapItem, QGraphicsScene
from PyQt5 import QtGui
from PyQt5.QtCore import Qt,QThread
import threading
from .Ui_VechicleGUI import Ui_MainWindow
import cv2
import numpy as np
from PIL import Image
import tensorflow as tf
from pathlib import Path
import sys
from tqdm import tqdm
lib_dir = (Path(__file__).parent / '..' / 'lib').resolve()
if str(lib_dir) not in sys.path:
    sys.path.insert(0, str(lib_dir))

from core import utils
import tools.save_image as save_image
from tools.iou_tracker import save_mod, track_viou_video, save_to_csv

class UiMain(QMainWindow):

    def __init__(self):
        super().__init__()
        ui = Ui_MainWindow()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = ui
        self.media_path = ""
        self.showVideo_flag = False
        self.writeVideo_flag = True
        self.return_elements = ["input/input_data:0", "pred_sbbox/concat_2:0",
                                "pred_mbbox/concat_2:0", "pred_lbbox/concat_2:0"]
        self.pb_file = "./models/yolov3_visdrone.pb"
        self.output_path = './output/output.avi'
        self.annotation_path = './output/test_output/tracker.txt'
        self.pickle_file_path = './output/test_output/tmp.pk'
        self.num_classes = 12
        self.input_size = 416
        self.is_on = True
        ui.setupUi(self)
        ui.browse.clicked.connect(self.browse_file)
        ui.generate.clicked.connect(self.generate_baseline)
        ui.start.clicked.connect(self.start_process)
        ui.pause.setEnabled(False)
        ui.pause.clicked.connect(self.pause_process)
        ui.realtimemode.clicked.connect(self.update_realtimemode)

    def browse_file(self):
        media_path, media_type = QFileDialog.getOpenFileName(
            self, "Open Media")
        if media_path == "":
            return
        self.media_path = media_path
        # Valiate media
        vid = cv2.VideoCapture(media_path)
        self.vid = vid
        if not vid.isOpened():
            self.ui.textBrowser.setPlainText("Couldn't open media!")
        else:
            self.ui.textBrowser.setPlainText(media_path)
            self.ui.textBrowser.moveCursor(
                self.ui.textBrowser.textCursor().End)
        # Save media info
        self.total_frame_counter = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
        self.media_fps = vid.get(cv2.CAP_PROP_FPS)
        self.media_size = (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)),
                           int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        # Sample frame for baseline
        while True:
            return_value, frame = vid.read()
            if return_value == True:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB,)
                self.frame = frame
                break
        self.update_graphic_viewer(frame)
        self.generate_baseline()

    def generate_baseline(self):
        # Validate
        if self.media_path == "":
            self.ui.baseline_message.setText("Please open media first!")
            return
        try:
            self.left_position = int(self.ui.left_position.toPlainText())
            self.left_start = int(self.ui.left_start.toPlainText())
            self.left_end = int(self.ui.left_end.toPlainText())
            self.right_position = int(self.ui.right_position.toPlainText())
            self.right_start = int(self.ui.right_start.toPlainText())
            self.right_end = int(self.ui.right_end.toPlainText())
            self.bottom_position = int(self.ui.bottom_position.toPlainText())
            self.bottom_start = int(self.ui.bottom_start.toPlainText())
            self.bottom_end = int(self.ui.bottom_end.toPlainText())
        except ValueError:
            self.ui.baseline_message.setText(
                "Argument Fault! Please input number!")
        cv2.line(self.frame,
                 (self.left_position, self.left_start),
                 (self.left_position, self.left_end),
                 (0xFF, 0, 0), 5)
        cv2.line(self.frame,
                 (self.right_position, self.right_start),
                 (self.right_position, self.right_end),
                 (0, 0xFF, 0), 5)
        cv2.line(self.frame,
                 (self.bottom_start, self.bottom_position),
                 (self.bottom_end, self.bottom_position),
                 (0,  0, 0xFF), 5)
        self.update_graphic_viewer(self.frame)

    def update_graphic_viewer(self, image):
        showImage = QtGui.QImage(
            image, image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(showImage)
        item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(item)
        self.ui.graphicsView.setScene(self.scene)  # 将场景添加至视图

    '''
        Control mutual Status
    '''

    def mutual_control(self, status: bool):
        self.ui.browse.setEnabled(status)
        self.ui.generate.setEnabled(status)
        self.ui.start.setEnabled(status)
        self.ui.pause.setEnabled(status)
        self.ui.realtimemode.setEnabled(status)

    '''
        开始进行图像处理操作
    '''
    def start_process(self):
        self.mutual_control(False)
        self.ui.pause.setEnabled(True)
        self.compute_thread = WorkThread(window=self)
        self.compute_thread.start()



    def pause_process(self):
        self.is_on = False


    def update_realtimemode(self):
        self.showVideo_flag = self.ui.realtimemode.isChecked()

class WorkThread(QThread):
    
    def __init__(self, window, parent=None):
        super(WorkThread, self).__init__(parent)
        self.window = window
    
    def detect_inference(self):
        graph = tf.Graph()
        return_tensors = utils.read_pb_return_tensors(
            graph, self.window.pb_file, self.window.return_elements)
        # 创建进度条
        pbar = tqdm(total=self.window.total_frame_counter)
        with tf.Session(graph=graph) as sess:
            if self.window.writeVideo_flag:
                isOutput = True if self.window.output_path != "" else False
                if isOutput:
                    video_FourCC = cv2.VideoWriter_fourcc(*'MPEG')
                    out = cv2.VideoWriter(
                        self.window.output_path, video_FourCC, self.window.media_fps, self.window.media_size)
                    list_file = open('detection.txt', 'w')
                    frame_index = -1
            while True:
                while not self.window.is_on:
                    pass
                return_value, frame = self.window.vid.read()
                if return_value != True:
                    break
                if return_value:
                    image = Image.fromarray(frame)
                    self.window.frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                else:
                    raise ValueError("No image!")
                frame_size = frame.shape[:2]
                image_data = utils.image_preporcess(
                    np.copy(frame), [self.window.input_size, self.window.input_size])
                image_data = image_data[np.newaxis, ...]


                pred_sbbox, pred_mbbox, pred_lbbox = sess.run(
                    [return_tensors[1], return_tensors[2], return_tensors[3]],
                    feed_dict={return_tensors[0]: image_data})
                pred_bbox = np.concatenate([np.reshape(pred_sbbox, (-1, 5 + self.window.num_classes)),
                                    np.reshape(pred_mbbox, (-1, 5 + self.window.num_classes)),
                                    np.reshape(pred_lbbox, (-1, 5 + self.window.num_classes))], axis=0)
                bboxes = utils.postprocess_boxes(pred_bbox, frame_size, self.window.input_size, 0.45)
                bboxes = utils.nms(bboxes, 0.45, method='nms')

                # save images
                # save_image.save_image(annotation_file, frame, vid.get(1), bboxes)

                image = utils.draw_bbox(frame, bboxes)
                # image = utils.draw_bbox(frame, bboxes, vid.get(1))
                # 保存为 iou_tracker 格式
                detections = save_mod(bboxes, 0.6)
                result = np.asarray(image)
                if self.window.writeVideo_flag:
                    # save a frame
                    out.write(result)
                if self.window.showVideo_flag:
                    self.window.update_graphic_viewer(result)
                    pbar.update(1)
                    self.window.ui.processrate.setText(str(pbar))
                else:
                    pbar.update(1)
                    self.window.update_graphic_viewer(result)
                    self.window.ui.processrate.setText(str(pbar))
        self.window.mutual_control(True)
        self.window.ui.pause.setEnabled(False)
    
    def run(self):
        self.detect_inference()