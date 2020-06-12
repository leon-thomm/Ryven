from PySide2.QtWidgets import QWidget, QPushButton, QHBoxLayout, QSlider, QColorDialog
from PySide2.QtCore import Qt
from PySide2.QtGui import QColor


class FlowStylusModesWidget(QWidget):
    def __init__(self, flow):
        super(FlowStylusModesWidget, self).__init__()

        # GENERAL ATTRIBUTES
        self.flow = flow
        self.pen_color = QColor(255, 255, 0)

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
        self.pen_width_slider.setRange(1, 100)  # -> /10
        self.pen_width_slider.setValue(20)

        self.pen_style_widget = QWidget()
        pen_style_layout = QHBoxLayout()
        pen_style_layout.addWidget(self.pen_color_button)
        pen_style_layout.addWidget(self.pen_width_slider)

        self.pen_style_widget.setLayout(pen_style_layout)

        # MERGE SETTINGS
        self.settings_widget = QWidget()
        settings_layout = QHBoxLayout()
        settings_layout.addWidget(self.pen_style_widget)
        settings_layout.addWidget(self.set_stylus_mode_comment_button)
        settings_layout.addWidget(self.set_stylus_mode_edit_button)

        self.settings_widget.setLayout(settings_layout)


        # MAIN LAYOUT
        main_horizontal_layout = QHBoxLayout()

        main_horizontal_layout.addWidget(self.settings_widget)
        main_horizontal_layout.addWidget(self.stylus_button)

        self.setLayout(main_horizontal_layout)


        self.setStyleSheet('''
            background: transparent;
            border: none;
        ''')

        self.push_button_style_sheet_start = '''
            QPushButton:hover:pressed {
                background-color: rgba(100, 100, 100, 150);
            }
            QPushButton {
                border: 1px solid #aaaaaa;
                border-radius: 8px;
                height: 25px;
                width: 50px;'''  # color may be dynamic

        self.std_push_button_style_sheet = self.push_button_style_sheet_start + '''
                background-color: rgba(10, 10, 10, 150);
                color: #aaaaaa;
            }
        '''

        self.set_stylus_mode_comment_button.setStyleSheet(self.std_push_button_style_sheet)
        self.set_stylus_mode_edit_button.setStyleSheet(self.std_push_button_style_sheet)
        self.stylus_button.setStyleSheet(self.std_push_button_style_sheet)
        self.update_color_button_SS()

        self.stylus_button.setFixedWidth(50)
        self.set_stylus_mode_edit_button.setFixedWidth(60)
        self.set_stylus_mode_comment_button.setFixedWidth(60)

        self.pen_style_widget.hide()
        self.settings_widget.hide()


    def on_stylus_button_clicked(self):
        if self.settings_widget.isHidden():
            self.settings_widget.show()
        elif not self.settings_widget.isHidden():
            self.settings_widget.hide()
        self.adjustSize()
        self.flow.set_stylus_proxy_pos()

    def on_edit_button_clicked(self):
        self.flow.stylus_mode = 'edit'
        self.pen_style_widget.hide()

        # if I don't hide and show the settings_widget manually here, the stylus mode buttons take up the additional
        # space when clicking on comment and then edit. self.adjustSize() does not seem to work properly here...
        self.settings_widget.hide()
        self.settings_widget.show()

        self.adjustSize()
        self.flow.set_stylus_proxy_pos()
        # self.flow.setDragMode(QGraphicsView.RubberBandDrag)

    def on_comment_button_clicked(self):
        self.flow.stylus_mode = 'comment'
        self.pen_style_widget.show()
        self.adjustSize()
        self.flow.set_stylus_proxy_pos()
        # self.flow.setDragMode(QGraphicsView.NoDrag)

    def on_choose_color_clicked(self):
        self.pen_color = QColorDialog.getColor(self.pen_color, options=QColorDialog.ShowAlphaChannel,
                                               title='Choose pen color')
        self.update_color_button_SS()

    def update_color_button_SS(self):
        self.pen_color_button.setStyleSheet(self.push_button_style_sheet_start+'''
                color: black;
                background-color: '''+self.pen_color.name()+''';
            }''')

    def get_pen_settings(self):
        return {'color': self.pen_color.name(),
                'base stroke weight': self.pen_width_slider.value()/10}