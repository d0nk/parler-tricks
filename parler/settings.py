class SettingsAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def get_security_settings(self, *args, **kwargs):
        return self.s.get("{}/v1/profile/settings/security".format(self.root_url), *args, **kwargs)

    def get_settings(self, *args, **kwargs):
        return self.s.get("{}/v1/profile/settings".format(self.root_url), *args, **kwargs)

    def get_verification_page_data(self, *args, **kwargs):
        return self.s.get("{}/v1/profile/verify/form".format(self.root_url), *args, **kwargs)

    def patch_setting(self, *args, **kwargs):
        return self.s.post("{}/v1/profile/settings".format(self.root_url), *args, **kwargs)

    # badge
    def set_primary_badge(self, *args, **kwargs):
        return self.s.post("{}/v1/profile/badge/display".format(self.root_url), *args, **kwargs)
