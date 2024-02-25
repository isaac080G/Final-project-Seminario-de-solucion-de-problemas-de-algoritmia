from math import sqrt
from lista import lista


def distancia_euclidiana(x1, y1, x2, y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)


def puntos_cercanos(lista) -> list:
    resultado = []
    for punto in lista.returnLista():
        for i in range(2):
            if (i == 0):
                x1 = punto.destino_x
                y1 = punto.destino_y
            else:
                x1 = punto.origen_x
                y1 = punto.origen_y
            min = 1000
            cercano = (0, 0)
            for punto_j in lista.returnLista():
                if punto_j != punto:
                    x2 = punto_j.destino_x
                    y2 = punto_j.destino_y
                    d = distancia_euclidiana(x1, y1, x2, y2)
                    x3 = punto_j.origen_x
                    y3 = punto_j.origen_y
                    d2 = distancia_euclidiana(x1, y1, x3, y3)
                    if d < d2 and d < min:
                        min = d
                        cercano = (x2, y2)
                    elif d2 < min:
                        min = d2
                        cercano = (x3, y3)

            resultado.append((x1, y1))
            resultado.append(cercano)

    return resultado
