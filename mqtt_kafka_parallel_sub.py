"""
Arquivo: mqtt_kafka_parallel_sub.py
Descrição: Exemplo de kafkar producer em paralelo com a publicação mqtt
mqtt_kafka_parallel_pub é responsável por publicar em um tópico em um broker mqtt e também no kafka
e o mqtt_kafka_parallel_sub realiza o subscribe tanto no mqtt e quando no kafka consumer
Autores: Malki-çedheq Benjamim,
Inspiração: https://medium.com/python-point/mqtt-and-kafka-8e470eff606b
Criado em: 01/06/2023
Atualizado em: 19/06/2023
"""
from pykafka import KafkaClient, Topic
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


def subscribe(client: mqtt_client, topic: str):
    """
    Inscrive o cliente mqtt em um tópico
    Argumentos:
    client: instância do cliente mqtt
    topic: nome do tópico para inscrição
    """

    def on_message(client, userdata, msg):
        print(f"Recebeu `{msg.payload.decode()}` do tópico `{msg.topic}`")

    client.subscribe(topic)
    client.on_message = on_message


def connect_kafka() -> KafkaClient:
    """
    Conecta o cliente ao broker kafka
    """
    try:
        client_kafka = KafkaClient(
            hosts="{}:{}".format(env["KAFKA_BROKER"], env["KAFKA_PORT"])
        )
        print("LOG: Conectado ao Kafka com sucesso!")
        return client_kafka
    except:
        print("LOG: Falha ao conectar com Kafka")
        return None


def kafka_sync_consumer(client_kafka: KafkaClient, topico: str) -> None:
    topic = client_kafka.topics[topico]
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


def run():
    client_mqtt = connect_mqtt()  # conecta ao broker mqtt
    client_kafka = connect_kafka()  # conecta ao broker kafka

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
