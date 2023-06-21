"""
Arquivo: kafka_producer.py
Descrição: Exemplo de kafkar producer em python
Publica mensagens em um topico de um broker de um cluster kafka
Autores: Malki-çedheq Benjamim,
Criado em: 01/06/2023
Atualizado em: 19/06/2023
"""

import time
from functions_kafka import connect_kafka, kafka_publish
from variables import (
    KAFKA_BROKER,
    KAFKA_PORT,
    KAFKA_USERNAME,
    KAFKA_PASSWORD,
)


def run():
    client_kafka = connect_kafka(KAFKA_BROKER, KAFKA_PORT)  # conecta ao broker kafka

    if client_kafka:
        topic_name = "grupo1.topico1"
        print("LOG: Nome do tópico selecionado: {}".format(topic_name))
        msg_count = 0
        while True:
            time.sleep(1)  # segundos
            msg_payload = f"msg_count: {msg_count}"
            result_kafka = kafka_publish(client_kafka, topic_name, msg_payload)
            print(result_kafka)
            msg_count += 1


if __name__ == "__main__":
    run()
