# from grafo import nodo
from collections import deque
from queue import PriorityQueue
from networkx.utils import UnionFind
# from grafo import nodo


class nodo:
    def __init__(self, dato) -> None:
        self.__dato = dato

    @property
    def dato(self):
        return self.__dato

    def __str__(self) -> str:

        return str(self.__dato)

    def __eq__(self, __value: object) -> bool:
        if self.__dato == __value.dato:
            return True
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.dato)


class arista:
    def __init__(self, n1: nodo, n2: nodo) -> None:
        self.__par = [n1, n2]

    def dirigido(self) -> bool:
        return False

    def ponderada(self) -> bool:
        return False

    def get_par(self) -> list:
        return self.__par

    def __str__(self) -> str:
        return f"(nodo:{self.get_par()[0]}?------arista-----? (nodo:){self.get_par()[1]})"

    def __eq__(self, __value: object) -> bool:
        if self.get_par()[0] == __value.get_par()[0] and self.get_par()[1] == __value.get_par()[1]:
            return True
        else:
            return False


class aristaNoDirigida(arista):
    def __init__(self, n1: nodo, n2: nodo) -> None:
        super().__init__(n1, n2)

    def dirigido(self) -> bool:
        return False

    def get_nodo(self) -> nodo:
        return self.get_par()[0]

    def get_nodo2(self) -> nodo:
        return self.get_par()[1]

    def __str__(self) -> str:
        return f"(nodo:{self.get_nodo()}<------arista-----> (nodo:){self.get_nodo2})"


class grafo:
    def __init__(self) -> None:
        self.__aristas = []
        self.__ady = dict()

    def agregar_arista(self, arista: arista):
        if arista not in self.__aristas:
            self.__aristas.append(arista)

    def __str__(self) -> str:
        return str([str(arista)for arista in self.__aristas])

    def eliminarArista(self):
        self.__aristas.remove(arista)

    def get_lista_ad(self) -> dict:
        self.__ady.clear()
        for arista in self.__aristas:
            if arista.dirigido():
                pass
            else:
                n1 = arista.get_nodo()
                n2 = arista.get_nodo2()
                self.agregar_lista(n1, n2, arista.peso)
                self.agregar_lista(n2, n1, arista.peso)
        return self.__ady

    def print_ady(self):
        self.get_lista_ad()
        text = []
        for key in self.__ady.keys():
            textAux = ""
            print(key, "<------>", end="")
            textAux = "{}<------>.".format(key)
            # textAux.join(str(key) + "------>", end="")
            for value in self.__ady[key]:
                nodo = value[0]
                peso = value[1]
                print(nodo, peso, end="")
                textAux += (str(nodo)+str(peso))
            print("")
            text.append(textAux)
        return text

    def agregar_lista(self, n1: nodo, n2: nodo, peso):
        if n1 in self.__ady:
            self.__ady[n1].append([n2, peso])
        else:
            self.__ady[n1] = [[n2, peso]]

    def recorrido_profundidad(self, inicio: nodo) -> list:
        visitados = []
        pila = deque()
        recorrido = []

        grafo = self.get_lista_ad()

        if inicio not in grafo:
            return recorrido

        recorrido.append(inicio)
        visitados.append(inicio)

        while pila:
            nodo = pila.pop()
            recorrido.append(nodo)

            for ady in grafo[nodo]:
                if ady[0] not in visitados:
                    pila.append(ady[0])
                    visitados.append(ady[0])

        return recorrido


class poderada:
    def __init__(self, peso) -> None:
        self.__peso = peso

    @property
    def peso(self):
        return self.__peso


class aristaNoDirigidaPonderada(aristaNoDirigida, poderada):
    def __init__(self, n1: nodo, n2: nodo, peso) -> None:
        aristaNoDirigida.__init__(self, n1, n2)
        poderada.__init__(self, peso)

    def ponderada(self) -> bool:
        return True

    def __str__(self) -> str:
        return f"(nodo:{self.get_nodo()}<------arista:{self.peso}-----> (nodo:){self.get_nodo2})"
