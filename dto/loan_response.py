from pydantic import BaseModel


class LoanResponse(BaseModel):
    name: str
    salary: float
    loan: float

    def to_response(loan):
        return LoanResponse(name=loan.name, salary=loan.salary, loan=loan.loan)