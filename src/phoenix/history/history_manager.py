from phoenix.history.transaction_repository import (
    HistoryTransaction,
    TransactionRepository,
)


class HistoryManager:

    def __init__(self, folder="history"):

        self.repository = TransactionRepository(folder)
        self.folder = self.repository.folder

    def save(self, results):

        return self.repository.save(results)

    def list(self):

        return self.repository.list()

    def load(self, transaction_id):

        return self.repository.load(transaction_id)
