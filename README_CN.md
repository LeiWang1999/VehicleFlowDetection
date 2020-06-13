# <div align="center">VehicleFlowDetection</div>

在这个工程中，我们使用Yolo3算法对视频中的车流量进行统计，目前使用 2070super 可以达到 30fps 的速度。使用了 [tensorflow-serving-yolov3](https://github.com/Byronnar/tensorflow-serving-yolov3) 的算法，原版的 yolo 算法训练的过程对 GPU 要求较高，因此使用了 tensorflow 版本的 yolo 算法。另外，本工程使用Pyqt来设计交互界面，能够比较友好的选择视频、绘制计数线。

工程还有很多不足，欢迎递交PR ：）

在原版的 tensorflow-serving-yolov3 上我们主要修改了：

- `./core/config.py`

  ~~~
  __C.YOLO.CLASSES => class_names
  __C.TRAIN.ANNOT_PATH => train_labels
  __C.TEST.ANNOT_PATH => test_labels
  __C.TRAIN.BATCH_SIZE => banch_size 根据显存大小调整
  ~~~

- 增加了 VisDrone 数据集，位置在 `./VisDrone2018-tf-yolo/`

  训练好的模型放在 `./model/yolov3_visdrone.pb`
  
- 移植了 [iou-tracker](https://github.com/bochinski/iou-tracker) 算法，实现了多目标追踪，将多帧画面中的物体进行关联，实现对车辆运动轨迹的检测，当检测到车辆轨迹穿过检测线时进行计数。

目前检测 VisDrone 数据集的正确率已经比较高了

![mAP](http://leiblog.wang/static/image/2020/6/mAP.png)

效果如下：

GUI界面：

![](http://leiblog.wang/static/image/2020/6/QQ20200613-215038-HD.gif)

检测：

![detecting](http://leiblog.wang/static/image/2020/6/detect.gif)

计数：

![counting](http://leiblog.wang/static/image/2020/6/counting.gif)

# Part0. 资源下载

训练好的模型文件：[yolov3_visdrone.pb](http://leiblog.wang/static/2020-06-13/yolov3_visdrone.pb) 

训练用的数据集：[VisDrone2018-tf-yolo.zip](http://leiblog.wang/static/2020-06-13/VisDrone2018-tf-yolo.zip)

测试视频：[valid.mp4](http://leiblog.wang/static/2020-06-13/valid.mp4)

# Part2. 相关的说明

## 1. 目录结构

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

## 2. 程序说明

我们运行的环境是 `python >= 3.5`以及`tensorflow >= 1.15.0`,在命令行运行以下指令安装相关依赖

```bash
pip install -r requirement.txt
```

当点击Start按键时，会执行两段程序：

1. 首先执行的是detect操作，这段程序包含了两个过程：

   1. 先试用训练好模型 `./yolov3_visdrone.pb` 对视频选中进行检测，标出每帧图像中车辆的位置，这个过程同时会将检查的结果输出到 `./output/output.mp4` 中；
   2. 接着使用 [iou-tracker](https://github.com/bochinski/iou-tracker) 算法进行多目标追踪，即在原先检测的结果上，标定出**每辆车的行驶轨迹**，这个过程的结果保存在 `./output/tmp.pk` 中；

   注：可以通过点击**Real Time Mode**这个Checkbox来实时显示检测结果，如果是在 GPU 上进行，显示可能会造成显存不够，程序奔溃。如果不在GPU上运行，则运行速度感人，不过默认还是打开的。可以在程序运行完成后查看 `./output/output.mp4`。

2. 接着执行counting操作，统计车流量，即使用之前检测出的车辆轨迹数据，当有车辆轨迹经过路口画的线时，进行统计。

   - 与detect操作相同，**Real Time Mode**可以选择是否观看实时结果，也可以在程序运行完成后查看 `./output/counting.mp4`。
   
   - 路口划线位置在GUI界面的`baseline`里修改,他们的默认值如下
   
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

# Reference

[Drone_Vehicle_Flow_Detection](https://gitee.com/starrynightzyq/Drone_Vehicle_Flow_Detection)

[PyQt5](https://pypi.org/project/PyQt5/)

[tensorflow-yolov3](https://github.com/YunYang1994/tensorflow-yolov3)

[tensorflow-serving-yolov3](https://github.com/Byronnar/tensorflow-serving-yolov3)

[iou-tracker](https://github.com/bochinski/iou-tracker)