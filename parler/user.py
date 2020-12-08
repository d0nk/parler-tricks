class UserAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    # message
    def ban_user(self, user, *args, **kwargs):
        return self.s.post("{}/v2/iaa/user/{}/ban".format(self.root_url, user), *args, **kwargs)

    # password
    def delete_account_with_password(self, *args, **kwargs):
        return self.s.post("{}/v2/profile/delete".format(self.root_url), *args, **kwargs)

    def get_integration_partners(self, *args, **kwargs):
        return self.s.get("{}/v1/users/integrations".format(self.root_url), *args, **kwargs)

    def get_rss_partners(self, *args, **kwargs):
        return self.s.get("{}/v1/users/rss".format(self.root_url), *args, **kwargs)

    def get_user_verification_status(self, *args, **kwargs):
        return self.s.get("{}/v1/identity/status".format(self.root_url), *args, **kwargs)

    # front, back, selfOpen, selfClosed, barcodeText
    def verify_user(self, *args, **kwargs):
        return self.s.post("{}/v1/identity/submit".format(self.root_url), *args, **kwargs)

    # id, userId
    def block_user(self, *args, **kwargs):
        return self.s.post("{}/v1/user/block".format(self.root_url), *args, **kwargs)

    # accountColor
    def change_profile_color_theme(self, *args, **kwargs):
        return self.s.patch("{}/v1/profile".format(self.root_url), *args, **kwargs)

    # username
    def does_username_exist(self, *args, **kwargs):
        return self.s.get("{}/v1/user/exists".format(self.root_url), *args, **kwargs)

    # limit, startkey
    def get_blocked_users(self, *args, **kwargs):
        return self.s.get("{}/v1/user/block".format(self.root_url), *args, **kwargs)

    # id, startkey
    def get_followers_for_user_id(self, *args, **kwargs):
        return self.s.get("{}/v1/follow/followers".format(self.root_url), *args, **kwargs)

    # id, startkey
    def get_following_for_user_id(self, *args, **kwargs):
        return self.s.get("{}/v1/follow/following".format(self.root_url), *args, **kwargs)

    def get_muted_users(self, *args, **kwargs):
        return self.s.get("{}/v1/user/mute".format(self.root_url), *args, **kwargs)

    # id
    def get_profile_for_user(self, *args, **kwargs):
        return self.s.get("{}/v1/profile".format(self.root_url), *args, **kwargs)

    # id
    def get_profile_for_username(self, *args, **kwargs):
        return self.s.get("{}/v1/profile".format(self.root_url), *args, **kwargs)

    # startkey
    def get_subscribed(self, *args, **kwargs):
        return self.s.get("{}/v1/follow/following/subscribed".format(self.root_url), *args, **kwargs)

    # id, startkey
    def get_unfollowing(self, *args, **kwargs):
        return self.s.get("{}/v1/recommend/unfollow".format(self.root_url), *args, **kwargs)

    # id, userId, username
    def mute_user(self, *args, **kwargs):
        return self.s.post("{}/v1/user/mute".format(self.root_url), *args, **kwargs)

    def patch_profile(self, *args, **kwargs):
        return self.s.patch("{}/v1/profile".format(self.root_url), *args, **kwargs)

    # id, reason
    def report_object(self, *args, **kwargs):
        return self.s.post("{}/v1/user/report".format(self.root_url), *args, **kwargs)

    # id, userId, username
    def unblock_user(self, *args, **kwargs):
        return self.s.delete("{}/v1/user/block".format(self.root_url), *args, **kwargs)

    # id, userId, username
    def unmute_user(self, *args, **kwargs):
        return self.s.delete("{}/v1/user/mute".format(self.root_url), *args, **kwargs)