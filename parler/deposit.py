class DepositAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def execute_deposit(self, identifier, *args, **kwargs):
        return self.s.put("{}/v3/wallet/deposit/{}".format(self.root_url, identifier), *args, **kwargs)

    def load_deposits_list(self, *args, **kwargs):
        return self.s.get("{}/v3/wallet/deposits".format(self.root_url), *args, **kwargs)

    def load_details_for_deposit(self, identifier, *args, **kwargs):
        return self.s.get("{}/v3/wallet/deposit/{}".format(self.root_url, identifier), *args, **kwargs)

    def make_cancelled_deposit(self, identifier, *args, **kwargs):
        return self.s.delete("{}/v3/wallet/deposit/{}".format(self.root_url, identifier), *args, **kwargs)

    def send_iap_receipt(self, *args, **kwargs):
        return self.s.post("{}/v3/wallet/iap/ios".format(self.root_url), *args, **kwargs)

    def set_amount_for_deposit(self, identifier, *args, **kwargs):
        return self.s.post("{}/v3/wallet/deposit/{}".format(self.root_url, identifier), *args, **kwargs)

    def start_deposit_with_data(self, *args, **kwargs):
        return self.s.post("{}/v3/wallet/deposit".format(self.root_url), *args, **kwargs)
