from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2
from PyQt5.QtWidgets import *
from yolo_classes import get_cls_dict
from yolov3 import TrtYOLOv3
from camera import add_camera_args, Camera
from visualization import open_window, show_fps, record_time, show_runtime
from engine import BBoxVisualization
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.timer_camera = QtCore.QTimer()  # 定义定时器，用于控制显示视频的帧率
        self.cap = cv2.VideoCapture()  # 视频流
        self.CAM_NUM = 0  # 为0时表示视频流来自笔记本内置摄像头
        self.yolo_dim =416
        self.trt_yolov3 = yolov3.TrtYOLOv3('yolov3-tiny-my-416', (self.yolo_dim, self.yolo_dim))

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 618)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.picnow = QtWidgets.QLabel(self.centralwidget)
        self.picnow.setGeometry(QtCore.QRect(40, 30, 461, 431))
        self.picnow.setObjectName("picnow")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(540, 20, 161, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_can = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_can.setStyleSheet("rgb(170, 255, 0)")
        self.label_can.setObjectName("label_can")
        self.horizontalLayout.addWidget(self.label_can)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_can_num = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_can_num.setStyleSheet("rgb(170, 255, 0)")
        self.label_can_num.setObjectName("label_can_num")
        self.horizontalLayout.addWidget(self.label_can_num)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_cook = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_cook.setStyleSheet("rgb(170, 255, 0)")
        self.label_cook.setObjectName("label_cook")
        self.horizontalLayout_2.addWidget(self.label_cook)
        self.label_cook_num = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_cook_num.setStyleSheet("rgb(170, 255, 0)")
        self.label_cook_num.setObjectName("label_cook_num")
        self.horizontalLayout_2.addWidget(self.label_cook_num)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_bad = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_bad.setStyleSheet("rgb(170, 255, 0)")
        self.label_bad.setObjectName("label_bad")
        self.horizontalLayout_3.addWidget(self.label_bad)
        self.label_bad_num = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_bad_num.setStyleSheet("rgb(170, 255, 0)")
        self.label_bad_num.setObjectName("label_bad_num")
        self.horizontalLayout_3.addWidget(self.label_bad_num)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_other = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_other.setStyleSheet("rgb(170, 255, 0)")
        self.label_other.setObjectName("label_other")
        self.horizontalLayout_4.addWidget(self.label_other)
        self.label_other_num = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_other_num.setStyleSheet("rgb(170, 255, 0)")
        self.label_other_num.setObjectName("label_other_num")
        self.horizontalLayout_4.addWidget(self.label_other_num)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(540, 490, 195, 71))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_begin = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.btn_begin.setObjectName("btn_begin")
        self.horizontalLayout_5.addWidget(self.btn_begin)
        self.btn_end = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.btn_end.setAutoRepeatDelay(300)
        self.btn_end.setObjectName("btn_end")
        self.horizontalLayout_5.addWidget(self.btn_end)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 510, 481, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_index = QtWidgets.QLabel(self.horizontalLayoutWidget)

        self.label_index.setObjectName("label_index")
        self.horizontalLayout_6.addWidget(self.label_index)
        self.index = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setSpacing(0)
        self.index.setObjectName("index")
        self.horizontalLayout_6.addWidget(self.index)
        self.label_type = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_type.setObjectName("label_type")
        self.horizontalLayout_6.addWidget(self.label_type)
        self.label_trash = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_trash.setText("")
        self.label_trash.setObjectName("label_trash")
        self.horizontalLayout_6.addWidget(self.label_trash)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(720, 70, 72, 15))
        self.label.setText("")
        self.label.setObjectName("label")

        self.can_if = QtWidgets.QLabel(self.centralwidget)
        self.can_if.setGeometry(QtCore.QRect(740, 50, 72, 38))
        self.can_if.setObjectName("can_if")
        self.cook_if = QtWidgets.QLabel(self.centralwidget)
        self.cook_if.setGeometry(QtCore.QRect(740, 160, 72, 38))
        self.cook_if.setObjectName("cook_if")
        self.bad_if = QtWidgets.QLabel(self.centralwidget)
        self.bad_if.setGeometry(QtCore.QRect(740, 280, 72, 38))
        self.bad_if.setObjectName("bad_if")
        self.other_if = QtWidgets.QLabel(self.centralwidget)
        self.other_if.setGeometry(QtCore.QRect(740, 400, 72, 38))
        self.other_if.setObjectName("other_if")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def slot_init(self):
        self.timer_camera.timeout.connect(self.show_camera)
        self.btn_end.clicked.connect(self.close)
        self.btn_begin.clicked.connect(self.btn_begin_clicked)

    def btn_begin_clicked(self):
        if self.timer_camera.isActive() == False:  # 若定时器未启动
            flag = self.cap.open(-1)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            if flag == False:  # flag表示open()成不成功
                msg = QtWidgets.QMessageBox.warning(self, 'warning', "请检查相机于电脑是否连接正确", buttons=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(30)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
        else:
            self.timer_camera.stop()  # 关闭定时器
            self.cap.release()  # 释放视频流
            self.label_show_camera.clear()  # 清空视频显示区域

    def show_camera(self):
        flag, self.image = self.cap.read()  # 从视频流中读取
        img1 = self.image
        timer = cv2.getTickCount()
        cls_dict = get_cls_dict('coco')
        
        print('[INFO]  Camera: starting')
        vis = BBoxVisualization(cls_dict)
        if (img1 is not None):
            boxes, confs, clss, _preprocess_time, _postprocess_time,_network_time = self.trt_yolov3.detect(img1, 0.3)
            img, _visualize_time = vis.draw_bboxes(self.image, boxes, confs, clss)
            time_stamp = record_time(_preprocess_time, _postprocess_time, _network_time, _visualize_time)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
            img1 = show_fps(img1, fps)

        # loop_and_detect(cam, args.runtime, trt_yolov3, conf_th=0.3, vis=vis,ff = ff)

        show = cv2.resize(img1, (640, 480))  # 把读到的帧的大小重新设置为 640x480
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        self.picnow.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.picnow.setText(_translate("MainWindow", "TextLabel"))

        self.label_can.setText(_translate("MainWindow", "可回收垃圾"))
        self.label_can_num.setText(_translate("MainWindow", "0"))
        self.label_can.setStyleSheet("background-color: #ADFF2F;font:25px;")
        self.label_can_num.setStyleSheet("background-color: #ADFF2F;font:25px;")

        self.label_cook.setText(_translate("MainWindow", "厨余收垃圾"))
        self.label_cook_num.setText(_translate("MainWindow", "0"))
        self.label_cook.setStyleSheet("background-color: #ffff66;font:25px;")
        self.label_cook_num.setStyleSheet("background-color: #ffff66;font:25px;")

        self.label_index.setText(_translate("MainWindow", "序号 :"))
        self.label_index.setStyleSheet("background-color: #FFDAB9;font:25px;")
        self.index.setText(_translate("MainWindow", "2"))
        self.index.setStyleSheet("background-color: #FFDAB9;font:25px;")
        self.label_type.setText(_translate("MainWindow", "垃圾种类:"))
        self.label_type.setStyleSheet("background-color: #EEEED1;font:25px;")
        self.label_trash.setStyleSheet("background-color:#EEEED1;font:25px;")
        self.label_trash.setText(_translate("MainWindow", "有害垃圾"))


        self.can_if.setText(_translate("MainWindow", " ✅"))
        self.cook_if.setText(_translate("MainWindow", " ✅"))
        self.bad_if.setText(_translate("MainWindow", " ✅"))
        self.other_if.setText(_translate("MainWindow", " ✅"))
        self.can_if.setStyleSheet("font:25px;")
        self.cook_if.setStyleSheet("font:25px;")
        self.bad_if.setStyleSheet("font:25px;")
        self.other_if.setStyleSheet("font:25px;")



        self.label_bad.setText(_translate("MainWindow", "有害垃圾  "))
        self.label_bad_num.setText(_translate("MainWindow", "1"))
        self.label_bad.setStyleSheet("background-color: #ff0033;color: white;font:25px;")
        self.label_bad_num.setStyleSheet("background-color: #ff0033;color: white;font:25px;")


        self.label_other.setText(_translate("MainWindow", "其他收垃圾"))
        self.label_other_num.setText(_translate("MainWindow", "1"))
        self.label_other.setStyleSheet("background-color: #99ffff;font:25px;")
        self.label_other_num.setStyleSheet("background-color: #99ffff;font:25px;")

        self.btn_begin.setText(_translate("MainWindow", "开始"))
        self.btn_end.setText(_translate("MainWindow", "结束"))

class MyWindow(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.slot_init()
def showpic():
    app = QtWidgets.QApplication(sys.argv)  # 固定的，表示程序应用
    ui = MyWindow()  # 实例化Ui_MainWindow
    ui.show()  # 调用ui的show()以显示。同样show()是源于父类QtWidgets.QWidget的
    sys.exit(app.exec_())
