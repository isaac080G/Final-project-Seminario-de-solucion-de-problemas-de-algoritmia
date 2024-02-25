# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1117, 975)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(245, 240, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(250, 247, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(122, 120, 127, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(163, 160, 170, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        self.abrir = QAction(MainWindow)
        self.abrir.setObjectName(u"abrir")
        self.guardar = QAction(MainWindow)
        self.guardar.setObjectName(u"guardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(self.groupBox_7)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(544, 0))
        palette1 = QPalette()
        brush7 = QBrush(QColor(0, 108, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        brush8 = QBrush(QColor(120, 120, 120, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        self.groupBox.setPalette(palette1)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)

        self.verticalLayout.addWidget(self.label_7)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_4 = QFormLayout(self.groupBox_2)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.origenx_spinBox_4 = QSpinBox(self.groupBox_2)
        self.origenx_spinBox_4.setObjectName(u"origenx_spinBox_4")
        self.origenx_spinBox_4.setMaximum(250)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.origenx_spinBox_4)

        self.origenY_spinBox = QSpinBox(self.groupBox_2)
        self.origenY_spinBox.setObjectName(u"origenY_spinBox")
        self.origenY_spinBox.setMaximum(250)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.origenY_spinBox)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout_5 = QFormLayout(self.groupBox_3)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.destino_x_spinBox_2 = QSpinBox(self.groupBox_3)
        self.destino_x_spinBox_2.setObjectName(u"destino_x_spinBox_2")
        self.destino_x_spinBox_2.setMaximum(250)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.destino_x_spinBox_2)

        self.destino_y_spinBox_3 = QSpinBox(self.groupBox_3)
        self.destino_y_spinBox_3.setObjectName(u"destino_y_spinBox_3")
        self.destino_y_spinBox_3.setMaximum(250)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.destino_y_spinBox_3)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.color = QGroupBox(self.groupBox)
        self.color.setObjectName(u"color")
        self.formLayout_2 = QFormLayout(self.color)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_4 = QLabel(self.color)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.color)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.color)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.red_spinBox_4 = QSpinBox(self.color)
        self.red_spinBox_4.setObjectName(u"red_spinBox_4")
        self.red_spinBox_4.setMaximum(250)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.red_spinBox_4)

        self.green_spinBox_5 = QSpinBox(self.color)
        self.green_spinBox_5.setObjectName(u"green_spinBox_5")
        self.green_spinBox_5.setMaximum(250)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.green_spinBox_5)

        self.blue_spinBox_6 = QSpinBox(self.color)
        self.blue_spinBox_6.setObjectName(u"blue_spinBox_6")
        self.blue_spinBox_6.setMaximum(250)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.blue_spinBox_6)


        self.verticalLayout.addWidget(self.color)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.formLayout = QFormLayout(self.groupBox_4)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_2_buscar = QLineEdit(self.groupBox_4)
        self.lineEdit_2_buscar.setObjectName(u"lineEdit_2_buscar")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_2_buscar)

        self.pushButton_buscars = QPushButton(self.groupBox_4)
        self.pushButton_buscars.setObjectName(u"pushButton_buscars")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush9 = QBrush(QColor(85, 255, 0, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.pushButton_buscars.setPalette(palette2)
        self.pushButton_buscars.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.pushButton_buscars)

        self.velocidad_spinBox_3 = QSpinBox(self.groupBox_4)
        self.velocidad_spinBox_3.setObjectName(u"velocidad_spinBox_3")
        self.velocidad_spinBox_3.setMaximum(250)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.velocidad_spinBox_3)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_10)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_agrega_final_2 = QPushButton(self.groupBox_6)
        self.pushButton_agrega_final_2.setObjectName(u"pushButton_agrega_final_2")
        self.pushButton_agrega_final_2.setEnabled(True)
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        self.pushButton_agrega_final_2.setPalette(palette3)
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        self.pushButton_agrega_final_2.setFont(font1)
        self.pushButton_agrega_final_2.setAutoFillBackground(False)
        self.pushButton_agrega_final_2.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pushButton_agrega_final_2)

        self.pushButton_agrega_inicio_2 = QPushButton(self.groupBox_6)
        self.pushButton_agrega_inicio_2.setObjectName(u"pushButton_agrega_inicio_2")
        self.pushButton_agrega_inicio_2.setFont(font)

        self.verticalLayout_3.addWidget(self.pushButton_agrega_inicio_2)

        self.pushButton_3_mostar_2 = QPushButton(self.groupBox_6)
        self.pushButton_3_mostar_2.setObjectName(u"pushButton_3_mostar_2")
        self.pushButton_3_mostar_2.setFont(font)

        self.verticalLayout_3.addWidget(self.pushButton_3_mostar_2)


        self.verticalLayout.addWidget(self.groupBox_6)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.radioButton_ID = QRadioButton(self.groupBox_5)
        self.radioButton_ID.setObjectName(u"radioButton_ID")
        self.radioButton_ID.setFont(font)

        self.verticalLayout_6.addWidget(self.radioButton_ID)

        self.radioButton_2_Distancia = QRadioButton(self.groupBox_5)
        self.radioButton_2_Distancia.setObjectName(u"radioButton_2_Distancia")
        self.radioButton_2_Distancia.setFont(font)

        self.verticalLayout_6.addWidget(self.radioButton_2_Distancia)

        self.radioButton_3_velocidad = QRadioButton(self.groupBox_5)
        self.radioButton_3_velocidad.setObjectName(u"radioButton_3_velocidad")
        self.radioButton_3_velocidad.setFont(font)

        self.verticalLayout_6.addWidget(self.radioButton_3_velocidad)


        self.verticalLayout.addWidget(self.groupBox_5)

        self.pushButton_cercanos = QPushButton(self.groupBox)
        self.pushButton_cercanos.setObjectName(u"pushButton_cercanos")

        self.verticalLayout.addWidget(self.pushButton_cercanos)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.tabWidget = QTabWidget(self.groupBox_7)
        self.tabWidget.setObjectName(u"tabWidget")
        palette4 = QPalette()
        brush10 = QBrush(QColor(255, 0, 0, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        self.tabWidget.setPalette(palette4)
        self.Qplain = QWidget()
        self.Qplain.setObjectName(u"Qplain")
        self.verticalLayout_2 = QVBoxLayout(self.Qplain)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.plainTextEdit = QPlainTextEdit(self.Qplain)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        palette5 = QPalette()
        brush11 = QBrush(QColor(0, 83, 0, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        self.plainTextEdit.setPalette(palette5)

        self.verticalLayout_2.addWidget(self.plainTextEdit)

        self.tabWidget.addTab(self.Qplain, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget = QTableWidget(self.tab)
        self.tableWidget.setObjectName(u"tableWidget")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        brush12 = QBrush(QColor(127, 127, 127, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush12)
        brush13 = QBrush(QColor(170, 170, 170, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.tableWidget.setPalette(palette6)

        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_Dibujar = QPushButton(self.tab_2)
        self.pushButton_Dibujar.setObjectName(u"pushButton_Dibujar")

        self.gridLayout.addWidget(self.pushButton_Dibujar, 1, 1, 1, 1)

        self.pushButton_Limpia = QPushButton(self.tab_2)
        self.pushButton_Limpia.setObjectName(u"pushButton_Limpia")

        self.gridLayout.addWidget(self.pushButton_Limpia, 3, 1, 1, 1)

        self.graphicsView = QGraphicsView(self.tab_2)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 0, 1, 1, 1)

        self.pushButton_dibujar_sinLineas = QPushButton(self.tab_2)
        self.pushButton_dibujar_sinLineas.setObjectName(u"pushButton_dibujar_sinLineas")

        self.gridLayout.addWidget(self.pushButton_dibujar_sinLineas, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.groupBox_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1117, 26))
        self.menuPuntos = QMenu(self.menubar)
        self.menuPuntos.setObjectName(u"menuPuntos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPuntos.menuAction())
        self.menuPuntos.addSeparator()
        self.menuPuntos.addAction(self.abrir)
        self.menuPuntos.addAction(self.guardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.abrir.setText(QCoreApplication.translate("MainWindow", u"abrir", None))
        self.guardar.setText(QCoreApplication.translate("MainWindow", u"guardar", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"particulas", None))
        self.groupBox.setTitle("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"origen", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"destino", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.color.setTitle(QCoreApplication.translate("MainWindow", u"color", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"red", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"green", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"blue", None))
        self.groupBox_4.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"velocidad", None))
        self.pushButton_buscars.setText(QCoreApplication.translate("MainWindow", u"buscar", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"buscar una particula", None))
        self.groupBox_6.setTitle("")
        self.pushButton_agrega_final_2.setText(QCoreApplication.translate("MainWindow", u"agregar final", None))
        self.pushButton_agrega_inicio_2.setText(QCoreApplication.translate("MainWindow", u"agregar inicio", None))
        self.pushButton_3_mostar_2.setText(QCoreApplication.translate("MainWindow", u"mostrar", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"ordenar", None))
        self.radioButton_ID.setText(QCoreApplication.translate("MainWindow", u"ID(ascendente)", None))
        self.radioButton_2_Distancia.setText(QCoreApplication.translate("MainWindow", u"Distancia (descendente)", None))
        self.radioButton_3_velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad (ascendente)", None))
        self.pushButton_cercanos.setText(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Qplain), QCoreApplication.translate("MainWindow", u"Qplain", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab", None))
        self.pushButton_Dibujar.setText(QCoreApplication.translate("MainWindow", u"dibujar", None))
        self.pushButton_Limpia.setText(QCoreApplication.translate("MainWindow", u"limpiar", None))
        self.pushButton_dibujar_sinLineas.setText(QCoreApplication.translate("MainWindow", u"mostrar solo particulas(sin lineas)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Graphics", None))
        self.menuPuntos.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
    # retranslateUi

