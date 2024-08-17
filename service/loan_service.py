class LoanService:

    def __init__(self, loan_repository):
        self.loan_repository = loan_repository

    def save(self, loan):
        return self.loan_repository.persist(loan)
