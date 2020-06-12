import enum


class MovementEnum(enum.Enum):
    """bug test: click on NI, drag, then use shortcut movement and release. Should result in a double undo stack push
    this should get removed later, it's an ugly implementation"""
    mouse_clicked = 1
    position_changed = 2
    mouse_released = 3