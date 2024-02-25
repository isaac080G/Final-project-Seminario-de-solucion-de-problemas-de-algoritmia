from PySide2.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsLineItem, QLabel, QGraphicsTextItem
from PySide2.QtGui import QPalette, QColor, QPen, QBrush, QFont
from ui_SecondWindow import Ui_SecondWindow
from lista import lista
from PySide2.QtGui import QMovie
from PySide2.QtCore import Qt, QUrl, QSize, QTimer
from particulas import particulas
from random import randint
from algoritmos import puntos_cercanos, distancia_euclidiana
import networkx as nx
from grafo import nodo, arista, aristaNoDirigida, grafo, aristaNoDirigidaPonderada
from queue import PriorityQueue
from networkx.utils import UnionFind
import json
import heapq


class SecondWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene()
        # self.animacion()
        self.ui.graphicsView_2.setScene(self.scene)
        self.G = grafo()
        self.ui.pushButton_grafos.clicked.connect(self.dibujar)
        self.flag = 0
        self.ui.pushButton_2_kruskal.clicked.connect(self.kruskal_algorim)
        self.ui.pushButton_prim.clicked.connect(self.dijkstra)

    def recibir_lista(self, lista):
        self.lista2 = lista
        print("-----------------------------------------------------------------------")
        self.info()
        # print(self.lista2)

    def animacion(self):

        # Creamos el objeto QMovie y lo configuramos para mostrar la animación
        self.movie = QMovie("progress-bar.gif")
        self.movie.setScaledSize(QSize(500, 500))
        self.label = QLabel()
        self.label.setMovie(self.movie)

        # Añadimos el QLabel a la escena
        self.scene.addWidget(self.label)
        self.label.show()

        # Iniciamos la animación del QMovie
        self.movie.start()
        QTimer.singleShot(4500, self.stop_movie)

    def stop_movie(self):
        # Detener la reproducción del gif y eliminar el QGraphicsPixmapItem
        self.movie.stop()
        self.scene.clear()
        self.dibujar_aristas()
        # print(resultado)

        # self.ui.lcdNumber.display(len(resultado)/2)

    def wheelEvent(self, event):
        print(event.delta())
        if event.delta() > 0:
            self.ui.graphicsView_2.scale(1.2, 1.2)
        else:
            self.ui.graphicsView_2.scale(0.8, 0.8)

    def dibujar_aristas(self):
        self.dibujar()
        if self.flag == 1:
            for edge in self.arbol_minimo.edges.data('weight'):
                print("-------------")
                print(edge)

                pen = QPen()
                pen.setWidth(2)
                R = randint(0, 255)
                G = randint(0, 255)
                B = randint(0, 255)
                color = QColor(R, G, B)
                pen.setColor(color)
                line = QGraphicsLineItem(
                    edge[0][0], edge[0][1], edge[1][0], edge[1][1])
                line.setPen(pen)
                self.scene.addItem(line)
                text = QGraphicsTextItem(str(edge[2]))
                font = QFont("Arial", 6)
                text.setFont(font)
                text.setPos((edge[0][0] + edge[1][0])/2,
                            (edge[0][1] + edge[1][1])/2 - 10)
                self.scene.addItem(text)
        elif self.flag == 2:
            keylist = []
            for key in self.dist:
                pen = QPen()
                pen.setWidth(2)
                R = randint(0, 255)
                G = randint(0, 255)
                B = randint(0, 255)
                color = QColor(R, G, B)
                pen.setColor(color)
                keylist.append(key)
                self.dibujar()
            for index, key1 in enumerate(keylist):
                print("____")
                print(key1)
                if index < len(keylist) - 1:
                    self.scene.addLine(
                        key1[0], key1[1], keylist[index + 1][0], keylist[index + 1][1], pen)
                    text = QGraphicsTextItem(
                        str(self.cantidades[key]))
                    font = QFont("Arial", 6)
                    text.setFont(font)
                    text.setPos(
                        keylist[index + 1][0], (keylist[index + 1][1]-20))
                    self.scene.addItem(text)
            self.scene.addEllipse(
                keylist[0][0], keylist[0][1], 8, 8, pen)
            text = QGraphicsTextItem("start")
            font = QFont("Arial", 8)
            text.setFont(font)
            text.setPos(keylist[0][0], keylist[0][1] - 20)
            self.scene.addItem(text)
            print("---------")
            print(keylist)
        self.info()

    def dibujar(self):
        # pprint(self.lista2)
        for particula in self.lista2:
            pen = QPen()
            pen.setWidth(2)
            R = particula.red
            G = particula.green
            B = particula.blue
            color = QColor(R, G, B)
            pen.setColor(color)

            x_origen = particula.origen_x
            y_origen = particula.origen_y
            self.scene.addEllipse(x_origen, y_origen, 6, 6, pen)
            x_destino = particula.destino_x
            y_destino = particula.destino_y
            self.scene.addEllipse(x_destino, y_destino, 6, 6, pen)

    def generarGrafo(self):
        # self.animacion()
        self.lista2.ordenar_distancia()
        for particula in self.lista2:
            self.G.agregar_arista(aristaNoDirigidaPonderada(
                (particula.origen_x, particula.origen_y), (particula.destino_x, particula.destino_y), distancia_euclidiana(particula.origen_x, particula.origen_y, particula.destino_x, particula.destino_y)))
        # for particula in self.lista2:
        #    G.agregar_arista(aristaNoDirigida(
        #        particula.destino_x, particula.destino_y))
        # print(G)
        # self.ui.plainTextEdit.insertPlainText(str(self.G.print_ady()))
        print(self.G.get_lista_ad())

    def generarNX(self):
        graph = nx.Graph()
        for key in self.G.get_lista_ad().keys():
            for edge in self.G.get_lista_ad()[key]:
                graph.add_edge(key, edge[0], weight=edge[1])
        return graph

    def kruskal_algorim(self):
        self.generarGrafo()
        graph = self.generarNX()
        minimum_spaning_tree = nx.minimum_spanning_tree(graph)
        for n in self.G.recorrido_profundidad((0, 100)):
            print(n)
        self.arbol_minimo = minimum_spaning_tree
        # self.scene.clear()
        self.flag = 1
        self.dibujar()
        self.animacion()

        self.ui.plainTextEdit.clear()
        text = ""
        for edge in self.arbol_minimo.edges.data('weight'):
            print("-------------")
            text += ("("+str(edge[0][0])+","+str(edge[0][1])+")"+"<---------->" +
                     "("+str(edge[1][0])+"," +
                     str(edge[1][1])+")"+"dist="+str(edge[2])+"\n")
        self.ui.plainTextEdit.setPlainText(text)

    import heapq

    def dijkstra(self, graph):
        self.generarGrafo()
        graph = self.G.get_lista_ad()
        start = (int(self.ui.lineEdit.text()), int(self.ui.lineEdit_2.text()))
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        visited = set()
        heap = [(0, start)]
        previous = {}  # Rastrea los nodos previos en el camino más corto

        while heap:
            current_distance, current_node = heapq.heappop(heap)

            if current_node in visited:
                continue

            visited.add(current_node)

            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    # Actualiza el nodo previo
                    previous[neighbor] = current_node

                    # Agrega el vecino al montón con la nueva distancia
                    heapq.heappush(heap, (distance, neighbor))

        target_node = (int(self.ui.lineEdit_3_destino_x.text()),
                       int(self.ui.lineEdit_4destino_Y.text()))

        # Recuperar el camino más corto hacia el nodo objetivo
        self.cantidades = distances
        self.dist = path = []
        current_node = target_node
        while current_node in previous:
            path.insert(0, current_node)
            current_node = previous[current_node]
        path.insert(0, current_node)

        print("Distancias más cortas:", distances)
        print("Camino más corto hacia el nodo objetivo:", path)
        self.animacion()
        self.flag = 2
        text = str(path[0])
        for indice, tupla in enumerate(path):
            if indice > 0:  # Omitir la primera iteración (índice 0)
                text += "<---------> {}".format(tupla)
                print(text)
        self.ui.plainTextEdit.setPlainText(text)

    def info(self):
        with open('info.json', 'r') as archivo:
            contenido = json.load(archivo)

        if self.flag == 1:
            self.ui.plainTextEdit_2.setPlainText(contenido["kruskal"])
        elif self.flag == 2:
            self.ui.plainTextEdit_2.setPlainText(contenido["dijkstra"])
        else:
            self.ui.plainTextEdit_2.setPlainText("selecciona un algoritmo")
