class PostsAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    # id
    def delete_post(self, *args, **kwargs):
        return self.s.delete("{}/v1/post".format(self.root_url), *args, **kwargs)

    # id
    def dislike_post(self, *args, **kwargs):
        return self.s.post("{}/v1/user/dislike".format(self.root_url), *args, **kwargs)

    # urls
    def get_posts_using_urls(self, *args, **kwargs):
        return self.s.post("{}/v1/wordpress/posts".format(self.root_url), *args, **kwargs)

    
    def get_post_impressions_over_time(self, post, *args, **kwargs):
        return self.s.get("{}/v1/post/{}/impressions/time".format(self.root_url, post), *args, **kwargs)

    def get_post_impressions(self, post, *args, **kwargs):
        return self.s.get("{}/v1/post/{}/impressions".format(self.root_url, post), *args, **kwargs)

    # parent, body, links
    def repost_post_id(self, *args, **kwargs):
        return self.s.post("{}/v1/post".format(self.root_url), *args, **kwargs)

    # id
    def unvote_post(self, *args, **kwargs):
        return self.s.delete("{}/v1/post/upvote".format(self.root_url), *args, **kwargs)

    # id
    def upvote_post(self, *args, **kwargs):
        return self.s.post("{}/v1/post/upvote".format(self.root_url), *args, **kwargs)

    # body, links, sensitive
    def create_post(self, *args, **kwargs):
        return self.s.post("{}/v1/post/async".format(self.root_url), *args, **kwargs)

    # id
    def get_post(self, *args, **kwargs):
        return self.s.get("{}/v1/post".format(self.root_url), *args, **kwargs)
