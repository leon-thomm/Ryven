# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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

class Ui_main_widget(object):
    def setupUi(self, main_widget):
        if main_widget.objectName():
            main_widget.setObjectName(u"main_widget")
        main_widget.resize(1223, 876)
        self.gridLayout_5 = QGridLayout(main_widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.splitter = QSplitter(main_widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.contents_widget = QWidget(self.splitter)
        self.contents_widget.setObjectName(u"contents_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contents_widget.sizePolicy().hasHeightForWidth())
        self.contents_widget.setSizePolicy(sizePolicy)
        self.contents_widget.setMinimumSize(QSize(200, 0))
        self.verticalLayout = QVBoxLayout(self.contents_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.classes_group_box = QGroupBox(self.contents_widget)
        self.classes_group_box.setObjectName(u"classes_group_box")
        self.gridLayout_2 = QGridLayout(self.classes_group_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.classes_scrollArea = QScrollArea(self.classes_group_box)
        self.classes_scrollArea.setObjectName(u"classes_scrollArea")
        self.classes_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 771, 206))
        self.classes_scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_2.addWidget(self.classes_scrollArea, 0, 0, 1, 1)

        self.add_class_push_button = QPushButton(self.classes_group_box)
        self.add_class_push_button.setObjectName(u"add_class_push_button")

        self.gridLayout_2.addWidget(self.add_class_push_button, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.classes_group_box)

        self.variables_group_box = QGroupBox(self.contents_widget)
        self.variables_group_box.setObjectName(u"variables_group_box")
        self.gridLayout_3 = QGridLayout(self.variables_group_box)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.variables_scrollArea = QScrollArea(self.variables_group_box)
        self.variables_scrollArea.setObjectName(u"variables_scrollArea")
        self.variables_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 771, 206))
        self.variables_scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_3.addWidget(self.variables_scrollArea, 0, 0, 1, 1)

        self.add_variable_push_button = QPushButton(self.variables_group_box)
        self.add_variable_push_button.setObjectName(u"add_variable_push_button")

        self.gridLayout_3.addWidget(self.add_variable_push_button, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.variables_group_box)

        self.functions_groupBox = QGroupBox(self.contents_widget)
        self.functions_groupBox.setObjectName(u"functions_groupBox")
        self.gridLayout_4 = QGridLayout(self.functions_groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.functions_scrollArea = QScrollArea(self.functions_groupBox)
        self.functions_scrollArea.setObjectName(u"functions_scrollArea")
        self.functions_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 771, 206))
        self.functions_scrollArea.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_4.addWidget(self.functions_scrollArea, 0, 0, 1, 1)

        self.add_function_push_button = QPushButton(self.functions_groupBox)
        self.add_function_push_button.setObjectName(u"add_function_push_button")

        self.gridLayout_4.addWidget(self.add_function_push_button, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.functions_groupBox)

        self.splitter.addWidget(self.contents_widget)
        self.flows = QTabWidget(self.splitter)
        self.flows.setObjectName(u"flows")
        self.splitter.addWidget(self.flows)
        self.details_groupBox = QGroupBox(self.splitter)
        self.details_groupBox.setObjectName(u"details_groupBox")
        self.details_groupBox.setMinimumSize(QSize(200, 0))
        self.gridLayout = QGridLayout(self.details_groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.details_scrollArea = QScrollArea(self.details_groupBox)
        self.details_scrollArea.setObjectName(u"details_scrollArea")
        self.details_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 229, 815))
        self.details_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.details_scrollArea, 0, 0, 1, 1)

        self.splitter.addWidget(self.details_groupBox)

        self.gridLayout_5.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(main_widget)

        self.flows.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(main_widget)
    # setupUi

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QCoreApplication.translate("main_widget", u"Form", None))
        self.classes_group_box.setTitle(QCoreApplication.translate("main_widget", u"Classes", None))
        self.add_class_push_button.setText(QCoreApplication.translate("main_widget", u"add", None))
        self.variables_group_box.setTitle(QCoreApplication.translate("main_widget", u"Variables", None))
        self.add_variable_push_button.setText(QCoreApplication.translate("main_widget", u"add", None))
        self.functions_groupBox.setTitle(QCoreApplication.translate("main_widget", u"Functions", None))
        self.add_function_push_button.setText(QCoreApplication.translate("main_widget", u"add", None))
        self.details_groupBox.setTitle(QCoreApplication.translate("main_widget", u"Details", None))
    # retranslateUi

