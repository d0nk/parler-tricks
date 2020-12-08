class FollowAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    # id
    def approve_follower_request(self, *args, **kwargs):
        return self.s.post("{}/v1/follow/followers/pending/approve".format(self.root_url), *args, **kwargs)

    # id
    def deny_follower_request(self, *args, **kwargs):
        return self.s.post("{}/v1/follow/followers/pending/deny".format(self.root_url), *args, **kwargs)

    # id
    def follow_user(self, *args, **kwargs):
        return self.s.post("{}/v1/follow".format(self.root_url), *args, **kwargs)

    # startkey
    def get_pending_follower_requests(self, *args, **kwargs):
        return self.s.get("{}/v1/follow/followers/pending".format(self.root_url), *args, **kwargs)

    def pending_count(self, *args, **kwargs):
        return self.s.get("{}/v1/follow/followers/pending/count".format(self.root_url), *args, **kwargs)

    # id, enabled = 1
    def subscribe_to_user(self, *args, **kwargs):
        return self.s.post("{}/v1/follow/following/subscribed".format(self.root_url), *args, **kwargs)

    # id
    def unfollow_user(self, *args, **kwargs):
        return self.s.delete("{}/v1/follow".format(self.root_url), *args, **kwargs)

    # id. enabled = 0
    def unsubscribe_from_user(self, *args, **kwargs):
        return self.s.post("{}/v1/follow/following/subscribed".format(self.root_url), *args, **kwargs)
