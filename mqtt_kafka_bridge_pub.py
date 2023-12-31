"""
Arquivo: mqtt_kafka_bridge_pub.py
Descrição: Exemplo de kafkar producer em brigde
mqtt_kafka_bridge_pub é responsável por publicar em um tópico em um broker mqtt
e o mqtt_kafka_bridge_sub realiza o bridge entre o subscriber mqtt e kafka producer
Autores: Malki-çedheq Benjamim,
Inspiração: https://medium.com/python-point/mqtt-and-kafka-8e470eff606b
Criado em: 01/06/2023
Atualizado em: 21/06/2023
"""

import time
import uuid
from datetime import datetime

from random import gauss
from random import seed

import json

from functions_mqtt import connect_mqtt, mqtt_publish
from variables import (
    KAFKA_BROKER,
    KAFKA_PASSWORD,
    KAFKA_PORT,
    KAFKA_USERNAME,
    MQTT_BROKER,
    MQTT_PASSWORD,
    MQTT_PORT,
    MQTT_PROTOCOL,
    MQTT_USERNAME,
)

CLIENT_ID = "{}".format(
    uuid.uuid5(uuid.NAMESPACE_DNS, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
)  # gera um id aletório


def run():
    client_mqtt = connect_mqtt(
        MQTT_BROKER, MQTT_PORT, CLIENT_ID, MQTT_PROTOCOL, MQTT_USERNAME, MQTT_PASSWORD
    )  # conecta ao broker mqtt
    # O loop_start() inicia uma nova thread, que chama o método loop em intervalos regulares.
    # Ele também lida com reconexão automaticamente.
    client_mqtt.loop_start()

    msg_count = 0
    # seed random number generator
    seed(1)
    while True:
        time.sleep(1)  # segundos
        # create white noise series
        series = [gauss(0.0, 1.0) for i in range(10)]
        msg = json.dumps({"series": series, "msg_count": msg_count})
        result_mqtt = mqtt_publish(
            client_mqtt, topic="contador", msg=msg
        )  # publica msg num tópico
        # print(result_mqtt)
        msg_count += 1


if __name__ == "__main__":
    run()
