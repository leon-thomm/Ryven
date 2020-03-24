from PySide2.QtWidgets import QLabel, QVBoxLayout
from PySide2.QtCore import QSize, QTimer
from PySide2.QtGui import QPixmap, QImage

from PySide2.QtWidgets import QWidget

import cv2


class %NODE_TITLE%_NodeInstance_MainWidget(QWidget):
    def __init__(self, parent_node_instance):
        super(%NODE_TITLE%_NodeInstance_MainWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------

        self.video_size = QSize(400, 300)
        self.timer = QTimer()

        self.image_label = QLabel()
        self.image_label.setFixedSize(self.video_size)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.image_label)
        self.setLayout(self.main_layout)

        self.setup_camera()

        self.resize(self.video_size)

    def setup_camera(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())

        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)

    def display_video_stream(self):
        print('displaying video strem')
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)
        scaled_image = image.scaled(self.video_size)
        self.image_label.setPixmap(QPixmap.fromImage(scaled_image))

        self.parent_node_instance.video_picture_updated(frame)

    def deleted(self):
        self.timer.stop()
        print('timer stopped!')

    def get_data(self):
        return {}  # self.text()

    def set_data(self, data):
        pass #self.setText(data)
