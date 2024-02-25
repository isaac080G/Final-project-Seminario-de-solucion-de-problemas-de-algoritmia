# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SecondWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        if not SecondWindow.objectName():
            SecondWindow.setObjectName(u"SecondWindow")
        SecondWindow.resize(1121, 843)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        brush2 = QBrush(QColor(245, 240, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        SecondWindow.setPalette(palette)
        self.centralwidget = QWidget(SecondWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 0, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_2 = QGridLayout(self.groupBox_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)

        self.lineEdit_3_destino_x = QLineEdit(self.groupBox_5)
        self.lineEdit_3_destino_x.setObjectName(u"lineEdit_3_destino_x")

        self.gridLayout_2.addWidget(self.lineEdit_3_destino_x, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.lineEdit_4destino_Y = QLineEdit(self.groupBox_5)
        self.lineEdit_4destino_Y.setObjectName(u"lineEdit_4destino_Y")

        self.gridLayout_2.addWidget(self.lineEdit_4destino_Y, 0, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_5)

        self.plainTextEdit = QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.plainTextEdit)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_prim = QPushButton(self.groupBox_2)
        self.pushButton_prim.setObjectName(u"pushButton_prim")

        self.verticalLayout.addWidget(self.pushButton_prim)

        self.pushButton_2_kruskal = QPushButton(self.groupBox_2)
        self.pushButton_2_kruskal.setObjectName(u"pushButton_2_kruskal")

        self.verticalLayout.addWidget(self.pushButton_2_kruskal)

        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.plainTextEdit_2 = QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit_2)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.graphicsView_2 = QGraphicsView(self.groupBox_4)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.verticalLayout_2.addWidget(self.graphicsView_2)

        self.pushButton_grafos = QPushButton(self.groupBox_4)
        self.pushButton_grafos.setObjectName(u"pushButton_grafos")

        self.verticalLayout_2.addWidget(self.pushButton_grafos)


        self.horizontalLayout.addWidget(self.groupBox_4)

        SecondWindow.setCentralWidget(self.centralwidget)
        self.groupBox_4.raise_()
        self.groupBox.raise_()
        self.statusbar = QStatusBar(SecondWindow)
        self.statusbar.setObjectName(u"statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)

        QMetaObject.connectSlotsByName(SecondWindow)
    # setupUi

    def retranslateUi(self, SecondWindow):
        SecondWindow.setWindowTitle(QCoreApplication.translate("SecondWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.groupBox_3.setTitle(QCoreApplication.translate("SecondWindow", u"particula inicio", None))
        self.label.setText(QCoreApplication.translate("SecondWindow", u"X:", None))
        self.label_2.setText(QCoreApplication.translate("SecondWindow", u"Y:", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("SecondWindow", u"particula destino", None))
        self.label_4.setText(QCoreApplication.translate("SecondWindow", u"Y:", None))
        self.label_3.setText(QCoreApplication.translate("SecondWindow", u"X:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SecondWindow", u"Algoritmos", None))
        self.pushButton_prim.setText(QCoreApplication.translate("SecondWindow", u"dijkstra", None))
        self.pushButton_2_kruskal.setText(QCoreApplication.translate("SecondWindow", u"kruskal", None))
        self.pushButton_3.setText(QCoreApplication.translate("SecondWindow", u"e", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("SecondWindow", u"Info:", None))
        self.groupBox_4.setTitle("")
        self.pushButton_grafos.setText(QCoreApplication.translate("SecondWindow", u"dibujar grafo", None))
    # retranslateUi

