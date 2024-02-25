from PySide2.QtWidgets import QMainWindow, QGraphicsScene, QMessageBox, QFileDialog, QTableWidget, QTableWidgetItem, QGraphicsView, QRadioButton, QPushButton, QDialog
from PySide2.QtGui import QPalette, QColor
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from random import randint
from lista import lista
from particulas import particulas
from pprint import pprint
from SecondWindow import SecondWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene()
        self.lista = lista()

        self.ui.abrir.triggered.connect(self.action_Abrir_Archivo)
        self.ui.guardar.triggered.connect(self.action_Guardar_Archivo)
        # self.ui.agregar_final_pushButton.clicked.connect(self.agregar_final)
        # self.ui.mostrar.clicked.connect(self.mostrar)
        # self.ui.agregar_inicio_pushButton.clicked.connect(self.agregar_inicio)
        self.ui.pushButton_buscars.clicked.connect(self.buscar_id)
        self.ui.pushButton_Dibujar.clicked.connect(self.dibujar)
        self.ui.pushButton_Limpia.clicked.connect(self.limpiar)
        self.ui.graphicsView.setScene(self.scene)
        self.ui.pushButton_agrega_final_2.clicked.connect(self.agregar_final)
        self.ui.pushButton_agrega_inicio_2.clicked.connect(self.agregar_inicio)
        self.ui.pushButton_3_mostar_2.clicked.connect(self.mostrar_Qplain)
        # self.ui.pushButton_ordenar.clicked.connect(self.ordenar)
        self.ui.pushButton_dibujar_sinLineas.clicked.connect(
            self.dibujarSinlineas)
        self.ui.pushButton_cercanos.clicked.connect(self.openSecondWindow)

        self.ui.radioButton_ID.toggled.connect(self.ordenar)
        self.ui.radioButton_2_Distancia.toggled.connect(self.ordenar)
        self.ui.radioButton_3_velocidad.toggled.connect(self.ordenar)

        # colores

    @Slot()
    def agregar_final(self):
        ID = self.ui.lineEdit.text()
        origen_x = self.ui.origenx_spinBox_4.value()
        origen_y = self.ui.origenY_spinBox.value()
        destino_x = self.ui.destino_x_spinBox_2.value()
        destino_y = self.ui.destino_y_spinBox_3.value()
        velocidad = self.ui.velocidad_spinBox_3.value()
        red = self.ui.red_spinBox_4.value()
        green = self.ui.green_spinBox_5.value()
        blue = self.ui.blue_spinBox_6.value()

        p = particulas(ID, origen_x, origen_y, destino_x,
                       destino_y, velocidad, red, green, blue)
        self.lista.agregar_final(p)

    def agregar_inicio(self):
        ID = int(self.ui.lineEdit.text())
        origen_x = self.ui.origenx_spinBox_4.value()
        origen_y = self.ui.origenY_spinBox.value()
        destino_x = self.ui.destino_x_spinBox_2.value()
        destino_y = self.ui.destino_y_spinBox_3.value()
        velocidad = self.ui.velocidad_spinBox_3.value()
        red = self.ui.red_spinBox_4.value()
        green = self.ui.green_spinBox_5.value()
        blue = self.ui.blue_spinBox_6.value()

        p = particulas(ID, origen_x, origen_y, destino_x,
                       destino_y, velocidad, red, green, blue)
        self.lista.agregar_inicio(p)

    def mostrar(self):
        self.ui.tableWidget.setColumnCount(10)
        headers = ["ID", "origen x", "origen y", "destino x",
                   "destino y", "velocidad", "red", "green", "blue", "distancia"]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        self.ui.tableWidget.setRowCount(len(self.lista))

        row = 0
        for particula in self.lista:
            id_widget = QTableWidgetItem(str(particula.id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y__widget = QTableWidgetItem(str(particula.origen_y))
            destino_x__widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velicidad__widget = QTableWidgetItem(str(particula.velocidad))
            red__widget = QTableWidgetItem(str(particula.red))
            green__widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia_euclidiana(
                particula.origen_x, particula.origen_y, particula.destino_x, particula.destino_y)))

            self.ui.tableWidget.setItem(row, 0, id_widget)
            self.ui.tableWidget.setItem(row, 1, origen_x_widget)
            self.ui.tableWidget.setItem(row, 2, origen_y__widget)
            self.ui.tableWidget.setItem(row, 3, destino_x__widget)
            self.ui.tableWidget.setItem(row, 4, destino_y_widget)
            self.ui.tableWidget.setItem(row, 5, velicidad__widget)
            self.ui.tableWidget.setItem(row, 6, red__widget)
            self.ui.tableWidget.setItem(row, 7, green__widget)
            self.ui.tableWidget.setItem(row, 8, blue_widget)
            self.ui.tableWidget.setItem(row, 9, distancia_widget)
            row += 1

    def action_Guardar_Archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'guardar Archivo ',
            '.',
            'json(*.json)'
        )[0]
        # print(ubicacion)
        self.lista.guardar(ubicacion)
        if self.lista.guardar(ubicacion):
            QMessageBox.information(
                self,
                "exito",
                "se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "error",
                "no se pudo crear el archivo" + ubicacion
            )

    def action_Abrir_Archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'abrir Archivo ',
            '.',
            'json(*.json)'
        )[0]
        # self.aereopuerto.abrir(ubicacion)
        if self.lista.abrir(ubicacion):
            QMessageBox.information(
                self,
                "exito",
                "se pudo abrir el archivo" + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "error",
                "no se pudo abrir el archivo" + ubicacion
            )

    def buscar_id(self):

        id = self.ui.lineEdit_2_buscar.text()

        encontrado = False

        for particula in self.lista:
            if particula is None:
                continue
            if int(id) == particula.id:
                self.ui.tableWidget.clear()
                self.ui.tableWidget.setColumnCount(10)
                self.ui.tableWidget.setRowCount(1)
                headers = ["ID", "origen x", "origen y", "destino x",
                           "destino y", "velocidad", "red", "green", "blue", "distancia"]
                self.ui.tableWidget.setHorizontalHeaderLabels(headers)

                id_widget = QTableWidgetItem(str(particula.id))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y__widget = QTableWidgetItem(str(particula.origen_y))
                destino_x__widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velicidad__widget = QTableWidgetItem(str(particula.velocidad))
                red__widget = QTableWidgetItem(str(particula.red))
                green__widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia_euclidiana(
                    particula.origen_x, particula.origen_y, particula.destino_x, particula.destino_y)))

                self.ui.tableWidget.setItem(0, 0, id_widget)
                self.ui.tableWidget.setItem(0, 1, origen_x_widget)
                self.ui.tableWidget.setItem(0, 2, origen_y__widget)
                self.ui.tableWidget.setItem(0, 3, destino_x__widget)
                self.ui.tableWidget.setItem(0, 4, destino_y_widget)
                self.ui.tableWidget.setItem(0, 5, velicidad__widget)
                self.ui.tableWidget.setItem(0, 6, red__widget)
                self.ui.tableWidget.setItem(0, 7, green__widget)
                self.ui.tableWidget.setItem(0, 8, blue_widget)
                self.ui.tableWidget.setItem(0, 9, distancia_widget)

                self.ui.plainTextEdit.insertPlainText(str(particula))
                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self, "Atencion", "la particula con el identificador " + str(id) + " no fue encontrado")

    def dibujar(self):
        pprint(self.lista)
        for particula in self.lista:
            pen = QPen()
            pen.setWidth(2)
            R = particula.red
            G = particula.green
            B = particula.blue
            color = QColor(R, G, B)
            pen.setColor(color)

            x_origen = particula.origen_x
            y_origen = particula.origen_y
            self.scene.addEllipse(x_origen, y_origen, 6, 6)
            x_destino = particula.destino_x
            y_destino = particula.destino_y
            self.scene.addEllipse(x_destino, y_destino, 6, 6)
            self.scene.addLine(x_origen+3, y_origen+3,
                               x_destino+3, y_destino+3, pen)

    def limpiar(self):
        self.scene.clear()

    def wheelEvent(self, event):
        print(event.delta())
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    def mostrar_Qplain(self):
        self.lista.mostrar()
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.lista))
        self.mostrar()

    def ordenar(self):
        self.ui.plainTextEdit.clear()
        self.ui.tableWidget.clear()
        if self.ui.radioButton_ID.isChecked():
            self.lista.ordenar_id()

        elif self.ui.radioButton_2_Distancia.isChecked():
            self.lista.ordenar_distancia()
        elif self.ui.radioButton_3_velocidad.isChecked():
            self.lista.ordenar_velocidad()
        else:
            QMessageBox.information(
                self,
                "error",
                "selecciona un radio button"
            )
        self.mostrar_Qplain()

    def dibujarSinlineas(self):
        self.scene.clear()
        pprint(self.lista)
        for particula in self.lista:
            pen = QPen()
            pen.setWidth(2)
            R = particula.red
            G = particula.green
            B = particula.blue
            color = QColor(R, G, B)
            pen.setColor(color)

            x_origen = particula.origen_x
            y_origen = particula.origen_y
            self.scene.addEllipse(x_origen, y_origen, 6, 6)
            x_destino = particula.destino_x
            y_destino = particula.destino_y
            self.scene.addEllipse(x_destino, y_destino, 6, 6)

    def openSecondWindow(self):
        # Crear una instancia de la ventana secundaria
        self.second_window = SecondWindow()
        self.second_window.recibir_lista(self.lista)
        self.second_window.show()
