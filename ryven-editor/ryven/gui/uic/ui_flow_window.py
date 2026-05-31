# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flow_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from qtpy.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from qtpy.QtWidgets import (QApplication, QDockWidget, QMainWindow, QScrollArea,
    QSizePolicy, QWidget)

class Ui_FlowWindow(object):
    def setupUi(self, FlowWindow):
        if not FlowWindow.objectName():
            FlowWindow.setObjectName(u"FlowWindow")
        FlowWindow.resize(1045, 621)
        FlowWindow.setDockNestingEnabled(False)
        FlowWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.actionxc = QAction(FlowWindow)
        self.actionxc.setObjectName(u"actionxc")
        self.centralwidget = QWidget(FlowWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        FlowWindow.setCentralWidget(self.centralwidget)
        self.inspector_dock = QDockWidget(FlowWindow)
        self.inspector_dock.setObjectName(u"inspector_dock")
        self.inspector_dock.setFloating(False)
        self.inspector_dock.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.inspectorWidgetContents = QWidget()
        self.inspectorWidgetContents.setObjectName(u"inspectorWidgetContents")
        self.inspector_dock.setWidget(self.inspectorWidgetContents)
        FlowWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.inspector_dock)
        self.undo_history_dock = QDockWidget(FlowWindow)
        self.undo_history_dock.setObjectName(u"undo_history_dock")
        self.undo_history_dock.setFloating(False)
        self.undo_history_dock.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.undoHistoryContent = QWidget()
        self.undoHistoryContent.setObjectName(u"undoHistoryContent")
        self.undo_history_dock.setWidget(self.undoHistoryContent)
        FlowWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.undo_history_dock)
        self.settings_dock = QDockWidget(FlowWindow)
        self.settings_dock.setObjectName(u"settings_dock")
        self.settings_dock.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.settingsWidgetContents = QWidget()
        self.settingsWidgetContents.setObjectName(u"settingsWidgetContents")
        self.settings_dock.setWidget(self.settingsWidgetContents)
        FlowWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.settings_dock)
        self.variables_dock = QDockWidget(FlowWindow)
        self.variables_dock.setObjectName(u"variables_dock")
        self.variables_dock.setFloating(False)
        self.variables_dock.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.variablesWidgetContents = QWidget()
        self.variablesWidgetContents.setObjectName(u"variablesWidgetContents")
        self.variables_dock.setWidget(self.variablesWidgetContents)
        FlowWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.variables_dock)
        self.logger_dock = QDockWidget(FlowWindow)
        self.logger_dock.setObjectName(u"logger_dock")
        self.loggerWidgetContents = QWidget()
        self.loggerWidgetContents.setObjectName(u"loggerWidgetContents")
        self.logs_scrollArea = QScrollArea(self.loggerWidgetContents)
        self.logs_scrollArea.setObjectName(u"logs_scrollArea")
        self.logs_scrollArea.setGeometry(QRect(10, 20, 1, 1))
        self.logs_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 16, 16))
        self.logs_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.logger_dock.setWidget(self.loggerWidgetContents)
        FlowWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.logger_dock)
        self.source_dock = QDockWidget(FlowWindow)
        self.source_dock.setObjectName(u"source_dock")
        self.sourceWidgetContents = QWidget()
        self.sourceWidgetContents.setObjectName(u"sourceWidgetContents")
        self.source_dock.setWidget(self.sourceWidgetContents)
        FlowWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.source_dock)

        self.retranslateUi(FlowWindow)

        QMetaObject.connectSlotsByName(FlowWindow)
    # setupUi

    def retranslateUi(self, FlowWindow):
        FlowWindow.setWindowTitle(QCoreApplication.translate("FlowWindow", u"MainWindow", None))
        self.actionxc.setText(QCoreApplication.translate("FlowWindow", u"xc", None))
        self.inspector_dock.setWindowTitle(QCoreApplication.translate("FlowWindow", u"Inspector", None))
        self.undo_history_dock.setWindowTitle(QCoreApplication.translate("FlowWindow", u"Undo History", None))
        self.settings_dock.setWindowTitle(QCoreApplication.translate("FlowWindow", u"Settings", None))
        self.variables_dock.setWindowTitle(QCoreApplication.translate("FlowWindow", u"Variables", None))
        self.logger_dock.setWindowTitle(QCoreApplication.translate("FlowWindow", u"Log", None))
        self.source_dock.setWindowTitle(QCoreApplication.translate("FlowWindow", u"Source Code", None))
    # retranslateUi

