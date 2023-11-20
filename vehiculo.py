# vehiculo.py
import threading
import time
import random

class Vehiculo:
    def __init__(self, id_vehiculo, calle, semaforo):
        self.id_vehiculo = id_vehiculo
        self.calle = calle
        self.semaforo = semaforo
        self.eliminado = False  # Indica si el vehículo ha sido eliminado

    def conducir(self):
        while not self.semaforo.detener and not self.eliminado:
            tiempo_espera = random.randint(1, 5)
            time.sleep(tiempo_espera)

            with self.semaforo.semaforo_mutex:
                if self.calle == self.semaforo.lado_actual:
                    if self.semaforo.estado == "VERDE":
                        print(f"Calle {self.calle} - Vehículo {self.id_vehiculo} cruzando el cruce.")
                        self.eliminado = True
                        self.semaforo.vehiculos_eliminados.append(self)
                    else:
                        print(f"Calle {self.calle} - Vehículo {self.id_vehiculo} esperando en el semáforo rojo.")
                else:
                    print(f"Calle {self.calle} - Vehículo {self.id_vehiculo} Cruzando")
                    self.eliminado = True
                    self.semaforo.vehiculos_eliminados.append(self)
