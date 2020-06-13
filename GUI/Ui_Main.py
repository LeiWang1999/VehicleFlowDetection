import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QGraphicsPixmapItem, QGraphicsScene
from PyQt5 import QtGui
from .Ui_VechicleGUI import Ui_MainWindow
import cv2
from PIL import Image


class UiMain(QMainWindow):

    def __init__(self):
        super().__init__()
        ui = Ui_MainWindow()
        self.ui = ui
        self.media_path = ""
        ui.setupUi(self)
        ui.browse.clicked.connect(self.browse_file)
        ui.generate.clicked.connect(self.generate_baseline)

    def browse_file(self):
        media_path, media_type = QFileDialog.getOpenFileName(
            self, "Open Media")
        if media_path == "":
            return
        self.media_path = media_path
        # Valiate media
        vid = cv2.VideoCapture(media_path)
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
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB,)
            self.frame = frame
            if return_value == True:
                break
        self.update_graphic_viewer(frame)

    def generate_baseline(self):
        # Validate
        if self.media_path == "":
            self.ui.baseline_message.setText("Please open media first!")
            return
        try:
            print(self.ui.left_position.toPlainText())
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
