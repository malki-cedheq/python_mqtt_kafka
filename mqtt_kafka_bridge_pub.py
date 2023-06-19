"""
Arquivo: mqtt_kafka_bridge_pub.py
Descrição: Exemplo de kafkar producer em brigde
mqtt_kafka_bridge_pub é responsável por publicar em um tópico em um broker mqtt
e o mqtt_kafka_bridge_sub realiza o bridge entre o subscriber mqtt e kafka producer
Autores: Malki-çedheq Benjamim,
Inspiração: https://medium.com/python-point/mqtt-and-kafka-8e470eff606b
Criado em: 01/06/2023
Atualizado em: 19/06/2023
"""

import uuid
import time
from datetime import datetime
from paho.mqtt import client as mqtt_client
from dotenv import dotenv_values

env = dotenv_values(".env")

MQTT_BROKER = env["MQTT_BROKER"]
MQTT_PORT = int(env["MQTT_PORT"])
MQTT_USERNAME = env["MQTT_USERNAME"]
MQTT_PASSWORD = env["MQTT_PASSWORD"]
MQTT_PROTOCOL = "tcp"  # tcp / websockets
CLIENT_ID = "{}".format(
    uuid.uuid5(uuid.NAMESPACE_DNS, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
)  # gera um id aletório


def connect_mqtt() -> mqtt_client:
    """
    Conecta o cliente mqtt ao BROKER mqtt
    """

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Conectado ao BROKER MQTT com sucesso!")
        else:
            print("Falha ao conectar, STATUS CODE %d\n", rc)

    client = mqtt_client.Client(CLIENT_ID, transport=MQTT_PROTOCOL)
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    client.on_connect = on_connect
    client.connect(MQTT_BROKER, MQTT_PORT)
    return client


def mqtt_publish(client, topic: str, msg: str):
    """
    O cliente mqtt publica em um tópico no broker
    Argumentos:
    client: instância do cliente mqtt
    topic: nome do tópico para publicação
    msg: string a ser publicada
    """
    result = client.publish(topic, msg)
    status = result[0]  # result: [0, 1]
    if status == 0:
        return f"Enviado `{msg}` ao tópico `{topic}`"
    return f"Falha ao enviar mensagem ao tópico {topic}"


def run():
    client_mqtt = connect_mqtt()  # conecta ao broker
    # O loop_start() inicia uma nova thread, que chama o método loop em intervalos regulares.
    # Ele também lida com reconexão automaticamente.
    client_mqtt.loop_start()

    msg_count = 0
    while True:
        time.sleep(3)  # segundos
        msg = f"msg_count: {msg_count}"
        result_mqtt = mqtt_publish(
            client_mqtt, topic="contador", msg=msg
        )  # publica msg num tópico
        print(result_mqtt)
        msg_count += 1


if __name__ == "__main__":
    run()
