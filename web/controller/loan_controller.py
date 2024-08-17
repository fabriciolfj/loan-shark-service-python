import logging

from starlette import status
from starlette.requests import Request
from database.unit_of_work import UnitOfWork
from domain.create_loan import CreateLoan
from domain.loan_guid import LoanGuid
from repository.loan_repository import LoanRepository
from service.loan_service import LoanService
from web.app import app


@app.post('/api/v1/loans', status_code=status.HTTP_201_CREATED, response_model=LoanGuid)
def create_loan(request: Request, payload: CreateLoan):
    with UnitOfWork as unit:
        logging.info("receive payload %s", payload)

        repo = LoanRepository(unit.session)
        service = LoanService(repo)

        loan = CreateLoan.toLoan(payload)
        result = service.save(loan)
        unit.commit()

        logging.info("result %s", result)

    return LoanGuid(result.uuid)
