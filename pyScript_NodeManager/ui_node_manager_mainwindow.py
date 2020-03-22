# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'node_manager_mainwindow.ui',
# licensing of 'node_manager_mainwindow.ui' applies.
#
# Created: Sun Jan 12 15:51:03 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1185, 778)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.nodes_list_widget = QtWidgets.QWidget(self.splitter)
        self.nodes_list_widget.setObjectName("nodes_list_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.nodes_list_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.nodes_groupBox = QtWidgets.QGroupBox(self.nodes_list_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodes_groupBox.sizePolicy().hasHeightForWidth())
        self.nodes_groupBox.setSizePolicy(sizePolicy)
        self.nodes_groupBox.setObjectName("nodes_groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.nodes_groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nodes_scrollArea = QtWidgets.QScrollArea(self.nodes_groupBox)
        self.nodes_scrollArea.setWidgetResizable(True)
        self.nodes_scrollArea.setObjectName("nodes_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 170, 572))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.nodes_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.nodes_scrollArea)
        self.verticalLayout_2.addWidget(self.nodes_groupBox)
        self.node_list_actions_verticalLayout = QtWidgets.QVBoxLayout()
        self.node_list_actions_verticalLayout.setObjectName("node_list_actions_verticalLayout")
        self.add_new_node_pushButton = QtWidgets.QPushButton(self.nodes_list_widget)
        self.add_new_node_pushButton.setObjectName("add_new_node_pushButton")
        self.node_list_actions_verticalLayout.addWidget(self.add_new_node_pushButton)
        self.import_nodes_pushButton = QtWidgets.QPushButton(self.nodes_list_widget)
        self.import_nodes_pushButton.setObjectName("import_nodes_pushButton")
        self.node_list_actions_verticalLayout.addWidget(self.import_nodes_pushButton)
        self.save_pushButton = QtWidgets.QPushButton(self.nodes_list_widget)
        self.save_pushButton.setObjectName("save_pushButton")
        self.node_list_actions_verticalLayout.addWidget(self.save_pushButton)
        self.verticalLayout_2.addLayout(self.node_list_actions_verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.node_content_placeholder_widget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.node_content_placeholder_widget.sizePolicy().hasHeightForWidth())
        self.node_content_placeholder_widget.setSizePolicy(sizePolicy)
        self.node_content_placeholder_widget.setObjectName("node_content_placeholder_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.node_content_placeholder_widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1185, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.nodes_groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Nodes", None, -1))
        self.add_new_node_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "add new", None, -1))
        self.import_nodes_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "import nodes", None, -1))
        self.save_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "save", None, -1))

