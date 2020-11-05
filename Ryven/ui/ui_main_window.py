# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
        MainWindow.resize(1368, 908)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionImport_Nodes = QAction(MainWindow)
        self.actionImport_Nodes.setObjectName(u"actionImport_Nodes")
        self.actionSave_Project = QAction(MainWindow)
        self.actionSave_Project.setObjectName(u"actionSave_Project")
        self.actionDesignDark_Std = QAction(MainWindow)
        self.actionDesignDark_Std.setObjectName(u"actionDesignDark_Std")
        self.actionDesignDark_Tron = QAction(MainWindow)
        self.actionDesignDark_Tron.setObjectName(u"actionDesignDark_Tron")
        self.actionEnableDebugging = QAction(MainWindow)
        self.actionEnableDebugging.setObjectName(u"actionEnableDebugging")
        self.actionDisableDebugging = QAction(MainWindow)
        self.actionDisableDebugging.setObjectName(u"actionDisableDebugging")
        self.actionSave_Pic_Viewport = QAction(MainWindow)
        self.actionSave_Pic_Viewport.setObjectName(u"actionSave_Pic_Viewport")
        self.actionSave_Pic_Whole_Scene_scaled = QAction(MainWindow)
        self.actionSave_Pic_Whole_Scene_scaled.setObjectName(u"actionSave_Pic_Whole_Scene_scaled")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.gridLayout_2 = QGridLayout(self.centralWidget)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter = QSplitter(self.centralWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.scripts_groupBox = QGroupBox(self.splitter)
        self.scripts_groupBox.setObjectName(u"scripts_groupBox")
        self.gridLayout_3 = QGridLayout(self.scripts_groupBox)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scripts_console_splitter = QSplitter(self.scripts_groupBox)
        self.scripts_console_splitter.setObjectName(u"scripts_console_splitter")
        self.scripts_console_splitter.setOrientation(Qt.Vertical)
        self.widget = QWidget(self.scripts_console_splitter)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scripts_scrollArea = QScrollArea(self.widget)
        self.scripts_scrollArea.setObjectName(u"scripts_scrollArea")
        self.scripts_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 935, 727))
        self.scripts_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scripts_scrollArea, 0, 0, 1, 1)

        self.new_script_name_lineEdit = QLineEdit(self.widget)
        self.new_script_name_lineEdit.setObjectName(u"new_script_name_lineEdit")

        self.gridLayout.addWidget(self.new_script_name_lineEdit, 1, 0, 1, 1)

        self.add_new_script_pushButton = QPushButton(self.widget)
        self.add_new_script_pushButton.setObjectName(u"add_new_script_pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_new_script_pushButton.sizePolicy().hasHeightForWidth())
        self.add_new_script_pushButton.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.add_new_script_pushButton, 2, 0, 1, 1)

        self.scripts_console_splitter.addWidget(self.widget)

        self.gridLayout_3.addWidget(self.scripts_console_splitter, 0, 0, 1, 1)

        self.splitter.addWidget(self.scripts_groupBox)
        self.scripts_tab_widget = QTabWidget(self.splitter)
        self.scripts_tab_widget.setObjectName(u"scripts_tab_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scripts_tab_widget.sizePolicy().hasHeightForWidth())
        self.scripts_tab_widget.setSizePolicy(sizePolicy2)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.scripts_tab_widget.addTab(self.tab, "")
        self.splitter.addWidget(self.scripts_tab_widget)

        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1368, 26))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menuBar)
        self.menuView.setObjectName(u"menuView")
        self.menuFlow_Design_Style = QMenu(self.menuView)
        self.menuFlow_Design_Style.setObjectName(u"menuFlow_Design_Style")
        self.menuSave_Picture = QMenu(self.menuView)
        self.menuSave_Picture.setObjectName(u"menuSave_Picture")
        self.menuDebugging = QMenu(self.menuBar)
        self.menuDebugging.setObjectName(u"menuDebugging")
        self.menuDebugging_Messages = QMenu(self.menuDebugging)
        self.menuDebugging_Messages.setObjectName(u"menuDebugging_Messages")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuDebugging.menuAction())
        self.menuFile.addAction(self.actionImport_Nodes)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuView.addSeparator()
        self.menuView.addAction(self.menuFlow_Design_Style.menuAction())
        self.menuView.addAction(self.menuSave_Picture.menuAction())
        self.menuSave_Picture.addAction(self.actionSave_Pic_Viewport)
        self.menuSave_Picture.addAction(self.actionSave_Pic_Whole_Scene_scaled)
        self.menuDebugging.addAction(self.menuDebugging_Messages.menuAction())
        self.menuDebugging_Messages.addAction(self.actionEnableDebugging)
        self.menuDebugging_Messages.addAction(self.actionDisableDebugging)

        self.retranslateUi(MainWindow)

        self.scripts_tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionImport_Nodes.setText(QCoreApplication.translate("MainWindow", u"Import Nodes", None))
        self.actionSave_Project.setText(QCoreApplication.translate("MainWindow", u"Save Project", None))
        self.actionDesignDark_Std.setText(QCoreApplication.translate("MainWindow", u"Dark Std", None))
        self.actionDesignDark_Tron.setText(QCoreApplication.translate("MainWindow", u"Dark Tron", None))
        self.actionEnableDebugging.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.actionDisableDebugging.setText(QCoreApplication.translate("MainWindow", u"Disable", None))
        self.actionSave_Pic_Viewport.setText(QCoreApplication.translate("MainWindow", u"Save Pic - Viewport", None))
#if QT_CONFIG(tooltip)
        self.actionSave_Pic_Viewport.setToolTip(QCoreApplication.translate("MainWindow", u"Save a picture of the current scene's viewport.\n"
"This will save exactly what you see in the same resolution.", None))
#endif // QT_CONFIG(tooltip)
        self.actionSave_Pic_Whole_Scene_scaled.setText(QCoreApplication.translate("MainWindow", u"Save Pic - Whole Scene (scaled)", None))
#if QT_CONFIG(tooltip)
        self.actionSave_Pic_Whole_Scene_scaled.setToolTip(QCoreApplication.translate("MainWindow", u"Saves a picture of the whole current scene. \n"
"The more you zoomed in, the sharper the picture.\n"
"This will take a few seconds.", None))
#endif // QT_CONFIG(tooltip)
        self.scripts_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Scripts", None))
        self.new_script_name_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"script title", None))
        self.add_new_script_pushButton.setText(QCoreApplication.translate("MainWindow", u"add new", None))
        self.scripts_tab_widget.setTabText(self.scripts_tab_widget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Main", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuFlow_Design_Style.setTitle(QCoreApplication.translate("MainWindow", u"Flow Theme", None))
        self.menuSave_Picture.setTitle(QCoreApplication.translate("MainWindow", u"Save Picture", None))
        self.menuDebugging.setTitle(QCoreApplication.translate("MainWindow", u"Debugging", None))
        self.menuDebugging_Messages.setTitle(QCoreApplication.translate("MainWindow", u"Debugging Messages", None))
    # retranslateUi

