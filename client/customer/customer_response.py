from dataclasses import dataclass


@dataclass
class CustomerResponse:
    date_request: str
    others_loan: float