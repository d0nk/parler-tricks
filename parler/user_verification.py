class UserVerificationAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def get_user_verification_list(self, *args, **kwargs):
        return self.s.get("{}/v3/userVerifications".format(self.root_url), *args, **kwargs)

    def get_user_verification_status_details(self, verification, *args, **kwargs):
        return self.s.get("{}/v3/userVerification/{}".format(self.root_url, verification), *args, **kwargs)

    def get_user_verification_status(self, *args, **kwargs):
        return self.s.get("{}/v3/userVerification".format(self.root_url), *args, **kwargs)

    def submit_user_verification_status(self, *args, **kwargs):
        return self.s.post("{}/v3/userVerification".format(self.root_url), *args, **kwargs)
