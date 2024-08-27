import logging

from domain.loan import Loan


class LoanRepository:

    def __init__(self, session):
        self.session = session

    def persist(self, loan):
        try:
            self.session.add(loan)
            return loan
        except Exception as e:
            logging.error("fail save loan $s", e)

    def get_by_uuid(self, uuid):
        try:
            return self.session.query(Loan).filter_by(uuid=uuid).one()
        except Exception as e:
            logging.error("fail get loan %s", e)
            raise
