## <h1 align="center">VehicleFlowDetection</h1>

In this project, we use Yolo3 algorithm to count the traffic flow in media. Currently, this algorithm can achieve a speed of 30fps  with 2070 super. The algorithm of [tensorflow-serving-yolov3](https://github.com/Byronnar/tensorflow-serving-yolov3) and the tensorflow version of yolo algorithm is used is used because the training process of the original yolo algorithm requires high GPU computing power. In addition, this project uses Pyqt5 to design the interactive interface, which can be used to select videos and draw counting lines in a friendly manner.

There are still many deficiencies in the project, please feel free to PR !

**What did we mainly modify in the original `tensorflow-serving-yolov3`?**

- `./core/config.py`

  ~~~
  __C.YOLO.CLASSES => class_names
  __C.TRAIN.ANNOT_PATH => train_labels
  __C.TEST.ANNOT_PATH => test_labels
  __C.TRAIN.BATCH_SIZE => batch_size 
  ~~~

- Add VisDrone Dataset which is located in  `./VisDrone2018-tf-yolo/`, to Match the shooting angle of the drone

  Pretrain model should be put in  `./model/yolov3_visdrone.pb`
  
- Transplanted the [iou-tracker](https://github.com/bochinski/iou-tracker) algorithm to achieve multi-target tracking, correlating objects in multiple frames to realize the detection of vehicle trajectories, when detecting Count when the vehicle trajectory crosses the detection line.

The accuracy of detecting the VisDrone data set is relatively high right now

![mAP](http://leiblog.wang/static/image/2020/6/mAP.png)

#### PyQT5 interactive interface

![GUI](http://leiblog.wang/static/image/2020/6/1.jpg)

#### Detection：

![detecting](http://leiblog.wang/static/image/2020/6/detect.png)

#### Count：

![counting](http://leiblog.wang/static/image/2020/6/count.png)

### Resouces

Pretrained Yolov3 Model：[yolov3_visdrone.pb](http://leiblog.wang/static/2020-06-13/yolov3_visdrone.zip) 

Training Dataset：[VisDrone2018-tf-yolo.zip](http://leiblog.wang/static/2020-06-13/VisDrone2018-tf-yolo.zip)

Validation Media：[valid.mp4](http://leiblog.wang/static/2020-06-13/valid.mp4)

### File Tree of WorkSpace

~~~
.
├── GUI
│   ├── Ui_Main.py
│   ├── Ui_VechicleGUI.py
│   ├── VechicleGUI.ui
│   └── __pycache__
│       ├── Ui_Main.cpython-37.pyc
│       └── Ui_VechicleGUI.cpython-37.pyc
├── README.md
├── VisDrone2018-tf-yolo 
│   ├── scripts
│   │   ├── visdrone2tfyolo.py
│   │   └── visdrone2tfyolo.sh
│   ├── test.txt
│   ├── train.txt
│   └── visdrone.names
├── __pycache__
│   └── Ui_demo.cpython-37.pyc
├── debug.txt
├── detection.txt
├── images
│   └── background.jpg
├── lib
│   ├── core
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-37.pyc
│   │   │   ├── config.cpython-37.pyc
│   │   │   └── utils.cpython-37.pyc
│   │   ├── backbone.py
│   │   ├── backbone_mobilenetv2.py
│   │   ├── common.py
│   │   ├── common_mobilenetv2.py
│   │   ├── config.py
│   │   ├── config_Chinese.py
│   │   ├── dataset.py
│   │   ├── utils.py
│   │   ├── utils_Chinese.py
│   │   ├── yolov3.py
│   │   └── yolov3_mobilenetv2.py
│   └── tools
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-37.pyc
│       │   ├── image_process.cpython-37.pyc
│       │   ├── iou_tracker.cpython-37.pyc
│       │   ├── save_image.cpython-37.pyc
│       │   ├── speed_prediction.cpython-37.pyc
│       │   ├── trackers_to_perframe.cpython-37.pyc
│       │   ├── vehicle_counting.cpython-37.pyc
│       │   └── vis_tracker.cpython-37.pyc
│       ├── image_process.py
│       ├── iou_tracker.py
│       ├── save_image.py
│       ├── speed_prediction.py
│       ├── trackers_to_perframe.py
│       ├── vehicle_counting.py
│       └── vis_tracker.py
├── main.py
├── models
│   └── yolov3_visdrone.pb
├── output
│   ├── counting.avi
│   ├── output.avi
│   └── tmp.pk
└── videos
    ├── 1.mp4
    └── 2.mp4
~~~

### Explanations

The environment we are running is `python >= 3.5` and `tensorflow >= 1.15.0`, run the following command on the command line to install related dependencies

```bash
pip install -r requirement.txt
```

When the Start button is clicked, two programs will be executed:

1. The first thing to do is the detect operation, this program contains two processes：

   1. Firstly , try the trained model `./yolov3_visdrone.pb` to detect the video selection and mark the position of the vehicle in each frame of the image. This process will also output the inspection results to `./output/output.mp4`;
   2. Then use [iou-tracker](https://github.com/bochinski/iou-tracker) algorithm for multi-target tracking, that is, on the results of the original detection, the **traveling track of each car** is marked, this The result of the process is saved in `./output/tmp.pk`;

   Tips: You can click **Real Time Mode** Checkbox to display the detection results in real time. If it is performed on the GPU, the display may cause insufficient video memory and the program crashes. If it is not running on the GPU, the running speed is touching, but it is turned on by default. You can view `./output/output.mp4` after the program is completed.

2. Then perform the counting operation to count the traffic flow, that is, use the vehicle trajectory data previously detected, and count when the vehicle trajectory passes the line drawn at the intersection。

   - Same as the detect operation, **Real Time Mode** can choose whether to watch the real-time results, or you can view `./output/counting.mp4` after the program is completed.
   
   - The intersection line position is modified in the `baseline` GUI interface, their default values are as follows
   
     ~~~python
     # 左边路口划线位置
     LEFT_INTERSECTION_ROI_POSITION = 400
     LEFT_INTERSECTION_ROI_START = 300
     LEFT_INTERSECTION_ROI_END = 550
     # 右边路口划线位置
     RIGHT_INTERSECTION_ROI_POSITION = 1000
     RIGHT_INTERSECTION_ROI_START = 0
     RIGHT_INTERSECTION_ROI_END = 280
     # 底部路口划线位置
     BOTTOM_INTERSECTION_ROI_POSITION = 500
     BOTTOM_INTERSECTION_ROI_START = 500
     BOTTOM_INTERSECTION_ROI_END = 900
     ~~~

Watch Operation screen recording: http://leiblog.wang/technicaldetail/5ee4e9f35e36ca32d43f9ceb

Read CH Readme.md: https://github.com/NjtechPrinceling/VehicleFlowDetection/blob/master/README_CN.md

# Reference

[Drone_Vehicle_Flow_Detection](https://gitee.com/starrynightzyq/Drone_Vehicle_Flow_Detection)

[PyQt5](https://pypi.org/project/PyQt5/)

[tensorflow-yolov3](https://github.com/YunYang1994/tensorflow-yolov3)

[tensorflow-serving-yolov3](https://github.com/Byronnar/tensorflow-serving-yolov3)

[iou-tracker](https://github.com/bochinski/iou-tracker)