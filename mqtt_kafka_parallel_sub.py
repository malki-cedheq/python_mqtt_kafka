"""
Arquivo: mqtt_kafka_parallel_sub.py
Descrição: Exemplo de kafkar producer em paralelo com a publicação mqtt
mqtt_kafka_parallel_pub é responsável por publicar em um tópico em um broker mqtt e também no kafka
e o mqtt_kafka_parallel_sub realiza o subscribe tanto no mqtt e quando no kafka consumer
Autores: Malki-çedheq Benjamim,
Inspiração: https://medium.com/python-point/mqtt-and-kafka-8e470eff606b
Criado em: 01/06/2023
Atualizado em: 21/06/2023
"""

import uuid
from datetime import datetime

from functions_kafka import connect_kafka, kafka_sync_consumer
from functions_mqtt import connect_mqtt, subscribe
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

    topic = "contador"
    if client_mqtt and client_kafka:
        # Sincroniza o consumir com um tópico no kafka
        kafka_sync_consumer(client_kafka, topic)

        # Inscrições nos tópicos
        subscribe(client_mqtt, topic)

        # O método bloqueia o programa, é útil quando o programa deve ser executado indefinidamente
        client_mqtt.loop_forever()
    else:
        print("LOG: Não conectou ao mqtt ou kafka.")


if __name__ == "__main__":
    run()
