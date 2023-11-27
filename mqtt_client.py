# Radix-IT, Makhachkala #
##     MQTT Client     ##
### Magomedov Magomed ###

import json

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

from requests import get
from requests import post

# MQTT (параметры):
mqtt_name = 'mqtt_name'
mqtt_pass = 'mqtt_password'
mqtt_server = 'mqtt_server_ip'
mqtt_port = 1883
mqtt_keep = 60

# функция, вызываемая, когда клиент
# получает CONNACK-ответ от сервера (при успешном соединении)
def on_connect(client, userdata, flags, rc):
    print("Connected to server, result code " + str(rc), end='\n\n')
    
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # Подписка в функции on_connect() означает, что, если мы потеряем соединение
    # и снова подключимся, то подписки будут возобновлены.
    if rc == 0:
        client.subscribe('application/'+AppID+'/device/'+deviceEUI+'/event/up')
        print('*' * len('Subscribed on UP-channel (from device)'))
        print('Subscribed on UP-channel (from device)')
        print('*' * len('Subscribed on UP-channel (from device)') + '\n\n')
    else:
        print('*' * len('Connection error !'))
        print('Connection error !')
        print('*' * len('Connection error !') + '\n\n')

# функция, вызываемая при получении сообщения PUBLISH
# от сервера (при получении сообщения для подписанного топика)
def on_message(client, userdata, msg):
    if json.loads(msg.payload)['fPort'] == 4:
        client.publish(f'application/{AppID}/device/{deviceEUI}/command/down',
                    time_correct, qos=0)
        client.disconnect()

# функция вызываемая при публикации
# сообщения для топика down (сообщение к устройству)
def on_publish(client, userdata, mid):
    print('*' * len('Message published !'))
    print('Message published !')
    print('*' * len('Message published !') + '\n')

# функция вызывается при разъединении с сервером
def on_disconnect(client, userdata, rc):
    print('*' * len('Client disconnected !'))
    print('Client disconnected !')
    print('*' * len('Client disconnected !') + '\n')
    print('*' * len('The end !'))
    print('The end !')
    print('*' * len('The end !') + '\n')

# настройка MQTT перед использованием
client = mqtt.Client(transport = "tcp")
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.on_publish = on_publish

##client.username_pw_set(mqtt_name, mqtt_pass)
client.connect(mqtt_server, mqtt_port, mqtt_keep)

client.loop_forever()
