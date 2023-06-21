"""
Arquivo: functions_mqtt.py
Descrição: Acervo de funções para interação com mqtt
Autores: Malki-çedheq Benjamim,
Criado em: 21/06/2023
Atualizado em: 21/06/2023
"""

import paho.mqtt.client as mqtt_client


def connect_mqtt(
    mqtt_broker: str,
    mqtt_port: int,
    client_id: str,
    mqtt_protocol: str,
    mqtt_username: str,
    mqtt_password: str,
) -> mqtt_client:
    """
    Conecta o cliente mqtt ao BROKER mqtt
    """

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("LOG: Conectado ao BROKER MQTT com sucesso!")
        else:
            print("LOG: Falha ao conectar, STATUS CODE %d\n", rc)

    client = mqtt_client.Client(client_id, transport=mqtt_protocol)
    client.username_pw_set(mqtt_username, mqtt_password)
    client.on_connect = on_connect
    client.connect(mqtt_broker, mqtt_port)
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
