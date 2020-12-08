class WalletGeneralAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def internal_transfer_funds(self, *args, **kwargs):
        return self.s.post("{}/v3/wallet/transfer".format(self.root_url), *args, **kwargs)

    def load_billing_user(self, *args, **kwargs):
        return self.s.get("{}/v3/billing".format(self.root_url), *args, **kwargs)

    def set_tipping_enabled(self, *args, **kwargs):
        return self.s.post("{}/v3/billing/tipping".format(self.root_url), *args, **kwargs)

    def submit_new_billing_address(self, *args, **kwargs):
        return self.s.post("{}/v3/billing/address".format(self.root_url), *args, **kwargs)

    def submit_w9_with_file(self, *args, **kwargs):
        return self.s.post("{}/v3/billing/w9".format(self.root_url), *args, **kwargs)
