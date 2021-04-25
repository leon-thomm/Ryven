from NWENV import *
from qtpy.QtWidgets import QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget
from qtpy.QtGui import QImage, QPixmap
from qtpy.QtCore import QObject, Signal, QSize, QTimer

import cv2
import os


class OpenCVNode_MainWidget(QLabel, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QLabel.__init__(self)

        self.resize(200, 200)

    def show_image(self, img):
        self.resize(200, 200)
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        img_w = qt_image.width()
        img_h = qt_image.height()
        proportion = img_w / img_h
        self.resize(self.width() * proportion, self.height())
        qt_image = qt_image.scaled(self.width(), self.height())
        self.setPixmap(QPixmap(qt_image))
        self.node.update_shape()


class ChooseFileInputWidget(QPushButton, IWB):

    path_chosen = Signal(str)

    def __init__(self, params):
        IWB.__init__(self, params)
        QPushButton.__init__(self, "Select")

        self.clicked.connect(self.button_clicked)

    def button_clicked(self):
        file_path = QFileDialog.getOpenFileName(self, 'Select image')[0]
        try:
            file_path = os.path.relpath(file_path)
        except ValueError:
            return
        
        self.path_chosen.emit(file_path)


class PathInput(QWidget, IWB):
    path_chosen = Signal(str)

    def __init__(self, params):
        QWidget.__init__(self)
        IWB.__init__(self, params)

        self.path = ''

        # setup UI
        l = QVBoxLayout()
        button = QPushButton('choose')
        button.clicked.connect(self.choose_button_clicked)
        l.addWidget(button)
        self.path_label = QLabel('path')
        l.addWidget(self.path_label)
        self.setLayout(l)
    
    def choose_button_clicked(self):
        f_path = QFileDialog.getSaveFileName(self, 'Save')[0]
        self.path = f_path
        self.path_label.setText(f_path)
        self.node.update_shape()
        self.path_chosen.emit(f_path)

    def get_state(self):
        return {'path': self.path}
    
    def set_state(self, data):
        self.path = data['path']
        self.path_label.setText(self.path)
        self.node.update_shape()


class WebcamFeedWidget(QWidget, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QWidget.__init__(self)

    
        self.video_size = QSize(400, 300)
        self.timer = QTimer(self)
        self.capture = None

        self.image_label = QLabel()
        self.image_label.setFixedSize(self.video_size)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.image_label)
        self.setLayout(self.main_layout)

        self.setup_camera()

        self.resize(self.video_size)

    def setup_camera(self):
        self.capture = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())

        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(20)

    def display_video_stream(self):
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # frame = cv2.flip(frame, 1)
        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)
        scaled_image = image.scaled(self.video_size)
        self.image_label.setPixmap(QPixmap.fromImage(scaled_image))

        self.node.video_picture_updated(frame)
    
    def remove_event(self):
        self.timer.stop()


export_widgets(
    OpenCVNode_MainWidget,
    ChooseFileInputWidget,
    PathInput,
    WebcamFeedWidget,
)
