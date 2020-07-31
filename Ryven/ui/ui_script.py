# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'script.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_script_widget(object):
    def setupUi(self, script_widget):
        if not script_widget.objectName():
            script_widget.setObjectName(u"script_widget")
        script_widget.resize(1223, 876)
        self.gridLayout_4 = QGridLayout(script_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.splitter_3 = QSplitter(script_widget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.splitter = QSplitter(self.splitter_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter_2 = QSplitter(self.splitter)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.log_groupBox = QGroupBox(self.splitter_2)
        self.log_groupBox.setObjectName(u"log_groupBox")
        self.gridLayout_2 = QGridLayout(self.log_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.logs_scrollArea = QScrollArea(self.log_groupBox)
        self.logs_scrollArea.setObjectName(u"logs_scrollArea")
        self.logs_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 392, 815))
        self.logs_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.logs_scrollArea, 0, 0, 1, 1)

        self.splitter_2.addWidget(self.log_groupBox)
        self.source_code_groupBox = QGroupBox(self.splitter_2)
        self.source_code_groupBox.setObjectName(u"source_code_groupBox")
        self.gridLayout = QGridLayout(self.source_code_groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter_2.addWidget(self.source_code_groupBox)
        self.splitter.addWidget(self.splitter_2)
        self.splitter_3.addWidget(self.splitter)
        self.contents_widget = QWidget(self.splitter_3)
        self.contents_widget.setObjectName(u"contents_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contents_widget.sizePolicy().hasHeightForWidth())
        self.contents_widget.setSizePolicy(sizePolicy)
        self.contents_widget.setMinimumSize(QSize(200, 0))
        self.verticalLayout = QVBoxLayout(self.contents_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.settings_groupBox = QGroupBox(self.contents_widget)
        self.settings_groupBox.setObjectName(u"settings_groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.settings_groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.settings_groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.algorithm_data_flow_radioButton = QRadioButton(self.settings_groupBox)
        self.algorithm_buttonGroup = QButtonGroup(script_widget)
        self.algorithm_buttonGroup.setObjectName(u"algorithm_buttonGroup")
        self.algorithm_buttonGroup.addButton(self.algorithm_data_flow_radioButton)
        self.algorithm_data_flow_radioButton.setObjectName(u"algorithm_data_flow_radioButton")
        self.algorithm_data_flow_radioButton.setMaximumSize(QSize(16777210, 16777215))
        self.algorithm_data_flow_radioButton.setChecked(True)

        self.verticalLayout_3.addWidget(self.algorithm_data_flow_radioButton)

        self.algorithm_exec_flow_radioButton = QRadioButton(self.settings_groupBox)
        self.algorithm_buttonGroup.addButton(self.algorithm_exec_flow_radioButton)
        self.algorithm_exec_flow_radioButton.setObjectName(u"algorithm_exec_flow_radioButton")

        self.verticalLayout_3.addWidget(self.algorithm_exec_flow_radioButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.settings_groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.viewport_update_mode_sync_radioButton = QRadioButton(self.settings_groupBox)
        self.viewport_update_mode_buttonGroup = QButtonGroup(script_widget)
        self.viewport_update_mode_buttonGroup.setObjectName(u"viewport_update_mode_buttonGroup")
        self.viewport_update_mode_buttonGroup.addButton(self.viewport_update_mode_sync_radioButton)
        self.viewport_update_mode_sync_radioButton.setObjectName(u"viewport_update_mode_sync_radioButton")
        self.viewport_update_mode_sync_radioButton.setChecked(True)

        self.verticalLayout_2.addWidget(self.viewport_update_mode_sync_radioButton)

        self.viewport_update_mode_async_radioButton = QRadioButton(self.settings_groupBox)
        self.viewport_update_mode_buttonGroup.addButton(self.viewport_update_mode_async_radioButton)
        self.viewport_update_mode_async_radioButton.setObjectName(u"viewport_update_mode_async_radioButton")

        self.verticalLayout_2.addWidget(self.viewport_update_mode_async_radioButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.settings_groupBox)

        self.variables_group_box = QGroupBox(self.contents_widget)
        self.variables_group_box.setObjectName(u"variables_group_box")
        self.gridLayout_3 = QGridLayout(self.variables_group_box)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.variables_scrollArea = QScrollArea(self.variables_group_box)
        self.variables_scrollArea.setObjectName(u"variables_scrollArea")
        self.variables_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 628, 593))
        self.variables_scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_3.addWidget(self.variables_scrollArea, 0, 0, 1, 1)

        self.add_variable_push_button = QPushButton(self.variables_group_box)
        self.add_variable_push_button.setObjectName(u"add_variable_push_button")

        self.gridLayout_3.addWidget(self.add_variable_push_button, 2, 0, 1, 1)

        self.new_var_name_lineEdit = QLineEdit(self.variables_group_box)
        self.new_var_name_lineEdit.setObjectName(u"new_var_name_lineEdit")

        self.gridLayout_3.addWidget(self.new_var_name_lineEdit, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.variables_group_box)

        self.splitter_3.addWidget(self.contents_widget)

        self.gridLayout_4.addWidget(self.splitter_3, 0, 0, 1, 1)


        self.retranslateUi(script_widget)

        QMetaObject.connectSlotsByName(script_widget)
    # setupUi

    def retranslateUi(self, script_widget):
        script_widget.setWindowTitle(QCoreApplication.translate("script_widget", u"Form", None))
        self.log_groupBox.setTitle(QCoreApplication.translate("script_widget", u"Log", None))
        self.source_code_groupBox.setTitle(QCoreApplication.translate("script_widget", u"Source Code", None))
        self.settings_groupBox.setTitle(QCoreApplication.translate("script_widget", u"Settings", None))
        self.label_2.setText(QCoreApplication.translate("script_widget", u"Algorithm", None))
        self.algorithm_data_flow_radioButton.setText(QCoreApplication.translate("script_widget", u"Data Flow", None))
        self.algorithm_exec_flow_radioButton.setText(QCoreApplication.translate("script_widget", u"Exec Flow", None))
        self.label.setText(QCoreApplication.translate("script_widget", u"Viewport Update Mode", None))
        self.viewport_update_mode_sync_radioButton.setText(QCoreApplication.translate("script_widget", u"Sync", None))
        self.viewport_update_mode_async_radioButton.setText(QCoreApplication.translate("script_widget", u"Async", None))
        self.variables_group_box.setTitle(QCoreApplication.translate("script_widget", u"Variables", None))
        self.add_variable_push_button.setText(QCoreApplication.translate("script_widget", u"add", None))
        self.new_var_name_lineEdit.setPlaceholderText(QCoreApplication.translate("script_widget", u"new var name", None))
    # retranslateUi

