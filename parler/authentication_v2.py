class V2AuthenticationAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def add_phone(self, *args, **kwargs):
        return self.s.post("{}/v2/login/sms/add".format(self.root_url), *args, **kwargs)

    # email, phone, password, passwordConfirm, deviceId, notificationId (opt), deviceType (opt), ios (opt)
    def apply_for_account(self, *args, **kwargs):
        return self.s.post("{}/v2/login/apply".format(self.root_url), *args, **kwargs)

    # phone, password
    def change_add_phone(self, *args, **kwargs):
        return self.s.post("{}/v2/login/sms/change".format(self.root_url), *args, **kwargs)

    def get_a_captcha(self, *args, **kwargs):
        return self.s.post("{}/v2/login/captcha/new".format(self.root_url), *args, **kwargs)

    def get_captcha_for_email(self, *args, **kwargs):
        return self.s.post("{}/v2/login/password/reset/captcha".format(self.root_url), *args, **kwargs)

    # identifier, password, deviceId, notificationId (opt), deviceType (opt), ios (opt)
    def login_phone_or_email(self, *args, **kwargs):
        return self.s.post("{}/v2/login/new".format(self.root_url), *args, **kwargs)

    def logout(self, *args, **kwargs):
        return self.s.post("{}/v2/logout".format(self.root_url), *args, **kwargs)

    def re_request_smsopt(self, *args, **kwargs):
        return self.s.post("{}/v2/login/sms/opt/resend".format(self.root_url), *args, **kwargs)

    # identifier, captchaKey
    def reset_password_for_email(self, *args, **kwargs):
        return self.s.post("{}/v2/login/password/reset/new".format(self.root_url), *args, **kwargs)

    # identifier, doesn't work to skip phone auth
    def skip_step(self, *args, **kwargs):
        return self.s.post("{}/v2/login/skip".format(self.root_url), *args, **kwargs)

    def submit_captcha(self, *args, **kwargs):
        return self.s.post("{}/v2/login/captcha/submit".format(self.root_url), *args, **kwargs)

    def submit_phone_change(self, *args, **kwargs):
        return self.s.post("{}/v2/login/sms/change/submit".format(self.root_url), *args, **kwargs)

    def submit_smsopt(self, *args, **kwargs):
        return self.s.post("{}/v2/login/sms/otp/submit".format(self.root_url), *args, **kwargs)

    def submit_totp(self, *args, **kwargs):
        return self.s.post("{}/v2/login/totp/submit".format(self.root_url), *args, **kwargs)