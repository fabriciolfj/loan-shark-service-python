import logging


class LoanRepository:

    def __init__(self, session):
        self.session = session

    def persist(self, loan):
        try:
            return self.session.add(loan)
        except Exception as e:
            logging.error("fail save loan $s", e)
