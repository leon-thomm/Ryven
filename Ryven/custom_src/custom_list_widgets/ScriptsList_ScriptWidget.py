from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QMenu, QAction
from PySide2.QtGui import QIcon, QImage
from PySide2.QtCore import Signal, Qt, QEvent

import json

from custom_src.custom_list_widgets.ListWidget_NameLineEdit import ListWidget_NameLineEdit


class ScriptsList_ScriptWidget(QWidget):
    """Single script representing component for ScriptsListWidget.
    See ScriptsListWidget for further info."""

    name_LE_editing_finished = Signal()

    def __init__(self, scripts_list_widget, script):
        super(ScriptsList_ScriptWidget, self).__init__()

        self.script = script
        self.scripts_list_widget = scripts_list_widget

        self.ignore_name_line_edit_signal = False


        # UI
        main_layout = QHBoxLayout()

        # create icon via label
        script_icon = QIcon('../resources/pics/script_picture.png')
        icon_label = QLabel()
        icon_label.setFixedSize(20, 20)
        icon_label.setStyleSheet('border:none;')
        icon_label.setPixmap(script_icon.pixmap(20, 20))
        main_layout.addWidget(icon_label)

        # create name and data_type line edits
        self.name_line_edit = ListWidget_NameLineEdit(script.name, self)
        self.name_line_edit.setPlaceholderText('name')
        self.name_line_edit.setEnabled(False)
        self.name_line_edit.editingFinished.connect(self.name_line_edit_editing_finished)
        self.name_line_edit.unfocused.connect(self.name_line_edit_editing_finished)

        name_type_layout = QVBoxLayout()
        name_type_layout.addWidget(self.name_line_edit)
        main_layout.addLayout(name_type_layout)

        self.setLayout(main_layout)



    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.name_line_edit.geometry().contains(event.pos()):
                self.name_line_edit_double_clicked()
                return


    # TODO: (maybe) Script migration via drag and drop
    #
    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         drag = QDrag(self)
    #         mime_data = QMimeData()
    #         data_text = self.get_drag_data()
    #         data = QByteArray(bytes(data_text, 'utf-8'))
    #         mime_data.setData('text/plain', data)
    #         drag.setMimeData(mime_data)
    #         drop_action = drag.exec_()
    #         return


    def event(self, event):
        if event.type() == QEvent.ToolTip:
            img: QImage = self.script.flow.get_viewport_img()
            self.script.thumbnail_source = 'temp/script_'+self.script.name+'_thumbnail.png'
            img.save(self.script.thumbnail_source)
            self.setToolTip('<img height=100 src="'+self.script.thumbnail_source+'"/>')

        return QWidget.event(self, event)


    def contextMenuEvent(self, event):
        menu: QMenu = QMenu(self)

        delete_action = QAction('delete')
        delete_action.triggered.connect(self.action_delete_triggered)

        actions = [delete_action]
        for a in actions:
            menu.addAction(a)

        menu.exec_(event.globalPos())


    def action_delete_triggered(self):
        self.scripts_list_widget.del_script(self.script, self)


    def name_line_edit_double_clicked(self):
        self.name_line_edit.setEnabled(True)
        self.name_line_edit.setFocus()
        self.name_line_edit.selectAll()

        self.scripts_list_widget.currently_edited_script = self.script


    def get_drag_data(self):
        data = {'type': 'script',
                'name': self.script.name}
        data_text = json.dumps(data)
        return data_text



    def name_line_edit_editing_finished(self):
        if self.ignore_name_line_edit_signal:
            return
        self.ignore_name_line_edit_signal = True
        self.name_LE_editing_finished.emit()
        self.ignore_name_line_edit_signal = False