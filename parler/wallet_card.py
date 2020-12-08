class WalletCardAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def create_payment_method_from_data(self, *args, **kwargs):
        return self.s.post("{}/v3/wallet/card/new".format(self.root_url), *args, **kwargs)

    def delete_payment_method(self, method, *args, **kwargs):
        return self.s.delete("{}/v3/wallet/card/{}".format(self.root_url, method), *args, **kwargs)

    def load_details_for_payment_method(self, method, *args, **kwargs):
        return self.s.get("{}/v3/wallet/card/{}".format(self.root_url, method), *args, **kwargs)

    def load_list_of_payment_methods(self, *args, **kwargs):
        return self.s.get("{}/v3/wallet/card".format(self.root_url), *args, **kwargs)
