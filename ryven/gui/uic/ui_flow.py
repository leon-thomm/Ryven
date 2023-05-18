# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *


class Ui_flow_widget(object):
    def setupUi(self, flow_widget):
        if not flow_widget.objectName():
            flow_widget.setObjectName(u"flow_widget")
        flow_widget.resize(1223, 876)
        self.gridLayout_4 = QGridLayout(flow_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.splitter_3 = QSplitter(flow_widget)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 544, 818))
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
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
        self.gridLayout_5 = QGridLayout(self.contents_widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.settings_vars_splitter = QSplitter(self.contents_widget)
        self.settings_vars_splitter.setObjectName(u"settings_vars_splitter")
        self.settings_vars_splitter.setOrientation(Qt.Vertical)
        self.settings_groupBox = QGroupBox(self.settings_vars_splitter)
        self.settings_groupBox.setObjectName(u"settings_groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.settings_groupBox.sizePolicy().hasHeightForWidth())
        self.settings_groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.settings_groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.settings_vars_splitter.addWidget(self.settings_groupBox)
        self.variables_group_box = QGroupBox(self.settings_vars_splitter)
        self.variables_group_box.setObjectName(u"variables_group_box")
        self.gridLayout_3 = QGridLayout(self.variables_group_box)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.settings_vars_splitter.addWidget(self.variables_group_box)

        self.gridLayout_5.addWidget(self.settings_vars_splitter, 0, 0, 1, 1)

        self.splitter_3.addWidget(self.contents_widget)

        self.gridLayout_4.addWidget(self.splitter_3, 0, 0, 1, 1)


        self.retranslateUi(flow_widget)

        QMetaObject.connectSlotsByName(flow_widget)
    # setupUi

    def retranslateUi(self, flow_widget):
        flow_widget.setWindowTitle(QCoreApplication.translate("flow_widget", u"Form", None))
        self.log_groupBox.setTitle(QCoreApplication.translate("flow_widget", u"Log", None))
        self.source_code_groupBox.setTitle(QCoreApplication.translate("flow_widget", u"Source Code", None))
        self.settings_groupBox.setTitle(QCoreApplication.translate("flow_widget", u"Settings", None))
        self.variables_group_box.setTitle(QCoreApplication.translate("flow_widget", u"Variables", None))
    # retranslateUi

