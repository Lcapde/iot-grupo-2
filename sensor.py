import time
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.adc import ADC
import paho.mqtt.client as mqtt

CounterFitConnection.init('127.0.0.1', 5000)

adc = ADC()
broker_address = "127.0.0.1"
broker_port = 1883

def obtener_temperatura(sensor):
    valor_analogico = adc.read(sensor)
    temperatura = valor_analogico * 0.1
    return temperatura

client = mqtt.Client()
client.connect(broker_address, broker_port, 60)

while True:
    temperatura_sensor1 = obtener_temperatura(0)
    temperatura_sensor2 = obtener_temperatura(1)
    temperatura_sensor3 = obtener_temperatura(2)

    print(f"Sensor 1 - Temperatura actual: {temperatura_sensor1:.2f} °C")
    print(f"Sensor 2 - Temperatura actual: {temperatura_sensor2:.2f} °C")
    print(f"Sensor 3 - Temperatura actual: {temperatura_sensor3:.2f} °C")

    # Enviar la telemetría de temperatura al broker MQTT
    telemetry_data = f"{temperatura_sensor1:.2f},{temperatura_sensor2:.2f},{temperatura_sensor3:.2f}"
    client.publish("temperatura/telemetria", telemetry_data)

    time.sleep(1)
