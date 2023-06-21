"""
Arquivo: variables.py
Descrição: Variáveis ambiente e constantes compartilháveis
Autores: Malki-çedheq Benjamim,
Criado em: 21/06/2023
Atualizado em: 21/06/2023
"""

from dotenv import dotenv_values

env = dotenv_values(".env")

MQTT_BROKER = env["MQTT_BROKER"]
MQTT_PORT = int(env["MQTT_PORT"])
MQTT_USERNAME = env["MQTT_USERNAME"]
MQTT_PASSWORD = env["MQTT_PASSWORD"]
MQTT_PROTOCOL = "tcp"  # tcp / websockets

KAFKA_BROKER = env["KAFKA_BROKER"]
KAFKA_PORT = int(env["KAFKA_PORT"])
KAFKA_USERNAME = env["KAFKA_USERNAME"]
KAFKA_PASSWORD = env["KAFKA_PASSWORD"]
