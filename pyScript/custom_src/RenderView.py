from PySide2.QtWidgets import QGraphicsView, QGraphicsScene
from PySide2.QtGui import QPainter, QPixmap, QImage, QColor
from PySide2.QtCore import QPointF, Qt

import math


class RenderView:       # THIS SECRETELY FAKES A QGRAPHICSVIEW - USING A QGRAPHICSVIEW CAUSES RANDOM CRASHES
    def __init__(self, main_window, node, node_instance_class):
        self.main_window = main_window
        
        # create UI
        scene = RenderScene()
        self.myscene = scene
        scene.setItemIndexMethod(QGraphicsScene.NoIndex)

        new_node_instance = node_instance_class(node, self)
        scene.addItem(new_node_instance)
        new_node_instance.setPos(new_node_instance.width/2, new_node_instance.height/2)
        new_node_instance.add_content_to_scene_and_compute_shape()
        scene.setSceneRect(scene.itemsBoundingRect())

    def scene(self):
        return self.myscene
    
    def get_custom_input_widget_classes(self):
        return self.main_window.custom_node_input_widget_classes

    def drawBackground(self, painter, rect):
        painter.fillRect(rect.intersected(self.sceneRect()), QColor('#333333'))
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.sceneRect())

    def pythagoras(self, a, b):
        return math.sqrt(a**2 + b**2)

    def get_img(self):
        # pixmap = self.render_view.grab(self.render_view.sceneRect().toRect())
        img = QImage(self.scene().sceneRect().size().toSize(), QImage.Format_ARGB32)
        img.fill(Qt.transparent)

        painter = QPainter(img)
        painter.setRenderHint(QPainter.Antialiasing)
        self.scene().render(painter)  # app crashes here for some reason
        # img.save('H:/Projekte/QT/PySide2/pyScript/pyScript_011/mypic.png')
        return img


class RenderScene(QGraphicsScene):
    def __init__(self):
        super(RenderScene, self).__init__()

        # self.render_view = view