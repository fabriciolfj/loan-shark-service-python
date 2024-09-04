import logging

from confluent_kafka import Producer

logging.basicConfig(level=logging.DEBUG)

class KafkaProducerConfig:

    def __init__(self, kafka):
        self.producer = Producer(**kafka.config)

    def send_message(self, topic: str, value: str):
        def delivery_report(err, msg):
            if err is not None:
                logging.error('Message delivery failed: %s', err)
            else:
                logging.info('Message delivered to %s [%d]', msg.topic(), msg.partition())

        self.producer.produce(topic, value=value, callback=delivery_report)

    def close(self):
        self.producer.flush()