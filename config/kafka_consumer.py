from confluent_kafka import Consumer


class KafkaConsumerConfig:

    def __init__(self, kafka):
        self.consumer = Consumer(**kafka.config)

    def subscribe(self, topic: str):
        self.consumer.subscribe([topic])       \

    def poll(self, timeout: float):
        return self.consumer.poll(timeout)

    def close(self):
        self.consumer.close()