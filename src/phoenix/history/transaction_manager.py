from phoenix.history.transaction_repository import TransactionRepository


class TransactionManager:

    def __init__(self, folder="history"):

        self.repository = TransactionRepository(folder)
        self.folder = self.repository.folder

    def create_id(self):

        return self.repository.create_id()

    def save(self, results):

        return self.repository.save(results)
