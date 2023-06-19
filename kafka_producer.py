"""
Arquivo: kafka_producer.py
Descrição: Exemplo de kafkar producer em python
Publica mensagens em um topico de um broker de um cluster kafka
Autores: Malki-çedheq Benjamim,
Criado em: 01/06/2023
Atualizado em: 19/06/2023
"""
from pykafka import KafkaClient
import time
from dotenv import dotenv_values

env = dotenv_values(".env")

KAFKA_BROKER = env["KAFKA_BROKER"]
KAFKA_PORT = int(env["KAFKA_PORT"])
KAFKA_USERNAME = env["KAFKA_USERNAME"]
KAFKA_PASSWORD = env["KAFKA_PASSWORD"]


def connect_kafka() -> KafkaClient:
    """
    Conecta o cliente ao broker kafka
    """
    try:
        kafka_client = KafkaClient(
            hosts="{}:{}".format(env["KAFKA_BROKER"], env["KAFKA_PORT"])
        )
        print("LOG: Conectado ao Kafka com sucesso!")
        return kafka_client
    except:
        print("LOG: Falha ao conectar com Kafka")
        return None


def run():
    client_kafka = connect_kafka()

    if client_kafka:
        print("LOG: Dict de tópicos disponíveis: {}".format(client_kafka.topics))

        topic = client_kafka.topics["my.test"]
        print("LOG: Tópico selecionado: {}".format(topic))

        msg_count = 0
        while True:
            time.sleep(1)  # segundos
            msg_payload = f"msg_count: {msg_count}"
            topic.get_sync_producer().produce(msg_payload.encode("ascii"))
            print(
                "LOG: KAFKA: Publicou {} no tópico {}".format(
                    msg_payload, topic.name.decode("utf-8")
                )
            )
            msg_count += 1


if __name__ == "__main__":
    run()
