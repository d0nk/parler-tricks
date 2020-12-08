import uuid

class AuthenticationAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def add_password_to_account(self, password, passwordConfirm):
        '''
        POST /v1/login/passwordSetup
        params:
            password
            passwordConfirm 
        response:
            400: {"message": "This person already has a password set, and can not be set through this API"}
        rate-limit: 5
        auth: yes
        '''
        return self.s.post(
            "{}/v1/login/passwordSetup".format(self.root_url), 
            data={
                'password': password,
                'passwordConfirm': passwordConfirm
            })

    def authenticate(self, email, password, captchaToken, captchaValue, deviceId=None):
        '''
        POST /v1/login
        params:
            email
            password
            captchaToken
            captchaValue
            deviceId
            deviceType - optional
            notificationId - optional
        response:
        rate-limit: 5
        auth: no
        '''
        if deviceId is None:
            deviceId = str(uuid.uuid4())

        return self.s.post(
            "{}/v1/login".format(self.root_url), 
            data={
                'email': email,
                'password': password,
                'captchaToken': captchaToken,
                'captchaValue': captchaValue,
                'deviceId': deviceId
            })

    def begin_registration_otp(self):
        '''
        GET /v1/login/otp/registration 
            returns OTP token as base64 QR code and secret
        response:
            200: {"message": "NEED_REG", "registration": "data:image/png;base64,...", "secret": "O5ZW..."}
            200: {"message": "OK"} - if already added
        rate-limit: 5
        auth: yes
        '''
        return self.s.get("{}/v1/login/otp/registration".format(self.root_url))

    def change_password(self, password, new_password):
        '''
        PATCH /v1/profile
        params:
            passwordOld
            passwordNew
            passwordConfirmation
        response:
            400: { "message": "The provided name and password provided do not match", "fieldvalidationsMap": [] }
        rate-limit: 4
        auth: yes
        '''
        return self.s.patch(
            "{}/v1/profile".format(self.root_url), 
            data={
                'passwordOld': password,
                'passwordNew': new_password,
                'passwordConfirmation': new_password
            })
    
    def checkin(self):
        '''
        GET /v1/checkin
            removed
        '''
        return self.s.get(
            "{}/v1/checkin"
        )

    def create_account(self, email, password, captchaToken, captchaValue, deviceId=None):
        '''
        POST /v1/login/register
            removed, replaced by V2 API
        params:
            email
            password
            passwordConfirm
            deviceType
            ios
            deviceId
            notificationId
            captchaToken
            captchaValue
        response:
            404: replaced by V2 Auth API
        '''
        if deviceId is None:
            deviceId = str(uuid.uuid4())

        return self.s.post(
            "{}/v1/login/register".format(self.root_url), 
            data={
                'email': email,
                'password': password,
                'passwordConfirm': password,
                'captchaToken': captchaToken,
                'captchaValue': captchaValue,
                'deviceId': deviceId
            })

    def disable_otp(self, totp):
        '''
        POST /v1/login/otp/deregistration 
        params:
            totp
        response:
            403: {"message": "Invalid OTP code provided, please try again"}
        rate-limit: 5
        auth: yes
        '''
        return self.s.post(
            "{}/v1/login/otp/deregistration".format(self.root_url), 
            data={
                'totp': totp
            })

    def email_use_status(self, email):
        '''
        GET /v1/login/{email}
        response:
            200: {"message": "HAS_PASSWORD"}
        rate-limit: 5
        auth: no
        '''
        return self.s.get(
            "{}/v1/login/{}".format(self.root_url, email)
        )

    def enroll_otp(self, totp, secret):
        '''
        POST /v1/login/otp/registration
        params:
            totp
            secret - can provide own secet
        response:
            200: {"message": "OK"}
        rate-limit: 5
        auth: yes
        '''
        return self.s.post(
            "{}/v1/login/otp/registration".format(self.root_url), 
            data={
                'totp': totp,
                'secret': secret
            })

    def get_a_captcha(self):
        '''
        GET /v1/login/captcha
            base64 png
        response:
            200: {"captchaToken": "00cd2762aeea4bc3ae93f504d739de88", "data": "/9j/2wBDAAY..."}
        rate-limit: 6
        auth: no
        '''
        return self.s.get("{}/v1/login/captcha".format(self.root_url))

    def logout(self, authenticationToken):
        '''
        POST /v1/logout 
        params: 
            authenticationToken
        auth: yes
        '''
        return self.s.post(
            "{}/v1/logout".format(self.root_url),
            data={
                'authenticationToken': authenticationToken
            }
        )

    def request_password_reset(self, email):
        '''
        POST /v1/login/resetReqeust
        params:
            email
        response:
            200: {"message": "OK"}
        rate-limit: 3
        auth: no
        '''
        return self.s.post(
            "{}/v1/login/resetRequest".format(self.root_url),
            data={
                'email': email
            }
        )

    def request_signin_link_for_email(self, email, captchaToken, captchaValue, deviceId):
        '''
        POST /v1/signin/request
            removed
        params:
            email
            deviceId
            captchaToken
            captchaValue
        response:
            404: {"message": "No resource for URL", "fieldvalidationsMap": []}}
        '''
        if deviceId is None:
            deviceId = str(uuid.uuid4())

        return self.s.post(
            "{}/v1/signin/request".format(self.root_url),
            data={
                'email': email,
                'captchaToken': captchaToken,
                'captchaValue': captchaValue,
                'deviceId': deviceId
            }
        )

    def reset_user_password(self, password, passwordConfirm, resetToken):
        '''
        POST /v2/login/password/reset/submit
        params:
            password
            passwordConfirm
            resetToken: 16 char uppercase alphanum
        response:
            400: {"message": "Verification code expired", "fieldvalidationsMap": [] }
        rate-limit: 4
        auth: no
        '''
        return self.s.post(
            "{}/v2/login/password/reset/submit".format(self.root_url),
            data = {
                'password': password,
                'passwordConfirm': passwordConfirm,
                'resetToken': resetToken
            }
        )

    def send_email_reminder(self, username):
        '''
        POST /v1/login/reminder
            sends email reminder for username
        params:
            username
        response:
            200: {"message": "success"}
        rate-limit: 15
        auth: no
        '''
        return self.s.post(
            "{}/v1/login/reminder".format(self.root_url),
            data={
                'username': username
            }
        )

    def send_notification_token(self, notificationId):
        '''
        POST /v1/notification
            Mobile push notification token
        params:
            notificationId
        response:
            200: {"message": "success"}
        rate-limit: 5
        auth: yes
        '''
        return self.s.post(
            "{}/v1/notification".format(self.root_url),
            data = {
                'notificationId': notificationId
            }
        )

    def sign_in_with_email(self, email, code, deviceId=None):
        '''
        POST /v1/signin
            sign in using code sent to email. removed
        params:
            email
            code
            deviceType
            deviceId
            ios
            notificationId
        response:
            404: { "message": "No resource for URL", "fieldvalidationsMap": [] }
        '''
        if deviceId is None:
            deviceId = str(uuid.uuid4())

        return self.s.post(
            "{}/v1/signin".format(self.root_url),
            data={
                'deviceId': deviceId,
                'email': email,
                'code': code
            }
        )

    def sign_up_email(self, email, name, deviceId=None):
        '''
        POST /v1/signup 
            removed
        params:
            email
            name
            deviceId
        response:
            404: { "message": "No resource for URL", "fieldvalidationsMap": [] }
        '''
        if deviceId is None:
            deviceId = str(uuid.uuid4())

        return self.s.post(
            "{}/v1/signup".format(self.root_url),
            data={
                'deviceId': deviceId,
                'email': email,
                'name': name
            }
        )

    def verify_reset_code(self, token):
        '''
        POST /v2/login/password/reset/verify
        params:
            email (optional)
            token 16 char uppercase alphanum
        response:
            400: {"message": "The provided password reset code is invalid", "fieldvalidationsMap": []}
            200: {"valid": true}
        rate-limit: 4
        auth: no
        '''
        return self.s.post(
            "{}/v2/login/password/reset/verify".format(self.root_url),
            data={
                'token': token,
            }
        )
    
