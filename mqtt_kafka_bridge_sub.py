"""
Arquivo: mqtt_kafka_bridge_sub.py
Descrição: Exemplo de kafkar producer em brigde
mqtt_kafka_bridge_pub é responsável por publicar em um tópico em um broker mqtt
e o mqtt_kafka_bridge_sub realiza o bridge entre o subscriber mqtt e kafka producer
Autores: Malki-çedheq Benjamim,
Inspiração: https://medium.com/python-point/mqtt-and-kafka-8e470eff606b
Criado em: 01/06/2023
Atualizado em: 21/06/2023
"""

import uuid
from datetime import datetime
from functions_kafka import connect_kafka, kafka_sync_producer
from functions_mqtt import connect_mqtt
from functions_mqtt_kafka_common import subscribe_and_produce
from variables import (
    MQTT_BROKER,
    MQTT_PORT,
    MQTT_USERNAME,
    MQTT_PASSWORD,
    MQTT_PROTOCOL,
    KAFKA_BROKER,
    KAFKA_PORT,
    KAFKA_USERNAME,
    KAFKA_PASSWORD,
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
        # Sincroniza o produzir com um tópico no kafka
        kafka_producer = kafka_sync_producer(client_kafka, "contador")

        # Inscrições nos tópicos mqtt e bridge kafka
        subscribe_and_produce(client_mqtt, "contador", kafka_producer)

        # O método bloqueia o programa, é útil quando o programa deve ser executado indefinidamente
        client_mqtt.loop_forever()
    else:
        print("LOG: Não conectou ao mqtt ou kafka.")


if __name__ == "__main__":
    run()
