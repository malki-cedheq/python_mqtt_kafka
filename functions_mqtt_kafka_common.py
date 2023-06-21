"""
Arquivo: functions_mqtt_kafka_common.py
Descrição: Acervo de funções para interação entre mqtt e kafka
Autores: Malki-çedheq Benjamim,
Criado em: 21/06/2023
Atualizado em: 21/06/2023
"""

from functions_mqtt import mqtt_client
from functions_kafka import kafka_producer_produce, Producer


def subscribe_and_produce(
    client: mqtt_client, topic: str, kafka_producer: tuple([Producer, str])
):
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
