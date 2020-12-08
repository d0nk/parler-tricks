class FeedAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    # startKey, followingOnly, hideEchoes, onlySubscribed
    def get_feed(self, *args, **kwargs):
        return self.s.get("{}/v1/feed".format(self.root_url), *args, **kwargs)

    # id, startKey
    def get_media_content_for_user(self, *args, **kwargs):
        return self.s.get("{}/v1/post/creator/media".format(self.root_url), *args, **kwargs)

    # tag, startKey
    def get_posts_for_hashtag(self, *args, **kwargs):
        return self.s.get("{}/v1/post/hashtag".format(self.root_url), *args, **kwargs)

    # id, startKey
    def get_users_comments(self, *args, **kwargs):
        return self.s.get("{}/v1/comment/creator".format(self.root_url), *args, **kwargs)

    # id, startKey
    def get_users_feed(self, *args, **kwargs):
        return self.s.get("{}/v1/post/creator".format(self.root_url), *args, **kwargs)

    # id, startKey
    def get_users_likes(self, *args, **kwargs):
        return self.s.get("{}/v1/post/creator/liked".format(self.root_url), *args, **kwargs)

    # id, startKey
    def get_users_news(self, *args, **kwargs):
        return self.s.get("{}/v1/post/creator/media".format(self.root_url), *args, **kwargs)

    def integration_partner_feed(self, *args, **kwargs):
        return self.s.get("{}/v1/post/integration".format(self.root_url), *args, **kwargs)

    # startkey, limit
    def news_feed(self, *args, **kwargs):
        return self.s.get("{}/v1/news".format(self.root_url), *args, **kwargs)
