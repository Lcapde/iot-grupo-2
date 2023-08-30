import paho.mqtt.client as mqtt

broker_address = "127.0.0.1"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
    print("Conectado al broker MQTT")
    client.subscribe("temperatura/telemetria")

def on_message(client, userdata, msg):    
    temperaturas = list(map(float, msg.payload.decode().split(',')))
    
    for i, temperatura in enumerate(temperaturas):
        print(f"Sensor {i+1} - Temperatura: {temperatura} °C")
        if temperatura > 32:
            print("\n")
            print(f"Sensor {i+1} - Temperatura: {temperatura} °C")
            print("¡Alerta! Alta temperatura detectada, activar relay")
            print("\n")
            client.publish("temperatura/alerta", f"Sensor {i+1} - Alta temperatura detectada")
        if temperatura < 20:
            print("\n")
            print(f"Sensor {i+1} - Temperatura: {temperatura} °C")
            print("¡Alerta! Temperatura normalizada detectada, desactivar relay")
            print("\n")
            client.publish("temperatura/alerta", f"Sensor {i+1} - Temperatura normalizada detectada")

client = mqtt.Client()
client.connect(broker_address, broker_port, 60)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
