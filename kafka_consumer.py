"""
Arquivo: kafka_consumer.py
Descrição: Exemplo de kafkar consumer em python
Consome mensagens de um topico de um broker de um cluster kafka
Autores: Malki-çedheq Benjamim,
Criado em: 01/06/2023
Atualizado em: 19/06/2023
"""
from functions_kafka import connect_kafka, kafka_sync_consumer
from variables import KAFKA_BROKER, KAFKA_PASSWORD, KAFKA_PORT, KAFKA_USERNAME


def run():
    client_kafka = connect_kafka(KAFKA_BROKER, KAFKA_PORT)  # conecta ao broker kafka

    if client_kafka:
        print("LOG: Dicionário de tópicos disponíveis: {}".format(client_kafka.topics))

        topic = client_kafka.topics["grupo1.topico1"]
        print("LOG: Tópico selecionado: {}".format(topic))

        topic_name = topic.name.decode("utf-8")
        print("LOG: Nome do tópico selecionado: {}".format(topic_name))

        kafka_sync_consumer(client_kafka, topic_name)


if __name__ == "__main__":
    run()
