# Simulación de Concurrencia en SIGET 🚦

Este proyecto implementa una simulación del problema clásico de concurrencia **Productor–Consumidor**, adaptado específicamente a un Sistema de Gestión de Tráfico Urbano (**SIGET**).

## 📝 Descripción

En este escenario, se simula el flujo de información de una red vial inteligente:
* **Productores:** Sensores de tráfico que generan datos constantes sobre el flujo vehicular.
* **Consumidor:** Un módulo de análisis que procesa dicha información para la toma de decisiones.
* **Buffer Compartido:** Almacén temporal de datos donde la sincronización es crítica.

La solución utiliza **semáforos** para gestionar el acceso a los recursos, evitando condiciones de carrera y garantizando que los datos se procesen en el orden correcto sin pérdidas.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python
* **Librerías:** `threading` (para la ejecución concurrente)
* **Mecanismos:** Semáforos y Mutex

## 🏗️ Estructura del Sistema

El sistema opera con múltiples hilos ejecutándose de forma simultánea:

### Procesos Concurrentes
1.  **Sensor de tráfico 1** (Productor)
2.  **Sensor de tráfico 2** (Productor)
3.  **Sensor de tráfico 3** (Productor)
4.  **Analizador de tráfico** (Consumidor)

---

## 🔐 Mecanismos de Sincronización

Para garantizar la integridad de la simulación, se han implementado tres semáforos principales:

| Semáforo | Función |
| :--- | :--- |
| `empty` | Controla los espacios disponibles en el buffer. |
| `full` | Indica la cantidad de datos listos para ser procesados. |
| `mutex` | Garantiza la **exclusión mutua** (solo un hilo accede al buffer a la vez). |

### Problemas Resueltos:
* **Condiciones de carrera:** Evita que dos sensores escriban en el mismo espacio al mismo tiempo.
* **Pérdida de datos:** Asegura que el analizador no intente leer si el buffer está vacío.
* **Desbordamiento:** Impide que los sensores generen datos si el buffer está lleno.

---

## 🚀 Ejecución

Para correr la simulación, asegúrate de tener Python instalado y ejecuta:

```bash
python main.py
