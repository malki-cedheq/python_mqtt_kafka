"""
Arquivo: functions_kafka.py
Descrição: Acervo de funções para interação com kafka
Autores: Malki-çedheq Benjamim,
Criado em: 21/06/2023
Atualizado em: 21/06/2023
"""

from pykafka import KafkaClient, Producer


def connect_kafka(kafka_broker: str, kafka_port: int) -> KafkaClient:
    """
    Conecta o cliente ao broker kafka
    """
    try:
        kafka_client = KafkaClient(hosts="{}:{}".format(kafka_broker, kafka_port))
        print("LOG: Conectado ao Kafka com sucesso!")
        return kafka_client
    except:
        print("LOG: Falha ao conectar com Kafka")
        return None


def kafka_sync_producer(
    kafka_client: KafkaClient, topico: str
) -> tuple([Producer, str]):
    """
    Conecta o cliente ao broker kafka
    """
    try:
        kafka_topic = kafka_client.topics[topico]
        kafka_producer = kafka_topic.get_sync_producer()
        print(
            "LOG: Instância Kafka Producer no tópico {} criada com sucesso!".format(
                topico
            )
        )
    except:
        print(
            "LOG: Falha ao tentar criar instância Kafka Producer no tópico {}.".format(
                topico
            )
        )
    return tuple([kafka_producer, topico])


def kafka_producer_produce(producer: Producer, topic: str, msg_payload: str):
    """
    O cliente kafka publica em um tópico no broker
    Argumentos:
    client_kafka: instância do cliente kafka
    topic: nome do tópico para publicação
    msg_payload: string a ser publicada
    """
    producer.produce(msg_payload.encode("ascii"))
    # print("LOG: KAFKA: Publicou {} no tópico {}".format(msg_payload, topic))


def kafka_publish(client_kafka: KafkaClient, topic: str, msg_payload: str):
    """
    O cliente kafka publica em um tópico no broker
    Argumentos:
    client_kafka: instância do cliente kafka
    topic: nome do tópico para publicação
    msg_payload: string a ser publicada
    """
    kafka_topic = client_kafka.topics[str(topic)]
    kafka_producer = kafka_topic.get_sync_producer()
    kafka_producer.produce(msg_payload.encode("ascii"))
    return "LOG: KAFKA: Publicou {} no tópico {}".format(msg_payload, topic)


def kafka_sync_consumer(client_kafka: KafkaClient, topico: str) -> None:
    """
    sincroniza o cliente kafka a um tópico do broker
    Argumentos:
    client_kafka: instância do cliente kafka
    topic: nome do tópico para consumo
    """
    topic = client_kafka.topics[topico]
    consumer = topic.get_simple_consumer()
    for message in consumer:
        if message != None:
            msg_payload = (message.value).decode("utf-8")
            msg_counter = message.offset
            print(
                "LOG {}: KAFKA: Consumiu {} no tópico {}".format(
                    msg_counter, msg_payload, topic.name.decode("utf-8")
                )
            )
