from NIWENV import *
from PySide2.QtWidgets import QLabel, QVBoxLayout
from PySide2.QtCore import QSize, QTimer
from PySide2.QtGui import QPixmap, QImage

from PySide2.QtWidgets import QWidget

import cv2


class %CLASS%(QWidget, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QWidget.__init__(self)

        

        self.video_size = QSize(400, 300)
        self.timer = QTimer()
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

        self.timer.timeout.connect(M(self.display_video_stream))
        self.timer.start(30)

    def display_video_stream(self):
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # frame = cv2.flip(frame, 1)
        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)
        scaled_image = image.scaled(self.video_size)
        self.image_label.setPixmap(QPixmap.fromImage(scaled_image))

        self.parent_node_instance.video_picture_updated(frame)

    def get_data(self):
        return {}  # self.text()

    def set_data(self, data):
        pass #self.setText(data)


    def remove_event(self):
        self.timer.stop()
