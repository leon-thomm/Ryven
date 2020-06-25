# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'class_new.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_class_widget(object):
    def setupUi(self, class_widget):
        if class_widget.objectName():
            class_widget.setObjectName(u"class_widget")
        class_widget.resize(1107, 722)
        self.gridLayout_4 = QGridLayout(class_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.splitter = QSplitter(class_widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.contents_widget = QWidget(self.splitter)
        self.contents_widget.setObjectName(u"contents_widget")
        self.contents_widget.setMinimumSize(QSize(200, 0))
        self.verticalLayout = QVBoxLayout(self.contents_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.variables_groupBox = QGroupBox(self.contents_widget)
        self.variables_groupBox.setObjectName(u"variables_groupBox")
        self.gridLayout = QGridLayout(self.variables_groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.variables_scrollArea = QScrollArea(self.variables_groupBox)
        self.variables_scrollArea.setObjectName(u"variables_scrollArea")
        self.variables_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 204, 270))
        self.variables_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.variables_scrollArea, 0, 0, 1, 1)

        self.add_variable_pushButton = QPushButton(self.variables_groupBox)
        self.add_variable_pushButton.setObjectName(u"add_variable_pushButton")

        self.gridLayout.addWidget(self.add_variable_pushButton, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.variables_groupBox)

        self.functions_groupBox = QGroupBox(self.contents_widget)
        self.functions_groupBox.setObjectName(u"functions_groupBox")
        self.gridLayout_2 = QGridLayout(self.functions_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.functions_scrollArea = QScrollArea(self.functions_groupBox)
        self.functions_scrollArea.setObjectName(u"functions_scrollArea")
        self.functions_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 204, 270))
        self.functions_scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_2.addWidget(self.functions_scrollArea, 0, 0, 1, 1)

        self.add_function_pushButton = QPushButton(self.functions_groupBox)
        self.add_function_pushButton.setObjectName(u"add_function_pushButton")

        self.gridLayout_2.addWidget(self.add_function_pushButton, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.functions_groupBox)

        self.splitter.addWidget(self.contents_widget)
        self.flows = QTabWidget(self.splitter)
        self.flows.setObjectName(u"flows")
        self.splitter.addWidget(self.flows)
        self.details_groupBox = QGroupBox(self.splitter)
        self.details_groupBox.setObjectName(u"details_groupBox")
        self.details_groupBox.setMinimumSize(QSize(200, 0))
        self.gridLayout_3 = QGridLayout(self.details_groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.details_scrollArea = QScrollArea(self.details_groupBox)
        self.details_scrollArea.setObjectName(u"details_scrollArea")
        self.details_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 298, 661))
        self.details_scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_3.addWidget(self.details_scrollArea, 0, 0, 1, 1)

        self.splitter.addWidget(self.details_groupBox)

        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(class_widget)

        QMetaObject.connectSlotsByName(class_widget)
    # setupUi

    def retranslateUi(self, class_widget):
        class_widget.setWindowTitle(QCoreApplication.translate("class_widget", u"Form", None))
        self.variables_groupBox.setTitle(QCoreApplication.translate("class_widget", u"Variables", None))
        self.add_variable_pushButton.setText(QCoreApplication.translate("class_widget", u"add", None))
        self.functions_groupBox.setTitle(QCoreApplication.translate("class_widget", u"Methods", None))
        self.add_function_pushButton.setText(QCoreApplication.translate("class_widget", u"add", None))
        self.details_groupBox.setTitle(QCoreApplication.translate("class_widget", u"Details", None))
    # retranslateUi

