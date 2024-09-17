import json
import os
import logging

from config.kafka_config import ProducerConfig
from config.kafka_producer import KafkaProducerConfig
from repository.loan_repository import LoanRepository

logging.basicConfig(level=logging.DEBUG)

class LoanService:

    def __init__(self, loan_repository: LoanRepository):
        self.loan_repository = loan_repository
        self.producer = KafkaProducerConfig(ProducerConfig())

    def save_publish(self, loan):
        try:
            result = self.loan_repository.persist(loan)
            value = json.dumps(result.to_dict())
            self.producer.send_message(os.getenv("KAFKA_TOPIC"), str(value))
            logging.info("Message sent successfully: %s", value)
            return result
        except Exception as e:
            logging.error("Error in save_publish: %s", str(e))
            raise

    def save(self, loan):
        try:
            loan_exists = self.find_by_uuid(loan.uuid)
            if loan_exists:
                self.merge(loan_exists, loan)
            else:
                raise ValueError("Loan does not exist. Cannot persist new loan.")

            self.loan_repository.persist(loan)
        except Exception as e:
            logging.error("Error in save_publish: %s", str(e))
            raise

    def find_by_uuid(self, uuid):
        uuid = str(uuid)
        return self.loan_repository.get_by_uuid(uuid)

    def merge(self, existing_loan, new_loan_data):
        for key, value in vars(new_loan_data).items():
            if key in vars(existing_loan) and key != 'id':
                setattr(existing_loan, key, value)
        return existing_loan

    def close(self):
        self.producer.close()