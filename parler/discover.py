class DiscoverAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def add_post_to_discover_page(self, postId, *args, **kwargs):
        return self.s.post("{}/v1/discover/posts/{}/add".format(self.root_url, postId), *args, **kwargs)

    # limit, startKey
    def get_discover_hashtags(self, *args, **kwargs):
        # app has this bug too :)
        return self.s.get("{}/v1/discover/hashtags".format(self.root_url), *args, **kwargs)

    # limit, startKey
    def get_discover_news(self, *args, **kwargs):
        return self.s.get("{}/v1/discover/news".format(self.root_url), *args, **kwargs)

    # limit, startKey
    def get_discover_posts(self, *args, **kwargs):
        return self.s.get("{}/v1/discover/posts".format(self.root_url), *args, **kwargs)

    # limit, startKey
    def get_discover_users(self, *args, **kwargs):
        return self.s.get("{}/v1/discover/users".format(self.root_url), *args, **kwargs)

    def remove_post_from_discover_page(self, postId, *args, **kwargs):
        return self.s.delete("{}/v1/discover/posts/{}/remove".format(self.root_url, postId), *args, **kwargs)
