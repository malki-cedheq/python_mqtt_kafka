"""
Arquivo: kafka_consumer.py
Descrição: Exemplo de kafkar consumer em python
Consome mensagens de um topico de um broker de um cluster kafka
Autores: Malki-çedheq Benjamim,
Criado em: 01/06/2023
Atualizado em: 19/06/2023
"""
from pykafka import KafkaClient
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

        consumer = topic.get_simple_consumer()
        for message in consumer:
            if message is not None:
                msg_payload = (message.value).decode("utf-8")
                msg_counter = message.offset
                print(
                    "LOG {}: KAFKA: Consumiu {} no tópico {}".format(
                        msg_counter, msg_payload, topic.name.decode("utf-8")
                    )
                )


if __name__ == "__main__":
    run()
