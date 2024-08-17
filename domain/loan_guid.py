from pydantic.v1 import BaseModel


class LoanGuid(BaseModel):
    uuid: str