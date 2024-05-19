from typing import List, Tuple
from enum import Enum

from qtpy.QtCore import (
    QTimeLine, 
    QPropertyAnimation, 
    QParallelAnimationGroup,
    QEasingCurve, 
)
from qtpy.QtGui import (
    QPen,
    QBrush, 
)
from qtpy.QtWidgets import (
    QGraphicsItem,
    QGraphicsObject,
)

from ...GUIBase import QGraphicsItemAnimated


class ConnPathItemsAnimation(QGraphicsObject):
    """
    Animates items over the path of a connection by updating their positions.
    When the path of the connection changes, recompute() needs to be called.
    The animation can be toggled on and off.
    """

    def __init__(
        self,
        items: List[QGraphicsItem],
        connection,
        frames=100,
        between=125,
        speed=0.15,
    ):
        super().__init__()
        
        self.items: List[QGraphicsItemAnimated] = [
            QGraphicsItemAnimated(item, self) 
            for item in items
        ]
        self.connection = connection
        self.between = between
        self.speed = speed
        self.visible_items: List[Tuple[QGraphicsItemAnimated, float]] = []
        self.__visible_flag = True
        
        self.setParentItem(self.connection)
        
        self.timeline = QTimeLine()
        self.timeline.setFrameRange(0, frames)
        self.timeline.setEasingCurve(QEasingCurve(QEasingCurve.Type.Linear))
        self.timeline.valueChanged.connect(self._update_items)
        self.timeline.setLoopCount(0)

    def boundingRect(self):
        return self.connection.boundingRect()
    
    def paint(self, painter, option, widget):
        pass
    
    def toggle(self, recompute: bool = False):
        """Toggles the path animation. Returns True if toggled on, otherwise False"""

        state = self.timeline.state()
        running = False
        if state == QTimeLine.NotRunning:
            self.timeline.start()
            running = True
        elif state == QTimeLine.Paused:
            self.timeline.resume()
            running = True
        else:
            running = False
            self.timeline.setPaused(True)
        
        if recompute:
            self.recompute()
        return running
    
    def start(self, recompute: bool = True):
        self.timeline.start()
        if recompute:
            self.recompute()

    def stop(self, recompute: bool = True):
        self.timeline.stop()
        if recompute:
            self.recompute()

    def recompute(self):
        
        if self.__visible_flag:
            for item in self.items:
                item.setVisible(False)
            self.__visible_flag = False

        if self.timeline.state() == QTimeLine.State.NotRunning:
            return
        
        self.__visible_flag = True

        path_len = self.connection.path().length()
        num_points = max(3, min(self.connection.num_dots, int(path_len / self.between)))

        self.timeline.setDuration(path_len / self.speed)
        self.visible_items = []

        for i in range(1, num_points + 1):
            percent = i / num_points
            item = self.items[i - 1]
            self.visible_items.append((item, percent))
            item.setVisible(True)
            item.item.setPen(QPen(self.connection.get_style_color(), self.connection.pen_width()))
            item.item.setBrush(QBrush(self.connection.get_style_color()))

    def _update_items(self, percent):
        for item, item_percent in self.visible_items:
            p = percent + item_percent
            if p > 1:
                p = p - 1
            item.setPos(self.connection.path().pointAtPercent(p))

    def _pause(self, paused: bool, recompute: bool = True):
        self.timeline.setPaused(paused)
        if recompute:
            self.recompute()

    def _state(self):
        return self.timeline.state()
    

class ConnPathItemsAnimationScaled:
    """
    Wraps a ConnPathItemsAnimation and adds a scale animation to it.
    """

    class State(Enum):
        NOT_RUNNING = 0
        RUNNING = 1
        TO_SCALE = 2
        TO_ZERO = 3
    
    def __init__(
        self,
        items_animation: ConnPathItemsAnimation,
        duration: int = 750, 
        scale: int = 1, 
    ) -> None:
        
        self.con_items_anim = items_animation
        self.duration = duration
        self.scalar = scale
        self.to_scalar_group = QParallelAnimationGroup()
        self.to_zero_group = QParallelAnimationGroup()
        self.state = ConnPathItemsAnimationScaled.State.NOT_RUNNING
        
        for item in self.con_items_anim.items:
            item.setScale(0)
            # to scaler
            to_scalar_anim = QPropertyAnimation(item, b'scale')  # type: ignore
            to_scalar_anim.setDuration(self.duration)
            self.to_scalar_group.addAnimation(to_scalar_anim)
            # to zero
            to_zero_anim = QPropertyAnimation(item, b'scale')  # type: ignore
            to_zero_anim.setDuration(self.duration)
            self.to_zero_group.addAnimation(to_zero_anim)

        self.to_scalar_group.finished.connect(self._on_scalar_ended)
        self.to_zero_group.finished.connect(self._on_zero_ended)
    
    def start(self):
        if (self.state == ConnPathItemsAnimationScaled.State.NOT_RUNNING or 
            self.state == ConnPathItemsAnimationScaled.State.TO_ZERO):
            self.toggle()
    
    def stop(self):
        if (self.state == ConnPathItemsAnimationScaled.State.RUNNING or
            self.state == ConnPathItemsAnimationScaled.State.TO_SCALE):
            self.toggle()
            
    def toggle(self):
        if self.state == ConnPathItemsAnimationScaled.State.NOT_RUNNING:
            self._run_scalar()
            self.con_items_anim.start()
            self.state = ConnPathItemsAnimationScaled.State.TO_SCALE
        elif self.state == ConnPathItemsAnimationScaled.State.RUNNING:
            self._run_zero()
            self.state = ConnPathItemsAnimationScaled.State.TO_ZERO
        elif self.state == ConnPathItemsAnimationScaled.State.TO_SCALE:
            self.to_scalar_group.stop()
            self._run_zero()
            self.state = ConnPathItemsAnimationScaled.State.TO_ZERO
        else:
            self.to_zero_group.stop()
            self._run_scalar()
            self.state = ConnPathItemsAnimationScaled.State.TO_SCALE
    
    def force_stop(self):
        self.to_zero_group.stop()
        self.to_scalar_group.stop()
    
    def _run_scalar(self):
        self._run_animation(self.to_scalar_group, self.scalar)
    
    def _run_zero(self):
        self._run_animation(self.to_zero_group, 0)
        
    def _run_animation(self, group: QParallelAnimationGroup, end_value):
        for i in range(group.animationCount()):
            anim: QPropertyAnimation = group.animationAt(i)
            target: QGraphicsItem = anim.targetObject()
            anim.setKeyValues([(0, target.scale()), (1, end_value)])
        group.start()
    
    def _on_scalar_ended(self):
        self.state = ConnPathItemsAnimationScaled.State.RUNNING
    
    def _on_zero_ended(self):
        if self.state == ConnPathItemsAnimationScaled.State.TO_ZERO:
            self.con_items_anim.stop()
        self.state = ConnPathItemsAnimationScaled.State.NOT_RUNNING