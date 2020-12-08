class TippingAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def set_tips_with_id(self, *args, **kwargs):
        return self.s.post("{}/v3/tip".format(self.root_url), *args, **kwargs)
