from enum import Enum


class Status(Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    PENDING = "pending"


for status in Status:
    print(f"Status: {status.name}, Value: {status.value}")
