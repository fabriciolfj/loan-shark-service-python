import uuid
from datetime import date, datetime

from pydantic import BaseModel, Field
from pydantic.v1 import validator

from domain.loan import Loan


class CreateLoan(BaseModel):
    name: str = Field(min_length=1, max_length=100, )
    document: str = Field(min_length=1, max_length=100, )
    salary: float = Field(gt=0)
    birth_date: date
    loan: float = Field(gt=0)

    @validator('document')
    def document_must_not_be_empty(cls, value):
        if value is None or len(value) == '':
            raise ValueError('Document cannot be empty')
        return value

    @validator('name')
    def name_must_not_be_empty(cls, value):
        if value is None or len(value) == '':
            raise ValueError('Name cannot be empty')
        return value

    @validator('birth_date')
    def validate_birthday(cls, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Birthday date must be in format YYYY-MM-DD')
        return value

    @staticmethod
    def toLoan(create):
        loan = Loan(
            name=create.name,
            salary=create.salary,
            birthday=create.birth_date,
            loan=create.loan,
            document=create.document,
            uuid=uuid.uuid4()
        )

        return loan
