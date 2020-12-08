class WalletAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def get_billing_information(self, *args, **kwargs):
        return self.s.get("{}/v3/billing".format(self.root_url), *args, **kwargs)