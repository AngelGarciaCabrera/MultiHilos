# semaforo.py
import threading
import time

class Semaforo:
    def __init__(self):
        self.estado = "VERDE"
        self.semaforo_mutex = threading.Lock()
        self.detener = False  # Bandera para detener el programa
        self.vehiculos_eliminados = []  # Lista para rastrear vehículos eliminados
        self.lado_actual = "IZQUIERDA"  # Inicia con el lado izquierdo

    def cambiar_estado(self):
        while not self.detener:
            with self.semaforo_mutex:
                if self.estado == "VERDE":
                    self.estado = "ROJO"
                else:
                    self.estado = "VERDE"
                    self.lado_actual = "DERECHA" if self.lado_actual == "IZQUIERDA" else "IZQUIERDA"
                    self.eliminar_vehiculos()  # Elimina vehículos marcados como eliminados
                print(f"Semaforo cambió a {self.estado}. Lado actual: {self.lado_actual}")
            time.sleep(5)  # Cambia cada 5 segundos

    def eliminar_vehiculos(self):
        self.vehiculos_eliminados = [vehiculo for vehiculo in self.vehiculos_eliminados if not vehiculo.eliminado]
        for vehiculo in self.vehiculos_eliminados:
            print(f"Eliminando vehículo {vehiculo.id}")
        self.vehiculos_eliminados = []

    def detener_programa(self):
        self.detener = True
