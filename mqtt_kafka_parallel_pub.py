"""
Arquivo: mqtt_kafka_parallel_pub.py
Descrição: Exemplo de kafkar producer em paralelo com a publicação mqtt
mqtt_kafka_parallel_pub é responsável por publicar em um tópico em um broker mqtt e também no kafka
e o mqtt_kafka_parallel_sub realiza o subscribe tanto no mqtt e quando no kafka consumer
Autores: Malki-çedheq Benjamim,
Inspiração: https://medium.com/python-point/mqtt-and-kafka-8e470eff606b
Criado em: 01/06/2023
Atualizado em: 19/06/2023
"""

import uuid
import time
from datetime import datetime
from paho.mqtt import client as mqtt_client
from pykafka import KafkaClient
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


def mqtt_publish(client, topic: str, msg: str):
    """
    O cliente mqtt publica em um tópico no broker
    Argumentos:
    client: instância do cliente mqtt
    topic: nome do tópico para publicação
    msg: string a ser publicada
    """
    result = client.publish(topic, msg)
    status = result[0]  # result: [0, 1]
    if status == 0:
        return f"Enviado `{msg}` ao tópico `{topic}`"
    return f"Falha ao enviar mensagem ao tópico {topic}"


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


def kafka_publish(client_kafka, topic: str, msg: str):
    """
    O cliente mqtt publica em um tópico no broker
    Argumentos:
    client: instância do cliente mqtt
    topic: nome do tópico para publicação
    msg: string a ser publicada
    """
    kafka_topic = client_kafka.topics[str(topic)]
    kafka_producer = kafka_topic.get_sync_producer()
    kafka_producer.produce(str(msg).encode("ascii"))
    return "LOG: KAFKA: Publicou {} no tópico {}".format(msg, topic)


def run():
    client_mqtt = connect_mqtt()  # conecta ao broker

    client_kafka = connect_kafka()  # conecta ao broker

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
            result_kafka = kafka_publish(client_kafka, topic=topico, msg=msg)
            print(result_mqtt)
            print(result_kafka)
            msg_count += 1
    else:
        print("LOG: Não conectou ao mqtt ou kafka.")


if __name__ == "__main__":
    run()
