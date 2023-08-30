# iot-grupo-2
MVP de practica para conectar sensores con un broker y una respuesta a un relay



Para iniciar el proyecto Instalar:
- Python3
- CounterFit 
- counterfit-connection
- counterfit-shims-grove
- paho-mqtt



Levantar el counterfit en el puerto por defecto 5000

agregar los sensores de temperatura en el pin 0, 1 y 2

agregar los actuadores relay en el pin 10, 11, 12 


correr los archivos .py por separado en terminales distintas. 


seleccionar un valor para la temperatura de cada sensor 
el sensor envia una señal al detectar que la temperatura es superior a los 32 grados celsius (se debe setear 320 en el CounterFit)
el sensor envia una señal al detectar que la temperatura es inferior a los 20 grados celsius (se debe setear 200 en el CounterFit)





