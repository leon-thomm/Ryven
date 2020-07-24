from PySide2.QtCore import QObject, QPropertyAnimation, Property
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QGraphicsItem


class NodeInstanceAnimator(QObject):
    def __init__(self, node_instance):
        super(NodeInstanceAnimator, self).__init__()

        self.node_instance = node_instance
        self.animation_running = False

        self.title_activation_animation = QPropertyAnimation(self, b"p_title_color")
        self.title_activation_animation.setDuration(700)
        self.title_activation_animation.finished.connect(self.finished)
        self.body_activation_animation = QPropertyAnimation(self, b"p_body_color")
        self.body_activation_animation.setDuration(700)

    def start(self):
        self.animation_running = True
        self.title_activation_animation.start()
        self.body_activation_animation.start()

    def stop(self):
        # reset color values. it would just freeze without
        self.title_activation_animation.setCurrentTime(self.title_activation_animation.duration())
        self.body_activation_animation.setCurrentTime(self.body_activation_animation.duration())

        self.title_activation_animation.stop()
        self.body_activation_animation.stop()

    def finished(self):
        self.animation_running = False

    def running(self):
        return self.animation_running

    def reload_values(self):
        self.stop()

        # self.node_instance.title_label.update_design()
        self.title_activation_animation.setKeyValueAt(0, self.get_title_color())
        self.title_activation_animation.setKeyValueAt(0.3, self.get_body_color().lighter().lighter())
        self.title_activation_animation.setKeyValueAt(1, self.get_title_color())

        self.body_activation_animation.setKeyValueAt(0, self.get_body_color())
        self.body_activation_animation.setKeyValueAt(0.3, self.get_body_color().lighter())
        self.body_activation_animation.setKeyValueAt(1, self.get_body_color())

    def get_body_color(self):
        return self.node_instance.color

    def set_body_color(self, val):
        self.node_instance.color = val
        QGraphicsItem.update(self.node_instance)

    p_body_color = Property(QColor, get_body_color, set_body_color)


    def get_title_color(self):
        return self.node_instance.title_label.color

    def set_title_color(self, val):
        self.node_instance.title_label.color = val
        # QGraphicsItem.update(self.node_instance)

    p_title_color = Property(QColor, get_title_color, set_title_color)