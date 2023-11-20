# main.py
from semaforo import Semaforo
from vehiculo import Vehiculo
import threading

if __name__ == "__main__":
    semaforo_calle = Semaforo()  # Un único semáforo para ambas calles

    vehiculos_calle_izquierda = [Vehiculo(i, "IZQUIERDA", semaforo_calle) for i in range(5)]
    vehiculos_calle_derecha = [Vehiculo(i + 5, "DERECHA", semaforo_calle) for i in range(5)]

    thread_semaforo_calle = threading.Thread(target=semaforo_calle.cambiar_estado)

    threads_vehiculos_calle_izquierda = [threading.Thread(target=vehiculo.conducir) for vehiculo in vehiculos_calle_izquierda]
    threads_vehiculos_calle_derecha = [threading.Thread(target=vehiculo.conducir) for vehiculo in vehiculos_calle_derecha]

    thread_semaforo_calle.start()

    for thread_vehiculo in threads_vehiculos_calle_izquierda + threads_vehiculos_calle_derecha:
        thread_vehiculo.start()

    # Espera a que todos los vehículos crucen
    for thread_vehiculo in threads_vehiculos_calle_izquierda + threads_vehiculos_calle_derecha:
        thread_vehiculo.join()

    # Detén el programa después de que todos los vehículos hayan cruzado
    semaforo_calle.detener_programa()

    thread_semaforo_calle.join()

    print("Programa terminado.")
