from PySide2.QtWidgets import QWidget, QPushButton, QHBoxLayout


class FlowStylusModesWidget(QWidget):
    def __init__(self, flow):
        super(FlowStylusModesWidget, self).__init__()

        self.flow = flow

        self.set_stylus_mode_comment_button = QPushButton('comment')
        self.set_stylus_mode_comment_button.clicked.connect(self.on_comment_button_clicked)
        self.set_stylus_mode_edit_button = QPushButton('edit')
        self.set_stylus_mode_edit_button.clicked.connect(self.on_edit_button_clicked)

        main_horizontal_layout = QHBoxLayout()

        self.mode_buttons_widget = QWidget()
        mode_buttons_layout = QHBoxLayout()
        mode_buttons_layout.addWidget(self.set_stylus_mode_comment_button)
        mode_buttons_layout.addWidget(self.set_stylus_mode_edit_button)
        self.mode_buttons_widget.setLayout(mode_buttons_layout)

        self.stylus_button = QPushButton('stylus')  # show/hide
        self.stylus_button.clicked.connect(self.on_stylus_button_clicked)

        main_horizontal_layout.addWidget(self.mode_buttons_widget)
        main_horizontal_layout.addWidget(self.stylus_button)
        self.setLayout(main_horizontal_layout)


        self.setStyleSheet('''
            background: transparent;
            border: none;
        ''')

        self.set_stylus_mode_comment_button.setStyleSheet('''
            QPushButton {
                background-color: rgba(10, 10, 10, 150);
                border: 1px solid #aaaaaa;
                border-radius: 8px;
                color: #aaaaaa;
                height: 25px;
                width: 50px;
            }
            QPushButton:hover:pressed {
                background-color: rgba(100, 100, 100, 150);
            }
        ''')

        self.set_stylus_mode_edit_button.setStyleSheet('''
            QPushButton {
                background-color: rgba(10, 10, 10, 150);
                border: 1px solid #aaaaaa;
                border-radius: 8px;
                color: #aaaaaa;
                height: 25px;
                width: 50px;
            }
            QPushButton:hover:pressed {
                background-color: rgba(100, 100, 100, 150);
            }
        ''')

        self.stylus_button.setStyleSheet('''
            QPushButton {
                background-color: rgba(10, 10, 10, 150);
                border: 1px solid #aaaaaa;
                border-radius: 8px;
                color: #aaaaaa;
                height: 25px;
                width: 50px;
            }
            QPushButton:hover:pressed {
                background-color: rgba(100, 100, 100, 150);
            }
        ''')
        self.stylus_button.setFixedWidth(50)

        self.mode_buttons_widget.hide()


    def on_stylus_button_clicked(self):
        if self.mode_buttons_widget.isHidden():
            self.mode_buttons_widget.show()
        elif not self.mode_buttons_widget.isHidden():
            self.mode_buttons_widget.hide()
        self.adjustSize()
        self.flow.set_stylus_proxy_pos()

    def on_edit_button_clicked(self):
        self.flow.stylus_mode = 'edit'

    def on_comment_button_clicked(self):
        self.flow.stylus_mode = 'comment'