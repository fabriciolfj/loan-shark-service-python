
from pydantic import BaseModel


class LoanGuid(BaseModel):
    uuid: str