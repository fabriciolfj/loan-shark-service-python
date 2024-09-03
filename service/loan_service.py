import json
import os
import logging

from config.kafka_config import KafkaConfig
from config.kafka_producer import KafkaProducerConfig
from repository.loan_repository import LoanRepository


class LoanService:

    def __init__(self, loan_repository: LoanRepository):
        self.loan_repository = loan_repository
        self.producer = KafkaProducerConfig(KafkaConfig())

    def save_publish(self, loan):
        result = self.loan_repository.persist(loan)

        value = json.dumps(result.to_dict())
        self.producer.send_message(os.getenv("KAFKA_TOPIC"), str(value))
        logging.info("sendo message %s success", value)

        return result

    def find_by_uuid(self, uuid):
        uuid = str(uuid)
        return self.loan_repository.get_by_uuid(uuid)
