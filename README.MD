# Introdução ao Kafka

[Apache Kafka: 10 essential terms and concepts explained](https://www.redhat.com/en/blog/apache-kafka-10-essential-terms-and-concepts-explained)

[Kafka Official Documentation](https://kafka.apache.org/documentation/)

# Acessando o Repositório

[Repo no GitHub](https://github.com/malki-cedheq/python_mqtt_kafka)

> Clonando o repositório do github via http

`git clone https://github.com/malki-cedheq/python_mqtt_kafka.git`

> Clonando o repositório do github via ssh

`git clone git@github.com:malki-cedheq/python_mqtt_kafka.git`

> Clonando o repositório do github via GitHub CLI

`gh repo clone malki-cedheq/python_mqtt_kafka`

> Atualizando o repositório local

`git pull`

# Requisitos

## Criação de arquivo .env no diretório raiz

```
MQTT_USERNAME=
MQTT_PASSWORD=
MQTT_PORT=
MQTT_BROKER=

KAFKA_USERNAME=
KAFKA_PASSWORD=
KAFKA_PORT=
KAFKA_BROKER=
```

# Utilizando o ambiente

## Requisitos

> [Docker](https://www.docker.com/)

> [Python ^3.10](https://www.python.org/)

> [Poetry](https://python-poetry.org/)

## Executando serviços com Docker

### Criando imagem Docker

No diretório raiz executar:

`docker build --tag mqtt_kafka --file Dockerfile.consumer .`

### Criando ambiente Docker mqtt+kafka

`docker compose -f docker-compose.yml up -d`

## Instalação das dependências

`poetry install`

## Executando aplicações

`poetry run python3 arquivo.py`

# Referências externas

\*SUBSTITUIR |ZOOKEEPER POR KRAF

Apache Kafka packaged by Bitnami

    https://hub.docker.com/r/bitnami/kafka

Monitoring Kafka

    https://hub.docker.com/r/obsidiandynamics/kafdrop

Python pyKafka an paho.MQTT - Integrate Kafka and MQTT - How to connect MQTT and Kafka

    https://www.youtube.com/watch?v=FDCTQ47oXUg
    https://medium.com/python-point/mqtt-and-kafka-8e470eff606b

Passo a passo

1. Docker compose Kafkar + Zookeeper + KafDrop

   1. https://www.youtube.com/watch?v=EV3KiPgE760

   2. https://www.youtube.com/watch?v=8aUZ1J7r8hM

2. Criando consumers e producers em Python

   https://www.youtube.com/watch?v=yT-GYVssdEg

PROMETHEUS

    https://www.confluent.io/ko-kr/blog/monitor-kafka-clusters-with-prometheus-grafana-and-confluent/

    https://www.metricfire.com/blog/kafka-monitoring/

    https://medium.com/@alvarobacelar/monitorando-um-cluster-kafka-com-ferramentas-open-source-a4032836dc79

    https://sridharan-rg.medium.com/kafka-metrics-monitoring-with-prometheus-15b0aebea16b

    https://computingforgeeks.com/monitor-apache-kafka-with-prometheus-and-grafana/

Which Metrics to Monitor in Kafka?

    https://www.youtube.com/watch?v=XXLe0KNEbR4

Setting up Kafka on Prometheus Tutorial

    https://www.youtube.com/watch?v=hL82UnQMnGM
