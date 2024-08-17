import uuid

from sqlalchemy import Column, String, UUID, Date, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Loan(Base):
    __tablename__ = 'loans'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
    birthday = Column(Date, nullable=False)
    loan = Column(Float, nullable=False)
    document = Column(Float, nullable=False)
