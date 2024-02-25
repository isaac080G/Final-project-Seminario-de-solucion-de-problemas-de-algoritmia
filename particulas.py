from math import sqrt


class particulas:
    def __init__(self, id=0, origen={}, destino={}, velocidad=0, color={}):
        self.__id = id
        self.__origen = {"x": origen["x"], "y": origen["y"]}
        self.__destino = {"x": destino["x"], "y": destino["y"]}
        self.__velocidad = velocidad
        self.__color = {"red": color["red"],
                        "green": color["green"], "blue": color["blue"]}

    def __str__(self):
        return (
            "ID: " + str(self.__id) + "\n" +
            "origen x: " + str(self.__origen["x"]) + "\n" +
            "origen y: " + str(self.__origen["y"]) + "\n"
            "destino x: " + str(self.__destino["x"]) + "\n"
            "destino y: " + str(self.__destino["y"]) + "\n"
            "velocidad: " + str(self.__velocidad) + "\n"
            "red: " + str(self.__color["red"]) + "\n"
            "green: " + str(self.__color["green"]) + "\n"
            "blue: " + str(self.__color["blue"]) + "\n"
            "distancia: " + str(self.distancia_euclidiana(self.__origen["x"],
                                self.__origen["y"], self.__destino["x"], self.__destino["y"]))
        )

    def to_dict(self):
        return {
            "id": self.__id,
            "origen": {
                "x": self.__origen["x"],
                "y": self.__origen["y"]
            },
            "destino": {
                "x": self.__destino["x"],
                "y": self.__destino["y"]
            },
            "velocidad": self.__velocidad,
            "color": {
                "red": self.__color["red"],
                "green": self.__color["green"],
                "blue": self.__color["blue"]
            }

        }

    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__lista):
            li = self.__lista[self.cont]
            self.cont += 1
            return li
        else:
            raise StopIteration

    def distancia_euclidiana(self, x1, y1, x2, y2):
        return sqrt((x2-x1)**2+(y2-y1)**2)

    @ property
    def id(self):
        return self.__id

    @ property
    def origen_x(self):
        return self.__origen["x"]

    @ property
    def origen_y(self):
        return self.__origen["y"]

    @ property
    def destino_x(self):
        return self.__destino["x"]

    @ property
    def destino_y(self):
        return self.__destino["y"]

    @ property
    def velocidad(self):
        return self.__velocidad

    @ property
    def red(self):
        return self.__color["red"]

    @ property
    def green(self):
        return self.__color["green"]

    @ property
    def blue(self):
        return self.__color["blue"]

    @ property
    def distancia(self):
        return self.distancia_euclidiana(self.__origen["x"],
                                         self.__origen["y"], self.__destino["x"], self.__destino["y"])
