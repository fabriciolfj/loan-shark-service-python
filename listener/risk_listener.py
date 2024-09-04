import logging
import os
import asyncio
from config.kafka_config import ConsumerConfig
from config.kafka_consumer import KafkaconsumerConfig

logging.basicConfig(level=logging.DEBUG)

class RiskListener:
    def __init__(self):
        self.consumer = KafkaconsumerConfig(ConsumerConfig())
        self.consumer.subscribe([os.getenv("KAFKA_TOPIC")])
        self.running = False

    async def receive(self):
        self.running = True
        while self.running:
            try:
                msg = await asyncio.to_thread(self.consumer.poll, 2.0)
                if msg is None:
                    continue
                if msg.error():
                    logging.error("Consumer error: %s", msg.error())
                    continue

                logging.info(
                    "Received message: %s:%d:%d: key=%s value=%s",
                    msg.topic(), msg.partition(), msg.offset(), msg.key(), msg.value()
                )
            except Exception as e:
                logging.error("Error processing message: %s", e)
            await asyncio.sleep(0)  # Yield control to the event loop

    async def stop(self):
        self.running = False
        await asyncio.to_thread(self.consumer.close)