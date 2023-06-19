"""
Arquivo: mqtt_kafka_bridge_sub.py
Descrição: Exemplo de kafkar producer em brigde
mqtt_kafka_bridge_pub é responsável por publicar em um tópico em um broker mqtt
e o mqtt_kafka_bridge_sub realiza o bridge entre o subscriber mqtt e kafka producer
Autores: Malki-çedheq Benjamim,
Inspiração: https://medium.com/python-point/mqtt-and-kafka-8e470eff606b
Criado em: 01/06/2023
Atualizado em: 19/06/2023
"""

from pykafka import KafkaClient, Producer
import paho.mqtt.client as mqtt_client
import uuid
from datetime import datetime
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

KAFKA_BROKER = env["KAFKA_BROKER"]
KAFKA_PORT = int(env["KAFKA_PORT"])
KAFKA_USERNAME = env["KAFKA_USERNAME"]
KAFKA_PASSWORD = env["KAFKA_PASSWORD"]


def connect_mqtt() -> mqtt_client:
    """
    Conecta o cliente mqtt ao BROKER mqtt
    """

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("LOG: Conectado ao BROKER MQTT com sucesso!")
        else:
            print("LOG: Falha ao conectar, STATUS CODE %d\n", rc)

    client = mqtt_client.Client(CLIENT_ID, transport=MQTT_PROTOCOL)
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    client.on_connect = on_connect
    client.connect(MQTT_BROKER, MQTT_PORT)
    return client


def subscribe(client: mqtt_client, topic: str, kafka_producer: tuple([Producer, str])):
    """
    Inscreve o cliente mqtt em um tópico
    Argumentos:
    client: instância do cliente mqtt
    topic: nome do tópico para inscrição
    """

    def on_message(client, userdata, msg):
        print(f"Recebeu `{msg.payload.decode()}` do tópico `{msg.topic}`")
        kafka_producer_produce(
            kafka_producer[0], kafka_producer[1], msg.payload.decode()
        )

    client.subscribe(topic)
    client.on_message = on_message


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
    producer.produce(msg_payload.encode("ascii"))
    print("LOG: KAFKA: Publicou {} no tópico {}".format(msg_payload, topic))


def run():
    client_mqtt = connect_mqtt()  # conecta ao broker mqtt
    client_kafka = connect_kafka()  # conecta ao broker kafka

    if client_mqtt and client_kafka:
        # Sincroniza o produzir com um tópico no kafka
        kafka_producer = kafka_sync_producer(client_kafka, "contador")

        # Inscrições nos tópicos mqtt e bridge kafka
        subscribe(client_mqtt, "contador", kafka_producer)

        # O método bloqueia o programa, é útil quando o programa deve ser executado indefinidamente
        client_mqtt.loop_forever()
    else:
        print("LOG: Não conectou ao mqtt ou kafka.")


if __name__ == "__main__":
    run()
