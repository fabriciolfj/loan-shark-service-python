import logging
from fastapi import HTTPException

from starlette import status
from database.unit_of_work import UnitOfWork
from domain.create_loan import CreateLoan
from domain.loan_guid import LoanGuid
from repository.loan_repository import LoanRepository
from service.loan_service import LoanService
from web.app import app


@app.post("/api/v1/loans", status_code=status.HTTP_201_CREATED, response_model=LoanGuid)
def create_loan(payload: CreateLoan):
    try:
        with UnitOfWork as unit:
            logging.info("receive payload %s", payload)

            repo = LoanRepository(unit.session)
            service = LoanService(repo)

            loan = CreateLoan.toLoan(payload)
            loan = service.save(loan)
            logging.info("result %s", loan)

            result = LoanGuid
            result.uuid = loan.uuid

            unit.commit()

        return result
    except Exception as e:
        logging.error(e)
        raise HTTPException(
            status_code=400, detail=f'fail save loan'
        )