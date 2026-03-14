# %%
import threading
import time
import random
from threading import Semaphore

# Buffer compartido
buffer = []

# Semáforos
empty = Semaphore(5)
full = Semaphore(0)
mutex = Semaphore(1)

# Control de ejecución
running = True


def sensor(sensor_id):
    global running
    while running:
        dato = random.randint(1, 100)

        empty.acquire()
        mutex.acquire()

        buffer.append(dato)
        print(f"Sensor {sensor_id} detectó tráfico: {dato} | Buffer: {buffer}")

        mutex.release()
        full.release()

        time.sleep(random.uniform(0.3, 1))


def analizador():
    global running
    while running or buffer:
        full.acquire()
        mutex.acquire()

        if buffer:
            dato = buffer.pop(0)
            print(f"Analizador procesó: {dato} | Buffer restante: {buffer}")

        mutex.release()
        empty.release()

        time.sleep(0.7)


print("Simulación SIGET iniciada...\n")

# Crear hilos
sensor1 = threading.Thread(target=sensor, args=(1,))
sensor2 = threading.Thread(target=sensor, args=(2,))
sensor3 = threading.Thread(target=sensor, args=(3,))
consumidor = threading.Thread(target=analizador)

sensor1.start()
sensor2.start()
sensor3.start()
consumidor.start()

# Ejecutar durante 5 segundos
time.sleep(5)
running = False

# Esperar a que terminen
sensor1.join()
sensor2.join()
sensor3.join()
consumidor.join()

print("\nSimulación finalizada.")


