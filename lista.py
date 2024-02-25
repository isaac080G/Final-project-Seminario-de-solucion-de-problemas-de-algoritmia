from particulas import particulas
import json


class lista:
    def __init__(self):
        self.__lista = []

    def agregar_final(self, particula):
        self.__lista.append(particula)

    def agregar_inicio(self, particula):
        self.__lista.insert(0, particula)

    def mostrar(self):
        for p in self.__lista:
            print(p)

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

    def __len__(self):
        return (
            len(self.__lista)
        )

    def __str__(self):
        return "".join(
            str(v) + "\n" for v in self.__lista
        )

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__lista]
                print(lista)
                json.dump(lista, archivo, indent=5)
                return 1
        except:
            return 0

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                # print(lista)
                self.__lista = [particulas(**particula) for particula in lista]
                return 1
        except FileNotFoundError:
            print(f"El archivo {ubicacion} no existe.")
            return 0
        except Exception as e:
            try:
                with open(ubicacion, 'r') as archivo:
                    lista = json.load(archivo)
                    self.__lista = [particulas(
                        id=particula["id"],
                        origen={"x": particula["origen_x"],
                                "y":particula["origen_y"]},
                        destino={
                            "x": particula["destino_x"], "y":particula["destino_y"]},
                        velocidad=particula["velocidad"],
                        color={"red": particula["red"],
                               "green":particula["green"],
                               "blue":particula["blue"], }
                    ) for particula in lista]
                    return 1
            except Exception as e:
                print(
                    f"Error al abrir el archivo {ubicacion} con el formato 2: {e}")
                return 0

    def ordenar_id(self):
        self.__lista.sort(key=lambda x: x.id)

    def ordenar_distancia(self):
        self.__lista.sort(key=lambda x: x.distancia)

    def ordenar_velocidad(self):
        self.__lista.sort(key=lambda x: x.velocidad)

    def returnLista(self):
        return self.__lista
