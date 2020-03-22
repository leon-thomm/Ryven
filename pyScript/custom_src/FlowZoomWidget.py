from PySide2.QtWidgets import QWidget, QPushButton, QHBoxLayout


class FlowZoomWidget(QWidget):
    def __init__(self, flow):
        super(FlowZoomWidget, self).__init__()

        self.flow = flow

        self.zoom_in_button = QPushButton('+')
        self.zoom_in_button.clicked.connect(self.on_zoom_in_button_clicked)
        self.zoom_out_button = QPushButton('-')
        self.zoom_out_button.clicked.connect(self.on_zoom_out_button_clicked)

        main_horizontal_layout = QHBoxLayout()

        main_horizontal_layout.addWidget(self.zoom_out_button)
        main_horizontal_layout.addWidget(self.zoom_in_button)
        self.setLayout(main_horizontal_layout)


        self.setStyleSheet('''
            background: transparent;
            border: none;
        ''')

        self.zoom_in_button.setStyleSheet('''
            QPushButton {
                background-color: rgba(10, 10, 10, 150);
                border: 1px solid #aaaaaa;
                border-radius: 8px;
                color: #aaaaaa;
                height: 35px;
                width: 35px;
            }
            QPushButton:hover:pressed {
                background-color: rgba(100, 100, 100, 150);
            }
        ''')

        self.zoom_out_button.setStyleSheet('''
            QPushButton {
                background-color: rgba(10, 10, 10, 150);
                border: 1px solid #aaaaaa;
                border-radius: 8px;
                color: #aaaaaa;
                height: 35px;
                width: 35px;
            }
            QPushButton:hover:pressed {
                background-color: rgba(100, 100, 100, 150);
            }
        ''')


    def on_zoom_in_button_clicked(self):
        self.flow.zoom_in(250)

    def on_zoom_out_button_clicked(self):
        self.flow.zoom_out(250)