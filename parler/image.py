class ImageAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def set_profile_photo(self, *args, **kwargs):
        return self.s.post("{}/v1/profile/photo".format(self.root_url), *args, **kwargs)

    def set_profile_cover(self, *args, **kwargs):
        return self.s.post("{}/v1/profile/cover-photo".format(self.root_url), *args, **kwargs)
