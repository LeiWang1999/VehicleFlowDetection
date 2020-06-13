# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/wanglei/DLHungYiLee/PyQt/01_Vechicle_Flow_Detection/GUI/VechicleGUI.ui'
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
        self.baseline_info.setGeometry(QtCore.QRect(780, 0, 501, 211))
        self.baseline_info.setStyleSheet("")
        self.baseline_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.baseline_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.baseline_info.setObjectName("baseline_info")
        self.gridLayout = QtWidgets.QGridLayout(self.baseline_info)
        self.gridLayout.setObjectName("gridLayout")
        self.left_position = QtWidgets.QTextEdit(self.baseline_info)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        self.left_position.setFont(font)
        self.left_position.setStyleSheet(
            "color:red;\\n\\nfont-family: 微软雅黑;\\n\\nfont-size:18px；")
        self.left_position.setObjectName("left_position")
        self.gridLayout.addWidget(self.left_position, 1, 1, 1, 1)
        self.left_start = QtWidgets.QTextEdit(self.baseline_info)
        self.left_start.setStyleSheet(
            "color:red;\\n\\nfont-family: 微软雅黑;\\n\\nfont-size:18px；")
        self.left_start.setObjectName("left_start")
        self.gridLayout.addWidget(self.left_start, 1, 2, 1, 1)
        self.bottom_end = QtWidgets.QTextEdit(self.baseline_info)
        self.bottom_end.setStyleSheet(
            "color:blue;\\n\\nfont-family: 微软雅黑;\\n\\nfont-size:18px；")
        self.bottom_end.setObjectName("bottom_end")
        self.gridLayout.addWidget(self.bottom_end, 3, 3, 1, 1)
        self.right_position = QtWidgets.QTextEdit(self.baseline_info)
        self.right_position.setStyleSheet(
            "color:green;\\\\n\\\\nfont-family: 微软雅黑;\\\\n\\\\nfont-size:18px；")
        self.right_position.setObjectName("right_position")
        self.gridLayout.addWidget(self.right_position, 2, 1, 1, 1)
        self.left_end = QtWidgets.QTextEdit(self.baseline_info)
        self.left_end.setStyleSheet(
            "color:red;\\\\n\\\\nfont-family: 微软雅黑;\\\\n\\\\nfont-size:18px；")
        self.left_end.setObjectName("left_end")
        self.gridLayout.addWidget(self.left_end, 1, 3, 1, 1)
        self.bottom_start = QtWidgets.QTextEdit(self.baseline_info)
        self.bottom_start.setStyleSheet(
            "color:blue;\\n\\nfont-family: 微软雅黑;\\n\\nfont-size:18px；")
        self.bottom_start.setObjectName("bottom_start")
        self.gridLayout.addWidget(self.bottom_start, 3, 2, 1, 1)
        self.right_end = QtWidgets.QTextEdit(self.baseline_info)
        self.right_end.setStyleSheet(
            "color:green;\\n\\nfont-family: 微软雅黑;\\n\\nfont-size:18px；")
        self.right_end.setObjectName("right_end")
        self.gridLayout.addWidget(self.right_end, 2, 3, 1, 1)
        self.bottom_position = QtWidgets.QTextEdit(self.baseline_info)
        self.bottom_position.setStyleSheet(
            "color:blue;\\n\\nfont-family: 微软雅黑;\\n\\nfont-size:18px；")
        self.bottom_position.setObjectName("bottom_position")
        self.gridLayout.addWidget(self.bottom_position, 3, 1, 1, 1)
        self.right_start = QtWidgets.QTextEdit(self.baseline_info)
        self.right_start.setStyleSheet(
            "color:green;\\n\\nfont-family: 微软雅黑;\\n\\nfont-size:18px；")
        self.right_start.setObjectName("right_start")
        self.gridLayout.addWidget(self.right_start, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.baseline_info)
        self.label_9.setStyleSheet(
            "color:black;\\n\\nfont-family: 微软雅黑;\\n\\nfont-size:18px；")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.baseline_info)
        self.label_8.setStyleSheet(
            "color:black;\\n\\nfont-family: 微软雅黑;\\n\\nfont-size:18px；")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.baseline_info)
        self.label_11.setStyleSheet(
            "color:black;\\n\\nfont-family: 微软雅黑;\\n\\nfont-size:18px；")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.baseline_info)
        self.label_10.setStyleSheet(
            "color:black;\\n\\nfont-family: 微软雅黑;\\n\\nfont-size:18px；")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.baseline_info)
        self.label_20.setStyleSheet("color:white;\n"
                                    "\n"
                                    "font-family: 微软雅黑;\n"
                                    "\n"
                                    "font-size:18px；")
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.baseline_info)
        self.label_4.setStyleSheet(
            "color:black;\\n\\nfont-family: 微软雅黑;\\n\\nfont-size:18px；")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.baseline_info)
        self.label_5.setStyleSheet(
            "color:black;\\n\\nfont-family: 微软雅黑;\\n\\nfont-size:18px；")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.baseline_message = QtWidgets.QLabel(self.baseline_info)
        self.baseline_message.setStyleSheet(
            "color:red;\\n\\nfont-family: 微软雅黑;\\n\\nfont-size:18px；")
        self.baseline_message.setObjectName("baseline_message")
        self.gridLayout.addWidget(self.baseline_message, 4, 0, 1, 3)
        self.generate = QtWidgets.QPushButton(self.baseline_info)
        self.generate.setStyleSheet("Generate")
        self.generate.setObjectName("generate")
        self.gridLayout.addWidget(self.generate, 4, 3, 1, 1)
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
        self.control_process.setGeometry(QtCore.QRect(20, 600, 761, 101))
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
        self.gridLayout_2.addWidget(self.processrate, 0, 0, 1, 2)
        self.show_result = QtWidgets.QFrame(self.centralwidget)
        self.show_result.setGeometry(QtCore.QRect(920, 450, 361, 291))
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
        self.label.raise_()
        self.choose_video.raise_()
        self.baseline_info.raise_()
        self.draw_baseline.raise_()
        self.control_process.raise_()
        self.show_result.raise_()
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
        self.left_position.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Heiti SC\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">400</p></body></html>"))
        self.left_position.setPlaceholderText(
            _translate("MainWindow", "number"))
        self.left_start.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Heiti SC\';\">300</span></p></body></html>"))
        self.left_start.setPlaceholderText(_translate("MainWindow", "number"))
        self.bottom_end.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Heiti SC\';\">900</span></p></body></html>"))
        self.bottom_end.setPlaceholderText(_translate("MainWindow", "number"))
        self.right_position.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Heiti SC\';\">1000</span></p></body></html>"))
        self.right_position.setPlaceholderText(
            _translate("MainWindow", "number"))
        self.left_end.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Heiti SC\';\">550</span></p></body></html>"))
        self.left_end.setPlaceholderText(_translate("MainWindow", "number"))
        self.bottom_start.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Heiti SC\';\">500</span></p></body></html>"))
        self.bottom_start.setPlaceholderText(
            _translate("MainWindow", "number"))
        self.right_end.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Heiti SC\';\">280</span></p></body></html>"))
        self.right_end.setPlaceholderText(_translate("MainWindow", "number"))
        self.bottom_position.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Heiti SC\';\">500</span></p></body></html>"))
        self.bottom_position.setPlaceholderText(
            _translate("MainWindow", "number"))
        self.right_start.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Heiti SC\';\">0</span></p></body></html>"))
        self.right_start.setPlaceholderText(_translate("MainWindow", "number"))
        self.label_9.setText(_translate("MainWindow", "Left"))
        self.label_8.setText(_translate("MainWindow", "End"))
        self.label_11.setText(_translate("MainWindow", "Bottom"))
        self.label_10.setText(_translate("MainWindow", "Right"))
        self.label_20.setText(_translate("MainWindow", "Baseline"))
        self.label_4.setText(_translate("MainWindow", "Position"))
        self.label_5.setText(_translate("MainWindow", "Start"))
        self.baseline_message.setText(_translate(
            "MainWindow", "Click Generate Button to draw baseline !"))
        self.generate.setText(_translate("MainWindow", "Generate"))
        self.label_3.setText(_translate(
            "MainWindow", "Draw Baseline  - Drag the scroll bar to view the full picture while the size of target is too large"))
        self.realtimemode.setText(_translate("MainWindow", "Real Time Mode"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.pause.setText(_translate("MainWindow", "Pause"))
        self.processrate.setText(_translate(
            "MainWindow", "Procfess Percent：0%"))
        self.label_19.setText(_translate("MainWindow", "Show Result"))
