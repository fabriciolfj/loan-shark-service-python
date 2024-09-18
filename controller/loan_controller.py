import io
import logging
import pandas as pd
from fastapi import HTTPException, UploadFile, File

from starlette import status

from app import app
from database.unit_of_work import UnitOfWork
from dto.create_loan import CreateLoan
from dto.loan_guid import LoanGuid
from dto.loan_response import LoanResponse
from repository.loan_repository import LoanRepository
from service.loan_service import LoanService


@app.post("/api/v1/loans", status_code=status.HTTP_201_CREATED, response_model=LoanGuid)
def create_loan(payload: CreateLoan):
    try:
        with UnitOfWork() as unit:
            logging.info("receive payload %s", payload)

            repo = LoanRepository(unit.session)
            service = LoanService(repo)

            loan = CreateLoan.toLoan(payload)
            loan = service.save_publish(loan)
            logging.info("result %s", loan)

            result = LoanGuid(uuid=str(loan.uuid))

            unit.commit()
            service.close()
        return result
    except Exception as e:
        logging.error(e)
        raise HTTPException(
            status_code=400, detail=f'fail save loan'
        )


@app.get("/api/v1/loans/{uuid}", status_code=status.HTTP_200_OK, response_model=LoanResponse)
def get_loan(uuid: str):
    try:
        with UnitOfWork() as unit:
            repo = LoanRepository(unit.session)
            service = LoanService(repo)

            result = service.find_by_uuid(uuid)

            return LoanResponse.to_response(result)
    except Exception:
        raise HTTPException(
            status_code=400, detail=f'fail get loan ${uuid}'
        )

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    if file.content_type == 'text/csv':
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))
        return {"filename": file.filename, "content": df.to_json()}
    else:
        return {"error": "O arquivo enviado não é um CSV"}