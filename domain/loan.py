from sqlalchemy import Column, String, Date, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Loan(Base):
    __tablename__ = 'loans'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    uuid = Column(String, nullable=False)
    name = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
    birthday = Column(Date, nullable=False)
    loan = Column(Float, nullable=False)
    document = Column(Float, nullable=False)
    status = Column(String, nullable=False)

    def to_dict(self):
        return {
            'uuid': str(self.uuid),
            'name': self.name,
            'salary': self.salary,
            'birthday': self.birthday.isoformat() if self.birthday else None,
            'loan': self.loan,
            'document': self.document
        }
