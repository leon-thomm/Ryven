from qtpy.QtWidgets import QWidget, QPushButton, QHBoxLayout, QSlider, QColorDialog
from qtpy.QtCore import Qt
from qtpy.QtGui import QColor


class FlowViewStylusModesWidget(QWidget):
    def __init__(self, flow_view):
        super(FlowViewStylusModesWidget, self).__init__()

        self.setObjectName('FlowViewStylusModesWidget')

        # GENERAL ATTRIBUTES
        self.flow_view = flow_view
        self.pen_color = QColor(255, 255, 0)
        self.stylus_buttons_visible = True

        # stylus button
        self.stylus_button = QPushButton('stylus')  # show/hide
        self.stylus_button.clicked.connect(self.on_stylus_button_clicked)

        # mode
        self.set_stylus_mode_comment_button = QPushButton('comment')
        self.set_stylus_mode_comment_button.clicked.connect(self.on_comment_button_clicked)
        self.set_stylus_mode_edit_button = QPushButton('edit')
        self.set_stylus_mode_edit_button.clicked.connect(self.on_edit_button_clicked)

        # pen style
        self.pen_color_button = QPushButton('color')
        self.pen_color_button.clicked.connect(self.on_choose_color_clicked)
        self.pen_width_slider = QSlider(Qt.Horizontal)
        self.pen_width_slider.setRange(1, 100)
        self.pen_width_slider.setValue(20)


        # MAIN LAYOUT
        main_horizontal_layout = QHBoxLayout()

        main_horizontal_layout.addWidget(self.pen_color_button)
        main_horizontal_layout.addWidget(self.pen_width_slider)
        main_horizontal_layout.addWidget(self.set_stylus_mode_comment_button)
        main_horizontal_layout.addWidget(self.set_stylus_mode_edit_button)
        main_horizontal_layout.addWidget(self.stylus_button)

        self.setLayout(main_horizontal_layout)

        self.setStyleSheet('''
        QWidget#FlowViewStylusModesWidget {
            background: transparent; 
        }
                ''')

        self.hide_stylus_buttons()
        self.hide_pen_style_widgets()

    def pen_width(self):
        return self.pen_width_slider.value()/20

    def hide_stylus_buttons(self):
        self.set_stylus_mode_edit_button.hide()
        self.set_stylus_mode_comment_button.hide()
        self.stylus_buttons_visible = False

    def show_stylus_buttons(self):
        self.set_stylus_mode_edit_button.show()
        self.set_stylus_mode_comment_button.show()
        self.stylus_buttons_visible = True

    def hide_pen_style_widgets(self):
        self.pen_color_button.hide()
        self.pen_width_slider.hide()

    def show_pen_style_widgets(self):
        self.pen_color_button.show()
        self.pen_width_slider.show()

    def on_stylus_button_clicked(self):
        if self.stylus_buttons_visible:
            self.hide_pen_style_widgets()
            self.hide_stylus_buttons()
        else:
            self.show_stylus_buttons()

        self.adjustSize()
        self.flow_view.set_stylus_proxy_pos()

    def on_edit_button_clicked(self):
        self.flow_view.stylus_mode = 'edit'
        # self.pen_style_widget.hide()
        self.hide_pen_style_widgets()

        # if I don't hide and show the settings_widget manually here, the stylus mode buttons take up the additional
        # space when clicking on comment and then edit. self.adjustSize() does not seem to work properly here...
        self.hide_stylus_buttons()
        self.show_stylus_buttons()
        # self.settings_widget.hide()
        # self.settings_widget.show()

        self.adjustSize()
        self.flow_view.set_stylus_proxy_pos()
        # self.flow.setDragMode(QGraphicsView.RubberBandDrag)

    def on_comment_button_clicked(self):
        self.flow_view.stylus_mode = 'comment'
        # self.pen_style_widget.show()
        self.show_pen_style_widgets()
        self.adjustSize()
        self.flow_view.set_stylus_proxy_pos()
        # self.flow.setDragMode(QGraphicsView.NoDrag)

    def on_choose_color_clicked(self):
        self.pen_color = QColorDialog.getColor(self.pen_color, options=QColorDialog.ShowAlphaChannel,
                                               title='Choose pen color')
        self.update_color_button_SS()


    def update_color_button_SS(self):

        self.pen_color_button.setStyleSheet(
            '''
QPushButton {
    background-color: '''+self.pen_color.name()+''';
}'''
        )

    def get_pen_settings(self):
        return {'color': self.pen_color.name(),
                'base stroke weight': self.pen_width_slider.value()/10}