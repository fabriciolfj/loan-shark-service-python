from confluent_kafka import Producer

class KafkaProducerConfig:

    def __init__(self, kafka):
        self.producer = Producer(**kafka.config)

    def send_message(self, topic: str, value: str):
        self.producer.produce(topic, value=value)
        self.producer.flush()