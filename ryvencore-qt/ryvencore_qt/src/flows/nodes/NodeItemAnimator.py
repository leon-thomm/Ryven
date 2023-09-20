from qtpy.QtCore import QObject, QPropertyAnimation, Property
from qtpy.QtGui import QColor
from qtpy.QtWidgets import QGraphicsItem


class NodeItemAnimator(QObject):

    def __init__(self, node_item):
        super(NodeItemAnimator, self).__init__()

        self.node_item = node_item
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

        # self.node_item.title_label.update_design()
        self.title_activation_animation.setKeyValueAt(0, self.get_title_color())
        self.title_activation_animation.setKeyValueAt(0.3, self.get_body_color().lighter().lighter())
        self.title_activation_animation.setKeyValueAt(1, self.get_title_color())

        self.body_activation_animation.setKeyValueAt(0, self.get_body_color())
        self.body_activation_animation.setKeyValueAt(0.3, self.get_body_color().lighter())
        self.body_activation_animation.setKeyValueAt(1, self.get_body_color())

    def fading_out(self):
        return self.title_activation_animation.currentTime()/self.title_activation_animation.duration() >= 0.3

    def set_animation_max(self):
        self.title_activation_animation.setCurrentTime(0.3*self.title_activation_animation.duration())
        self.body_activation_animation.setCurrentTime(0.3*self.body_activation_animation.duration())

    def get_body_color(self):
        return self.node_item.color

    def set_body_color(self, val):
        self.node_item.color = val
        QGraphicsItem.update(self.node_item)

    p_body_color = Property(QColor, get_body_color, set_body_color)


    def get_title_color(self):
        return self.node_item.widget.title_label.color

    def set_title_color(self, val):
        self.node_item.widget.title_label.color = val
        # QGraphicsItem.update(self.node_item)

    p_title_color = Property(QColor, get_title_color, set_title_color)