class SearchAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    # search, startkey, domain (optional)
    def search_for_news(self, *args, **kwargs):
        return self.s.get("{}/v1/news/search".format(self.root_url), *args, **kwargs)

    # tag, startkey
    def search_for_posts_with_hashtag(self, *args, **kwargs):
        return self.s.get("{}/v1/post/hashtag".format(self.root_url), *args, **kwargs)

    # search, startkey
    def search_for_users(self, *args, **kwargs):
        return self.s.get("{}/v1/users".format(self.root_url), *args, **kwargs)

    # search, startkey
    def search_hashtags(self, *args, **kwargs):
        return self.s.get("{}/v1/hashtag".format(self.root_url), *args, **kwargs)
