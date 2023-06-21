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

# Utilizando o ambiente

## Requisitos

> [Docker](https://www.docker.com/)

> [Python ^3.10](https://www.python.org/)

> [Poetry](https://python-poetry.org/)

### Criação de arquivo .env no diretório raiz

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

## Executando serviços com Docker

### Criando ambiente Docker mqtt+kafka

`docker compose -f docker-compose.yml up -d`

#### Interagindo via shell com o mqtt Docker

`docker exec -it mosquitto_container sh`

#### Criando um usuário autenticado via shell

`mosquitto_passwd -c /mosquitto/config/password.txt nome_usuario`

## Instalação das dependências

`poetry install`

## Executando aplicações

`poetry run python3 arquivo.py`

# Scripts Exemplo

## KAFKA (producer + consumer)

1. kafka_producer.py realiza produz mensagens em um tópico do broker do cluster KAFKA.
2. mqtt_kafka_bridge_sub.py consome mensagens de um tópico do broker do cluster KAFKA.

## MQTT + KAFKA (modo paralelo)

1. mqtt_kafka_parallel_pub.py realiza publicação de uma mensagem em um tópico do broker MQTT e produz a mesma mensagem no tópico de mesmo nome do broker do cluster KAFKA.
2. mqtt_kafka_parallel_sub.py realiza subscrição em um tópico do broker MQTT, e consome as mensagens que são produzidas no mesmo tópico do broker do cluster KAFKA.

## MQTT + KAFKA (modo serial)

1. mqtt_kafka_bridge_pub.py realiza publicação em um tópico do broker MQTT
2. mqtt_kafka_bridge_sub.py realiza subscrição em um tópico do broker MQTT, e ao receber uma nova mensagem no referido tópico encaminha esta mensagem, produz, no mesmo tópico do broker do cluster KAFKA.

# Referências externas

\*SUBSTITUIR |ZOOKEEPER POR KRAF

## Apache Kafka packaged by Bitnami

`https://hub.docker.com/r/bitnami/kafka`

## Monitoring Kafka

`https://hub.docker.com/r/obsidiandynamics/kafdrop`

## Python pyKafka an paho.MQTT - Integrate Kafka and MQTT - How to connect MQTT and Kafka

```
https://www.youtube.com/watch?v=FDCTQ47oXUg

https://medium.com/python-point/mqtt-and-kafka-8e470eff606b
```

## Vídeos

1. Docker compose Kafkar + Zookeeper + KafDrop

   1. `https://www.youtube.com/watch?v=EV3KiPgE760`

   2. `https://www.youtube.com/watch?v=8aUZ1J7r8hM`

2. Criando consumers e producers em Python

   `https://www.youtube.com/watch?v=yT-GYVssdEg`

## PROMETHEUS

```
https://www.confluent.io/ko-kr/blog/monitor-kafka-clusters-with-prometheus-grafana-and-confluent/

https://www.metricfire.com/blog/kafka-monitoring/

https://medium.com/@alvarobacelar/monitorando-um-cluster-kafka-com-ferramentas-open-source-a4032836dc79

https://sridharan-rg.medium.com/kafka-metrics-monitoring-with-prometheus-15b0aebea16b

https://computingforgeeks.com/monitor-apache-kafka-with-prometheus-and-grafana/
```

### Which Metrics to Monitor in Kafka?

`https://www.youtube.com/watch?v=XXLe0KNEbR4`

### Setting up Kafka on Prometheus Tutorial

`https://www.youtube.com/watch?v=hL82UnQMnGM`

## STEPS

```
http://www.liferaysavvy.com/2021/07/kafka-monitoring-with-prometheus.html

https://www.metricfire.com/blog/kafka-monitoring/
```

## Requeriments JAVA >= 7 (java -version)

```
sudo apt update
sudo apt install default-jre
java -version
sudo apt install default-jdk
javac -version
```

## Download agent e config

```
cd /home/$USER
mkdir prometheus
cd prometheus
```

## FAZER DOWNLOAD DO RAW PARA EVITAR ERROS

### github do prometheus jmx exporter

`https://github.com/prometheus/jmx_exporter`

#### configuração do zookeeper

`https://github.com/prometheus/jmx_exporter/blob/main/example_configs/zookeeper.yaml`

#### configuração do kafka 2.0.0

`https://github.com/prometheus/jmx_exporter/blob/main/example_configs/kafka-2_0_0.yml`

#### configuração do kafka 0.8.2

`https://github.com/prometheus/jmx_exporter/blob/main/example_configs/kafka-0-8-2.yml`

#### links dos agents

> https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/

`https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.18.0/jmx_prometheus_javaagent-0.18.0.jar`

# alterar kafka env KAFK_OPTS

`KAFKA_OPTS="-javaagent:/prometheus/jmx_prometheus_javaagent-0.18.0.jar=$PROMETHEUS_PORT:/prometheus/kafka_broker.yml"`

# configuração do prometheus

`https://github.com/LiferaySavvy/kafka-monitoring/blob/master/prometheus.yml`
