"""
Arquivo: mqtt_kafka_parallel_pub.py
Descrição: Exemplo de kafkar producer em paralelo com a publicação mqtt
mqtt_kafka_parallel_pub é responsável por publicar em um tópico em um broker mqtt e também no kafka
e o mqtt_kafka_parallel_sub realiza o subscribe tanto no mqtt e quando no kafka consumer
Autores: Malki-çedheq Benjamim,
Inspiração: https://medium.com/python-point/mqtt-and-kafka-8e470eff606b
Criado em: 01/06/2023
Atualizado em: 21/06/2023
"""

import time
import uuid
from datetime import datetime

from functions_kafka import connect_kafka, kafka_publish
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
    client_kafka = connect_kafka(KAFKA_BROKER, KAFKA_PORT)  # conecta ao broker kafka

    if client_mqtt and client_kafka:
        # O loop_start() inicia uma nova thread, que chama o método loop em intervalos regulares.
        # Ele também lida com reconexão automaticamente.
        client_mqtt.loop_start()
        msg_count = 0
        while True:
            time.sleep(2)  # segundos
            msg = f"msg_count: {msg_count}"
            topico = "contador"
            result_mqtt = mqtt_publish(
                client_mqtt, topic=topico, msg=msg
            )  # publica msg num tópico
            result_kafka = kafka_publish(client_kafka, topico, msg)
            print(result_mqtt)
            print(result_kafka)
            msg_count += 1
    else:
        print("LOG: Não conectou ao mqtt ou kafka.")


if __name__ == "__main__":
    run()
