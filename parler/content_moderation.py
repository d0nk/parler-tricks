class ContentModerationAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def get_reported_content(self, *args, **kwargs):
        return self.s.get("{}/v2/contentModeration/reports".format(self.root_url), *args, **kwargs)