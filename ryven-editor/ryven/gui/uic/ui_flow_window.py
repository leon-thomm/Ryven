# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flow_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_FlowWindow(object):
    def setupUi(self, FlowWindow):
        FlowWindow.setObjectName("FlowWindow")
        FlowWindow.resize(1045, 621)
        FlowWindow.setDockNestingEnabled(False)
        FlowWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(FlowWindow)
        self.centralwidget.setObjectName("centralwidget")
        FlowWindow.setCentralWidget(self.centralwidget)
        self.inspector_dock = QtWidgets.QDockWidget(FlowWindow)
        self.inspector_dock.setFloating(False)
        self.inspector_dock.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable|QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.inspector_dock.setObjectName("inspector_dock")
        self.inspectorWidgetContents = QtWidgets.QWidget()
        self.inspectorWidgetContents.setObjectName("inspectorWidgetContents")
        self.inspector_dock.setWidget(self.inspectorWidgetContents)
        FlowWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.inspector_dock)
        self.undo_history_dock = QtWidgets.QDockWidget(FlowWindow)
        self.undo_history_dock.setFloating(False)
        self.undo_history_dock.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable|QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.undo_history_dock.setObjectName("undo_history_dock")
        self.undoHistoryContent = QtWidgets.QWidget()
        self.undoHistoryContent.setObjectName("undoHistoryContent")
        self.undo_history_dock.setWidget(self.undoHistoryContent)
        FlowWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.undo_history_dock)
        self.settings_dock = QtWidgets.QDockWidget(FlowWindow)
        self.settings_dock.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable|QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.settings_dock.setObjectName("settings_dock")
        self.settingsWidgetContents = QtWidgets.QWidget()
        self.settingsWidgetContents.setObjectName("settingsWidgetContents")
        self.settings_dock.setWidget(self.settingsWidgetContents)
        FlowWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.settings_dock)
        self.variables_dock = QtWidgets.QDockWidget(FlowWindow)
        self.variables_dock.setFloating(False)
        self.variables_dock.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable|QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.variables_dock.setObjectName("variables_dock")
        self.variablesWidgetContents = QtWidgets.QWidget()
        self.variablesWidgetContents.setObjectName("variablesWidgetContents")
        self.variables_dock.setWidget(self.variablesWidgetContents)
        FlowWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.variables_dock)
        self.logger_dock = QtWidgets.QDockWidget(FlowWindow)
        self.logger_dock.setObjectName("logger_dock")
        self.loggerWidgetContents = QtWidgets.QWidget()
        self.loggerWidgetContents.setObjectName("loggerWidgetContents")
        self.logs_scrollArea = QtWidgets.QScrollArea(self.loggerWidgetContents)
        self.logs_scrollArea.setGeometry(QtCore.QRect(10, 20, 1, 1))
        self.logs_scrollArea.setWidgetResizable(True)
        self.logs_scrollArea.setObjectName("logs_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 16, 16))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.logs_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.logger_dock.setWidget(self.loggerWidgetContents)
        FlowWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.logger_dock)
        self.source_dock = QtWidgets.QDockWidget(FlowWindow)
        self.source_dock.setObjectName("source_dock")
        self.sourceWidgetContents = QtWidgets.QWidget()
        self.sourceWidgetContents.setObjectName("sourceWidgetContents")
        self.source_dock.setWidget(self.sourceWidgetContents)
        FlowWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.source_dock)
        self.actionxc = QtWidgets.QAction(FlowWindow)
        self.actionxc.setObjectName("actionxc")

        self.retranslateUi(FlowWindow)
        QtCore.QMetaObject.connectSlotsByName(FlowWindow)

    def retranslateUi(self, FlowWindow):
        _translate = QtCore.QCoreApplication.translate
        FlowWindow.setWindowTitle(_translate("FlowWindow", "MainWindow"))
        self.inspector_dock.setWindowTitle(_translate("FlowWindow", "Inspector"))
        self.undo_history_dock.setWindowTitle(_translate("FlowWindow", "Undo History"))
        self.settings_dock.setWindowTitle(_translate("FlowWindow", "Settings"))
        self.variables_dock.setWindowTitle(_translate("FlowWindow", "Variables"))
        self.logger_dock.setWindowTitle(_translate("FlowWindow", "Log"))
        self.source_dock.setWindowTitle(_translate("FlowWindow", "Source Code"))
        self.actionxc.setText(_translate("FlowWindow", "xc"))
