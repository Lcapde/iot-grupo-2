import paho.mqtt.client as mqtt
from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5000)
from counterfit_shims_grove.grove_relay import GroveRelay

broker_address = "127.0.0.1"
broker_port = 1883

relay = GroveRelay(10)
relay1 = GroveRelay(11)
relay2 = GroveRelay(12)



def on_connect(client, userdata, flags, rc):
    print("En espera de signals")
    client.subscribe("temperatura/alerta")

def on_message(client, userdata, msg):
    print(f"Recibido mensaje: {msg.payload.decode()}")
    if b"Sensor 1 " in msg.payload:
        if b"Alta temperatura detectada" in msg.payload:
            print("Activando relé...")
            relay.on()
        else:
            print("Desactivando relé...")
            relay.off()
    if b"Sensor 2 " in msg.payload:
        if b"Alta temperatura detectada" in msg.payload:
            print("Activando relé...")
            relay1.on()
        else:
            print("Desactivando relé...")
            relay1.off()

    if b"Sensor 3 " in msg.payload:
        if b"Alta temperatura detectada" in msg.payload:
            print("Activando relé...")
            relay2.on()
        else:
            print("Desactivando relé...")
            relay2.off()

client = mqtt.Client()
client.connect(broker_address, broker_port, 60)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever() 
