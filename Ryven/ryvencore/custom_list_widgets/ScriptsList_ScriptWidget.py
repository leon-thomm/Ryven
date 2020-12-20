from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QMenu, QAction
from PySide2.QtGui import QIcon, QImage
from PySide2.QtCore import Qt, QEvent

import json

from ryvencore.custom_list_widgets.ListWidget_NameLineEdit import ListWidget_NameLineEdit


class ScriptsList_ScriptWidget(QWidget):
    """Single script representing component for ScriptsListWidget.
    See ScriptsListWidget for further info."""

    # title_LE_editing_finished = Signal()

    def __init__(self, scripts_list_widget, session, script):
        super(ScriptsList_ScriptWidget, self).__init__()

        self.session = session
        self.script = script
        self.scripts_list_widget = scripts_list_widget
        self.previous_script_title = ''

        self.ignore_title_line_edit_signal = False


        # UI
        main_layout = QHBoxLayout()

        # create icon via label
        script_icon = QIcon('../resources/pics/script_picture.png')
        icon_label = QLabel()
        icon_label.setFixedSize(20, 20)
        icon_label.setStyleSheet('border:none;')
        icon_label.setPixmap(script_icon.pixmap(20, 20))
        main_layout.addWidget(icon_label)

        self.title_line_edit = ListWidget_NameLineEdit(script.title, self)
        self.title_line_edit.setPlaceholderText('title')
        self.title_line_edit.setEnabled(False)
        self.title_line_edit.editingFinished.connect(self.title_line_edit_editing_finished)
        self.title_line_edit.unfocused.connect(self.title_line_edit_editing_finished)

        # name_type_layout = QVBoxLayout()
        # name_type_layout.addWidget(self.title_line_edit)
        main_layout.addWidget(self.title_line_edit)

        self.setLayout(main_layout)



    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.title_line_edit.geometry().contains(event.pos()):
                self.title_line_edit_double_clicked()
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
            self.script.thumbnail_source = 'temp/script_' + self.script.title + '_thumbnail.png'
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


    def title_line_edit_double_clicked(self):
        self.title_line_edit.setEnabled(True)
        self.title_line_edit.setFocus()
        self.title_line_edit.selectAll()

        # self.scripts_list_widget.currently_edited_script = self.script
        self.previous_script_title = self.title_line_edit.text()


    def get_drag_data(self):
        data = {'type': 'script',
                'title': self.script.title}
        data_text = json.dumps(data)
        return data_text



    def title_line_edit_editing_finished(self):
        if self.ignore_title_line_edit_signal:
            return

        title = self.title_line_edit.text()

        self.ignore_title_line_edit_signal = True
        # self.title_LE_editing_finished.emit()
        if not self.session.check_new_script_title_validity(title):
            self.title_line_edit.setText(self.previous_script_title)
            return

        # rename script
        self.title_line_edit.setEnabled(False)
        self.script.title = title
        self.session.rename_script(script=self.script, title=title)

        self.ignore_title_line_edit_signal = False
