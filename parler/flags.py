class FlagsAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def get_flags_for(self, userUuid, *args, **kwargs):
        # i have no idea what this is
        return self.s.get("{}/v3/flags/user/uuid/{}".format(self.root_url, userUuid), *args, **kwargs)
 