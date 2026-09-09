# Projeto IoT - ESP32, DHT11 e ThingSpeak
# Projeto acadêmico

import network
import urequests
import dht
import machine
import time

# Wi-Fi
nomeWifi = "NOME_DA_REDE_WIFI"
password = "SENHA_DO_WIFI"

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(nomeWifi, password)

# Esperar conexão
while not station.isconnected():
    print("Conectando...")
    time.sleep(1)

# Status Internet
print("Conectado")
print("Conectando al WiFi:", station.isconnected())
print("IP:", station.ifconfig())

# ThingSpeak
api_key = "SUA_API_KEY_DO_THINGSPEAK"

# Sensor e relé
d = dht.DHT11(machine.Pin(4))
rele = machine.Pin(14, machine.Pin.OUT)

while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()

    print("Temp={} Hum={}".format(temp, hum))

    # Lógica do relé
    if temp > 31 or hum > 70:
        rele.value(1)  # ligar
    else:
        rele.value(0)  # desligar

    # Enviar dados para o ThingSpeak
    url = (
        "https://api.thingspeak.com/update"
        "?api_key={}&field1={}&field2={}"
    ).format(api_key, temp, hum)

    response = urequests.get(url)
    response.close()

    time.sleep(15)
