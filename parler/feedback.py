class FeedbackAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def submit_feedback(self, *args, **kwargs):
        return self.s.post("{}/v3/feedback".format(self.root_url), *args, **kwargs)
