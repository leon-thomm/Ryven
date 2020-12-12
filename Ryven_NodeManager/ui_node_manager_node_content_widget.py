# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'node_manager_node_content_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(915, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.top_horizontalLayout = QHBoxLayout()
        self.top_horizontalLayout.setObjectName(u"top_horizontalLayout")
        self.nodeTitle_gridLayout = QGridLayout()
        self.nodeTitle_gridLayout.setObjectName(u"nodeTitle_gridLayout")
        self.title_lineEdit = QLineEdit(Form)
        self.title_lineEdit.setObjectName(u"title_lineEdit")

        self.nodeTitle_gridLayout.addWidget(self.title_lineEdit, 0, 0, 1, 1)

        self.name_problems_detected_label = QLabel(Form)
        self.name_problems_detected_label.setObjectName(u"name_problems_detected_label")

        self.nodeTitle_gridLayout.addWidget(self.name_problems_detected_label, 0, 1, 1, 1)

        self.internal_name_lineEdit = QLineEdit(Form)
        self.internal_name_lineEdit.setObjectName(u"internal_name_lineEdit")
        self.internal_name_lineEdit.setEnabled(False)

        self.nodeTitle_gridLayout.addWidget(self.internal_name_lineEdit, 1, 0, 1, 1)

        self.auto_generate_internal_name_checkBox = QCheckBox(Form)
        self.auto_generate_internal_name_checkBox.setObjectName(u"auto_generate_internal_name_checkBox")
        self.auto_generate_internal_name_checkBox.setChecked(True)

        self.nodeTitle_gridLayout.addWidget(self.auto_generate_internal_name_checkBox, 1, 1, 1, 1)


        self.top_horizontalLayout.addLayout(self.nodeTitle_gridLayout)

        self.edit_node_metacode_placeholderButton = QPushButton(Form)
        self.edit_node_metacode_placeholderButton.setObjectName(u"edit_node_metacode_placeholderButton")

        self.top_horizontalLayout.addWidget(self.edit_node_metacode_placeholderButton)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.type_comboBox = QComboBox(Form)
        self.type_comboBox.addItem("")
        self.type_comboBox.addItem("")
        self.type_comboBox.setObjectName(u"type_comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.type_comboBox.sizePolicy().hasHeightForWidth())
        self.type_comboBox.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.type_comboBox)

        self.custom_type_lineEdit = QLineEdit(Form)
        self.custom_type_lineEdit.setObjectName(u"custom_type_lineEdit")
        self.custom_type_lineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.custom_type_lineEdit.sizePolicy().hasHeightForWidth())
        self.custom_type_lineEdit.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.custom_type_lineEdit)


        self.top_horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.top_horizontalLayout, 0, 0, 1, 1)

        self.splitter_2 = QSplitter(Form)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.description_textEdit = QTextEdit(self.splitter_2)
        self.description_textEdit.setObjectName(u"description_textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.description_textEdit.sizePolicy().hasHeightForWidth())
        self.description_textEdit.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamily(u"MS Reference Sans Serif")
        font.setPointSize(11)
        self.description_textEdit.setFont(font)
        self.splitter_2.addWidget(self.description_textEdit)
        self.widget = QWidget(self.splitter_2)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.input_widgets_groupBox = QGroupBox(self.widget)
        self.input_widgets_groupBox.setObjectName(u"input_widgets_groupBox")
        self.gridLayout_4 = QGridLayout(self.input_widgets_groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.input_widgets_scrollArea = QScrollArea(self.input_widgets_groupBox)
        self.input_widgets_scrollArea.setObjectName(u"input_widgets_scrollArea")
        self.input_widgets_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 438, 124))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.input_widgets_scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_4.addWidget(self.input_widgets_scrollArea, 0, 0, 1, 1)

        self.add_new_input_widget_pushButton = QPushButton(self.input_widgets_groupBox)
        self.add_new_input_widget_pushButton.setObjectName(u"add_new_input_widget_pushButton")

        self.gridLayout_4.addWidget(self.add_new_input_widget_pushButton, 1, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.input_widgets_groupBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.main_widget_checkBox = QCheckBox(self.groupBox)
        self.main_widget_checkBox.setObjectName(u"main_widget_checkBox")
        self.main_widget_checkBox.setChecked(False)

        self.horizontalLayout_4.addWidget(self.main_widget_checkBox)

        self.main_widget_position_widget = QWidget(self.groupBox)
        self.main_widget_position_widget.setObjectName(u"main_widget_position_widget")
        self.main_widget_position_widget.setEnabled(True)
        self.verticalLayout_12 = QVBoxLayout(self.main_widget_position_widget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.main_widget_under_ports_radioButton = QRadioButton(self.main_widget_position_widget)
        self.main_widget_under_ports_radioButton.setObjectName(u"main_widget_under_ports_radioButton")
        self.main_widget_under_ports_radioButton.setChecked(True)

        self.verticalLayout_12.addWidget(self.main_widget_under_ports_radioButton)

        self.main_widget_between_ports_radioButton = QRadioButton(self.main_widget_position_widget)
        self.main_widget_between_ports_radioButton.setObjectName(u"main_widget_between_ports_radioButton")

        self.verticalLayout_12.addWidget(self.main_widget_between_ports_radioButton)

        self.edit_main_widget_metacode_placeholderButton = QPushButton(self.main_widget_position_widget)
        self.edit_main_widget_metacode_placeholderButton.setObjectName(u"edit_main_widget_metacode_placeholderButton")

        self.verticalLayout_12.addWidget(self.edit_main_widget_metacode_placeholderButton)


        self.horizontalLayout_4.addWidget(self.main_widget_position_widget)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.design_style_groupBox = QGroupBox(self.widget)
        self.design_style_groupBox.setObjectName(u"design_style_groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.design_style_groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.design_style_extended_radioButton = QRadioButton(self.design_style_groupBox)
        self.design_style_extended_radioButton.setObjectName(u"design_style_extended_radioButton")
        self.design_style_extended_radioButton.setChecked(True)

        self.verticalLayout_2.addWidget(self.design_style_extended_radioButton)

        self.design_style_minimalistic_radioButton = QRadioButton(self.design_style_groupBox)
        self.design_style_minimalistic_radioButton.setObjectName(u"design_style_minimalistic_radioButton")

        self.verticalLayout_2.addWidget(self.design_style_minimalistic_radioButton)


        self.verticalLayout_10.addWidget(self.design_style_groupBox)

        self.node_color_groupBox = QGroupBox(self.widget)
        self.node_color_groupBox.setObjectName(u"node_color_groupBox")
        self.verticalLayout_13 = QVBoxLayout(self.node_color_groupBox)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.select_color_pushButton = QPushButton(self.node_color_groupBox)
        self.select_color_pushButton.setObjectName(u"select_color_pushButton")

        self.verticalLayout_13.addWidget(self.select_color_pushButton)

        self.color_sample_pushButton = QPushButton(self.node_color_groupBox)
        self.color_sample_pushButton.setObjectName(u"color_sample_pushButton")

        self.verticalLayout_13.addWidget(self.color_sample_pushButton)


        self.verticalLayout_10.addWidget(self.node_color_groupBox)


        self.horizontalLayout_3.addLayout(self.verticalLayout_10)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.splitter_2.addWidget(self.widget)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        sizePolicy2.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy2)
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.inputs_verticalLayout = QVBoxLayout(self.layoutWidget)
        self.inputs_verticalLayout.setObjectName(u"inputs_verticalLayout")
        self.inputs_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.inputs_groupBox = QGroupBox(self.layoutWidget)
        self.inputs_groupBox.setObjectName(u"inputs_groupBox")
        self.verticalLayout_8 = QVBoxLayout(self.inputs_groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.inputs_scrollArea = QScrollArea(self.inputs_groupBox)
        self.inputs_scrollArea.setObjectName(u"inputs_scrollArea")
        self.inputs_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 416, 159))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.inputs_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.inputs_scrollArea)

        self.add_new_input_pushButton = QPushButton(self.inputs_groupBox)
        self.add_new_input_pushButton.setObjectName(u"add_new_input_pushButton")

        self.verticalLayout_8.addWidget(self.add_new_input_pushButton)


        self.inputs_verticalLayout.addWidget(self.inputs_groupBox)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.outputs_verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.outputs_verticalLayout.setObjectName(u"outputs_verticalLayout")
        self.outputs_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.outputs_groupBox = QGroupBox(self.layoutWidget1)
        self.outputs_groupBox.setObjectName(u"outputs_groupBox")
        self.verticalLayout_7 = QVBoxLayout(self.outputs_groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.outputs_scrollArea = QScrollArea(self.outputs_groupBox)
        self.outputs_scrollArea.setObjectName(u"outputs_scrollArea")
        self.outputs_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 415, 159))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.outputs_scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.outputs_scrollArea)

        self.add_new_output_pushButton = QPushButton(self.outputs_groupBox)
        self.add_new_output_pushButton.setObjectName(u"add_new_output_pushButton")

        self.verticalLayout_7.addWidget(self.add_new_output_pushButton)


        self.outputs_verticalLayout.addWidget(self.outputs_groupBox)

        self.splitter.addWidget(self.layoutWidget1)
        self.splitter_2.addWidget(self.splitter)

        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title_lineEdit.setText(QCoreApplication.translate("Form", u"new node", None))
        self.title_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Title", None))
        self.name_problems_detected_label.setText(QCoreApplication.translate("Form", u"Name Problems Detected: None", None))
        self.internal_name_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Internal Name", None))
        self.auto_generate_internal_name_checkBox.setText(QCoreApplication.translate("Form", u"auto generate internal name", None))
        self.edit_node_metacode_placeholderButton.setText(QCoreApplication.translate("Form", u"(edit src placeholder)", None))
        self.type_comboBox.setItemText(0, QCoreApplication.translate("Form", u"custom", None))
        self.type_comboBox.setItemText(1, QCoreApplication.translate("Form", u"control structure", None))

        self.type_comboBox.setCurrentText(QCoreApplication.translate("Form", u"custom", None))
        self.custom_type_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Custom Type", None))
        self.description_textEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Node Description", None))
        self.input_widgets_groupBox.setTitle(QCoreApplication.translate("Form", u"Input Widgets", None))
        self.add_new_input_widget_pushButton.setText(QCoreApplication.translate("Form", u"add new", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Main Widget", None))
        self.main_widget_checkBox.setText(QCoreApplication.translate("Form", u"None", None))
        self.main_widget_under_ports_radioButton.setText(QCoreApplication.translate("Form", u"main widget under ports", None))
        self.main_widget_between_ports_radioButton.setText(QCoreApplication.translate("Form", u"main widget between ports", None))
        self.edit_main_widget_metacode_placeholderButton.setText(QCoreApplication.translate("Form", u"edit metacode", None))
        self.design_style_groupBox.setTitle(QCoreApplication.translate("Form", u"Design Style", None))
        self.design_style_extended_radioButton.setText(QCoreApplication.translate("Form", u"Extended", None))
        self.design_style_minimalistic_radioButton.setText(QCoreApplication.translate("Form", u"Minimalistic", None))
        self.node_color_groupBox.setTitle(QCoreApplication.translate("Form", u"Node Color", None))
        self.select_color_pushButton.setText(QCoreApplication.translate("Form", u"select color", None))
        self.color_sample_pushButton.setText("")
        self.inputs_groupBox.setTitle(QCoreApplication.translate("Form", u"Inputs", None))
        self.add_new_input_pushButton.setText(QCoreApplication.translate("Form", u"add new", None))
        self.outputs_groupBox.setTitle(QCoreApplication.translate("Form", u"Outputs", None))
        self.add_new_output_pushButton.setText(QCoreApplication.translate("Form", u"add new", None))
    # retranslateUi
