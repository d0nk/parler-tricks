class ParlerDataAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def upload_data(self, *args, **kwargs):
        return self.s.post("{}/v2/upload/image".format(self.root_url), *args, **kwargs)