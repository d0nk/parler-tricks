class TransactionAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def load_details_for_transaction(self, transaction, *args, **kwargs):
        return self.s.get("{}/v3/wallet/transaction/{}".format(self.root_url, transaction), *args, **kwargs)

    def load_list_of_transactions(self, *args, **kwargs):
        return self.s.get("{}/v3/wallet/transactions".format(self.root_url), *args, **kwargs)
