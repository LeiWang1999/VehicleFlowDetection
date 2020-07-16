# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/wanglei/Documents/Study/PyQt/01_Vehicle_Flow_Detection/GUI/VechicleGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 766)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.choose_video = QtWidgets.QFrame(self.centralwidget)
        self.choose_video.setGeometry(QtCore.QRect(10, 10, 771, 51))
        self.choose_video.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.choose_video.setFrameShadow(QtWidgets.QFrame.Raised)
        self.choose_video.setObjectName("choose_video")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.choose_video)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.choose_video)
        self.label_2.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:18px；")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.choose_video)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.browse = QtWidgets.QPushButton(self.choose_video)
        self.browse.setObjectName("browse")
        self.horizontalLayout.addWidget(self.browse)
        self.baseline_info = QtWidgets.QFrame(self.centralwidget)
        self.baseline_info.setGeometry(QtCore.QRect(780, 0, 501, 391))
        self.baseline_info.setStyleSheet("")
        self.baseline_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.baseline_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.baseline_info.setObjectName("baseline_info")
        self.baseline_table = QtWidgets.QTableWidget(self.baseline_info)
        self.baseline_table.setGeometry(QtCore.QRect(0, 0, 501, 351))
        self.baseline_table.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.baseline_table.setGridStyle(QtCore.Qt.NoPen)
        self.baseline_table.setRowCount(10)
        self.baseline_table.setColumnCount(4)
        self.baseline_table.setObjectName("baseline_table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.baseline_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.baseline_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.baseline_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.baseline_table.setHorizontalHeaderItem(3, item)
        self.baseline_table.horizontalHeader().setVisible(True)
        self.baseline_table.horizontalHeader().setCascadingSectionResizes(False)
        self.baseline_table.horizontalHeader().setDefaultSectionSize(110)
        self.baseline_table.horizontalHeader().setHighlightSections(True)
        self.baseline_table.horizontalHeader().setMinimumSectionSize(30)
        self.baseline_table.horizontalHeader().setSortIndicatorShown(False)
        self.baseline_table.horizontalHeader().setStretchLastSection(True)
        self.baseline_table.verticalHeader().setVisible(False)
        self.baseline_table.verticalHeader().setCascadingSectionResizes(False)
        self.baseline_table.verticalHeader().setHighlightSections(False)
        self.baseline_table.verticalHeader().setSortIndicatorShown(False)
        self.baseline_table.verticalHeader().setStretchLastSection(False)
        self.layoutWidget = QtWidgets.QWidget(self.baseline_info)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 350, 501, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.baseline_message = QtWidgets.QLabel(self.layoutWidget)
        self.baseline_message.setStyleSheet("color:red;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:18px；")
        self.baseline_message.setObjectName("baseline_message")
        self.horizontalLayout_2.addWidget(self.baseline_message)
        self.line_clear = QtWidgets.QPushButton(self.layoutWidget)
        self.line_clear.setObjectName("line_clear")
        self.horizontalLayout_2.addWidget(self.line_clear)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-1, -5, 1281, 751))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./images/background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.draw_baseline = QtWidgets.QFrame(self.centralwidget)
        self.draw_baseline.setGeometry(QtCore.QRect(10, 80, 771, 511))
        self.draw_baseline.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.draw_baseline.setFrameShadow(QtWidgets.QFrame.Raised)
        self.draw_baseline.setObjectName("draw_baseline")
        self.graphicsView = QtWidgets.QGraphicsView(self.draw_baseline)
        self.graphicsView.setGeometry(QtCore.QRect(0, 50, 771, 461))
        self.graphicsView.setObjectName("graphicsView")
        self.label_3 = QtWidgets.QLabel(self.draw_baseline)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 611, 51))
        self.label_3.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:18px；")
        self.label_3.setObjectName("label_3")
        self.realtimemode = QtWidgets.QRadioButton(self.draw_baseline)
        self.realtimemode.setGeometry(QtCore.QRect(630, 10, 131, 31))
        self.realtimemode.setObjectName("realtimemode")
        self.control_process = QtWidgets.QFrame(self.centralwidget)
        self.control_process.setGeometry(QtCore.QRect(10, 600, 771, 101))
        self.control_process.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.control_process.setFrameShadow(QtWidgets.QFrame.Raised)
        self.control_process.setObjectName("control_process")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.control_process)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.start = QtWidgets.QPushButton(self.control_process)
        self.start.setObjectName("start")
        self.gridLayout_2.addWidget(self.start, 1, 0, 1, 1)
        self.pause = QtWidgets.QPushButton(self.control_process)
        self.pause.setObjectName("pause")
        self.gridLayout_2.addWidget(self.pause, 1, 2, 1, 1)
        self.processrate = QtWidgets.QLabel(self.control_process)
        self.processrate.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:18px；")
        self.processrate.setObjectName("processrate")
        self.gridLayout_2.addWidget(self.processrate, 0, 0, 1, 3)
        self.process_message = QtWidgets.QLabel(self.control_process)
        self.process_message.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:18px；")
        self.process_message.setObjectName("process_message")
        self.gridLayout_2.addWidget(self.process_message, 1, 1, 1, 1)
        self.show_result = QtWidgets.QFrame(self.centralwidget)
        self.show_result.setGeometry(QtCore.QRect(780, 480, 501, 221))
        self.show_result.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.show_result.setFrameShadow(QtWidgets.QFrame.Raised)
        self.show_result.setObjectName("show_result")
        self.label_19 = QtWidgets.QLabel(self.show_result)
        self.label_19.setGeometry(QtCore.QRect(10, 0, 96, 39))
        self.label_19.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:18px；")
        self.label_19.setObjectName("label_19")
        self.label_6 = QtWidgets.QLabel(self.show_result)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 481, 151))
        self.label_6.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:18px；")
        self.label_6.setScaledContents(False)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(780, 390, 501, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.bicycle = QtWidgets.QCheckBox(self.frame)
        self.bicycle.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:18px；")
        self.bicycle.setChecked(False)
        self.bicycle.setObjectName("bicycle")
        self.gridLayout.addWidget(self.bicycle, 0, 3, 1, 1)
        self.car = QtWidgets.QCheckBox(self.frame)
        self.car.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:18px；")
        self.car.setChecked(True)
        self.car.setObjectName("car")
        self.gridLayout.addWidget(self.car, 0, 4, 1, 1)
        self.van = QtWidgets.QCheckBox(self.frame)
        self.van.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:18px；")
        self.van.setChecked(True)
        self.van.setObjectName("van")
        self.gridLayout.addWidget(self.van, 0, 5, 1, 1)
        self.motor = QtWidgets.QCheckBox(self.frame)
        self.motor.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:18px；")
        self.motor.setObjectName("motor")
        self.gridLayout.addWidget(self.motor, 1, 5, 1, 1)
        self.pedestrian = QtWidgets.QCheckBox(self.frame)
        self.pedestrian.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:18px；")
        self.pedestrian.setObjectName("pedestrian")
        self.gridLayout.addWidget(self.pedestrian, 0, 1, 1, 1)
        self.bus = QtWidgets.QCheckBox(self.frame)
        self.bus.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:18px；")
        self.bus.setChecked(True)
        self.bus.setObjectName("bus")
        self.gridLayout.addWidget(self.bus, 1, 4, 1, 1)
        self.people = QtWidgets.QCheckBox(self.frame)
        self.people.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:18px；")
        self.people.setObjectName("people")
        self.gridLayout.addWidget(self.people, 0, 2, 1, 1)
        self.awning_tricycle = QtWidgets.QCheckBox(self.frame)
        self.awning_tricycle.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:18px；")
        self.awning_tricycle.setObjectName("awning_tricycle")
        self.gridLayout.addWidget(self.awning_tricycle, 1, 3, 1, 1)
        self.tricycle = QtWidgets.QCheckBox(self.frame)
        self.tricycle.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:18px；")
        self.tricycle.setObjectName("tricycle")
        self.gridLayout.addWidget(self.tricycle, 1, 2, 1, 1)
        self.truck = QtWidgets.QCheckBox(self.frame)
        self.truck.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:18px；")
        self.truck.setChecked(True)
        self.truck.setObjectName("truck")
        self.gridLayout.addWidget(self.truck, 1, 1, 1, 1)
        self.label.raise_()
        self.choose_video.raise_()
        self.baseline_info.raise_()
        self.draw_baseline.raise_()
        self.control_process.raise_()
        self.show_result.raise_()
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VehicleGUI"))
        self.label_2.setText(_translate("MainWindow", "Choose Media Path"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        item = self.baseline_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "index"))
        item = self.baseline_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Start"))
        item = self.baseline_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "End"))
        item = self.baseline_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Count"))
        self.baseline_message.setText(_translate("MainWindow", "Click Image and add baseline"))
        self.line_clear.setText(_translate("MainWindow", "clear line"))
        self.label_3.setText(_translate("MainWindow", "Draw Baseline  - Drag the scroll bar to view the full picture while the size of target is too large"))
        self.realtimemode.setText(_translate("MainWindow", "Real Time Mode"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.pause.setText(_translate("MainWindow", "Pause"))
        self.processrate.setText(_translate("MainWindow", "Process Rate：0%"))
        self.process_message.setText(_translate("MainWindow", "Status Bar"))
        self.label_19.setText(_translate("MainWindow", "Summary"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>There are two steps to counting vehicle. one is detection operation, the other is counting. Corresponding to the two media output (output.avi, counting.avi) under the ouput folder. And u can speed up the processing speed dozens of times If u have GPU.</p><p>The GitHub page is : <a href=\"https://github.com/NjtechPrinceling/VehicleFlowDetection\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/LeiWang1999/VehicleFlowDetection</span></a></p></body></html>"))
        self.bicycle.setText(_translate("MainWindow", "bicycle"))
        self.car.setText(_translate("MainWindow", "car"))
        self.van.setText(_translate("MainWindow", "van"))
        self.motor.setText(_translate("MainWindow", "motor"))
        self.pedestrian.setText(_translate("MainWindow", "pedestrian"))
        self.bus.setText(_translate("MainWindow", "bus"))
        self.people.setText(_translate("MainWindow", "people"))
        self.awning_tricycle.setText(_translate("MainWindow", "awning-tricycle"))
        self.tricycle.setText(_translate("MainWindow", "tricycle"))
        self.truck.setText(_translate("MainWindow", "truck"))

