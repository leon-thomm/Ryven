# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'node_manager_mainwindow.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1185, 778)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.nodes_list_widget = QWidget(self.splitter)
        self.nodes_list_widget.setObjectName(u"nodes_list_widget")
        self.gridLayout = QGridLayout(self.nodes_list_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.nodes_groupBox = QGroupBox(self.nodes_list_widget)
        self.nodes_groupBox.setObjectName(u"nodes_groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodes_groupBox.sizePolicy().hasHeightForWidth())
        self.nodes_groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.nodes_groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nodes_scrollArea = QScrollArea(self.nodes_groupBox)
        self.nodes_scrollArea.setObjectName(u"nodes_scrollArea")
        self.nodes_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 958, 545))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.nodes_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.nodes_scrollArea)


        self.verticalLayout_2.addWidget(self.nodes_groupBox)

        self.node_list_actions_verticalLayout = QVBoxLayout()
        self.node_list_actions_verticalLayout.setObjectName(u"node_list_actions_verticalLayout")
        self.add_new_node_pushButton = QPushButton(self.nodes_list_widget)
        self.add_new_node_pushButton.setObjectName(u"add_new_node_pushButton")

        self.node_list_actions_verticalLayout.addWidget(self.add_new_node_pushButton)

        self.import_nodes_pushButton = QPushButton(self.nodes_list_widget)
        self.import_nodes_pushButton.setObjectName(u"import_nodes_pushButton")

        self.node_list_actions_verticalLayout.addWidget(self.import_nodes_pushButton)

        self.clear_nodes_pushButton = QPushButton(self.nodes_list_widget)
        self.clear_nodes_pushButton.setObjectName(u"clear_nodes_pushButton")

        self.node_list_actions_verticalLayout.addWidget(self.clear_nodes_pushButton)

        self.save_pushButton = QPushButton(self.nodes_list_widget)
        self.save_pushButton.setObjectName(u"save_pushButton")

        self.node_list_actions_verticalLayout.addWidget(self.save_pushButton)


        self.verticalLayout_2.addLayout(self.node_list_actions_verticalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.splitter.addWidget(self.nodes_list_widget)
        self.node_content_placeholder_widget = QWidget(self.splitter)
        self.node_content_placeholder_widget.setObjectName(u"node_content_placeholder_widget")
        sizePolicy.setHeightForWidth(self.node_content_placeholder_widget.sizePolicy().hasHeightForWidth())
        self.node_content_placeholder_widget.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.node_content_placeholder_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter.addWidget(self.node_content_placeholder_widget)

        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1185, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.nodes_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Nodes", None))
        self.add_new_node_pushButton.setText(QCoreApplication.translate("MainWindow", u"add new", None))
        self.import_nodes_pushButton.setText(QCoreApplication.translate("MainWindow", u"import nodes", None))
        self.clear_nodes_pushButton.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.save_pushButton.setText(QCoreApplication.translate("MainWindow", u"save", None))
    # retranslateUi

