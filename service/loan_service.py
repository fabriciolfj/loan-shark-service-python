from sqlalchemy import UUID

from repository.loan_repository import LoanRepository


class LoanService:

    def __init__(self, loan_repository: LoanRepository):
        self.loan_repository = loan_repository

    def save(self, loan):
        return self.loan_repository.persist(loan)

    def find_by_uuid(self, uuid):
        uuid = str(uuid)
        return self.loan_repository.get_by_uuid(uuid)
