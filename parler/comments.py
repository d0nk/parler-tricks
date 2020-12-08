
class CommentsAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    # parent, body, links, sensitive
    def create_comment(self, *args, **kwargs):
        return self.s.post("{}/v1/comment/async".format(self.root_url), *args, **kwargs)

    # id
    def delete_comment(self, _id, *args, **kwargs):
        return self.s.delete("{}/v1/comment".format(self.root_url), params={'id': _id} *args, **kwargs)

    # id, up
    def downvote_comment(self, *args, **kwargs):
        return self.s.post("{}/v1/comment/vote".format(self.root_url), *args, **kwargs)

    # sortBy, reverse, startKey, id
    def get_comments(self, *args, **kwargs):
        return self.s.get("{}/v1/comment".format(self.root_url), *args, **kwargs)

    # startKey, conversation, id, sortBy
    def get_comments_by_conversation(self, *args, **kwargs):
        return self.s.get("{}/v1/comment".format(self.root_url), *args, **kwargs)

    # id
    def remove_comment_votes(self, *args, **kwargs):
        return self.s.delete("{}/v1/comment/vote".format(self.root_url), *args, **kwargs)

    # id, up
    def upvote_comment(self, *args, **kwargs):
        return self.s.post("{}/v1/comment/vote".format(self.root_url), *args, **kwargs)
