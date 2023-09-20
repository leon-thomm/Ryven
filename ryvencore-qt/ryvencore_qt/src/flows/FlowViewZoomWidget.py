from qtpy.QtWidgets import QWidget, QPushButton, QHBoxLayout


class FlowViewZoomWidget(QWidget):
    def __init__(self, flow_view):
        super(FlowViewZoomWidget, self).__init__()

        self.flow_view = flow_view

        self.setObjectName('FlowViewZoomWidget')

        self.zoom_in_button = QPushButton('+')
        self.zoom_in_button.clicked.connect(self.on_zoom_in_button_clicked)
        self.zoom_out_button = QPushButton('-')
        self.zoom_out_button.clicked.connect(self.on_zoom_out_button_clicked)

        main_horizontal_layout = QHBoxLayout()

        main_horizontal_layout.addWidget(self.zoom_out_button)
        main_horizontal_layout.addWidget(self.zoom_in_button)
        self.setLayout(main_horizontal_layout)

        self.setStyleSheet('''
QWidget#FlowViewZoomWidget {
    background: transparent; 
}
        ''')


    def on_zoom_in_button_clicked(self):
        self.flow_view.zoom_in(250)

    def on_zoom_out_button_clicked(self):
        self.flow_view.zoom_out(250)