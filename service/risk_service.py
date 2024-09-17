import logging
from client.customer.customer_client import CustomerClient
from database.unit_of_work import UnitOfWork
from domain.status import Status, status
from repository.loan_repository import LoanRepository
from service.loan_service import LoanService


class RiskService:

    def __init__(self):
        self.loan_service = None
        self.customer_client = CustomerClient()

    def update_loan(self, loan):
        try:
            with UnitOfWork() as unit:
                repo = LoanRepository(unit.session)
                self.loan_service = LoanService(repo)

                customer = self.customer_client.get_data(loan.document)

                if loan.loan > customer.others_loan:
                    loan.status = Status.APPROVED.value
                else:
                    loan.status = status.REJECTED.value

                self.loan_service.save(loan)
                unit.commit()
        except Exception as e:
            logging.error(f"Failed to analyze risk. Details: {e}")
            raise
