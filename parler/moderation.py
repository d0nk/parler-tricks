class ModerationAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    # words, action, organization
    def add_word_filter(self, *args, **kwargs):
        # the free speech social network xd
        return self.s.post("{}/v1/moderation/filter/word".format(self.root_url), *args, **kwargs)

    # organization, id
    def approve_all_pending_comments_for_user_id(self, *args, **kwargs):
        return self.s.post("{}/v1/moderation/approve/user".format(self.root_url), *args, **kwargs)

    # organization, comments
    def approve_comments(self, *args, **kwargs):
        return self.s.post("{}/v1/moderation/approve".format(self.root_url), *args, **kwargs)

    def block_link(self, domain, *args, **kwargs):
        return self.s.post("{}/v2/iaa/moderation/domain/{}".format(self.root_url, domain), *args, **kwargs)

    def delete_iaa_report(self, report, *args, **kwargs):
        return self.s.delete("{}/v2/iaa/moderation/report/{}".format(self.root_url, report), *args, **kwargs)

    # organization, id
    def deny_all_comments_for_user_id(self, *args, **kwargs):
        return self.s.post("{}/v1/moderation/deny/user".format(self.root_url), *args, **kwargs)

    # organization, comments
    def deny_comments(self, *args, **kwargs):
        return self.s.post("{}/v1/moderation/deny".format(self.root_url), *args, **kwargs)

    # organization, startkey
    def get_approved_comments(self, *args, **kwargs):
        return self.s.get("{}/v1/moderation/approved".format(self.root_url), *args, **kwargs)

    # organization, startkey
    def get_denied_comments(self, *args, **kwargs):
        return self.s.get("{}/v1/moderation/denied".format(self.root_url), *args, **kwargs)

    def get_moderation_counts(self, *args, **kwargs):
        return self.s.get("{}/v1/moderation/count".format(self.root_url), *args, **kwargs)

    def get_iaa_report(self, *args, **kwargs):
        return self.s.get("{}/v2/iaa/moderation/report".format(self.root_url), *args, **kwargs)

    # organization, startkey
    def get_muted_comments(self, *args, **kwargs):
        return self.s.get("{}/v1/moderation/muted".format(self.root_url), *args, **kwargs)

    # organization, startkey
    def get_pending_comments(self, *args, **kwargs):
        return self.s.get("{}/v1/moderation/pending".format(self.root_url), *args, **kwargs)
    
    # organization, startkey
    def get_spam_comments(self, *args, **kwargs):
        return self.s.get("{}/v1/moderation/spam".format(self.root_url), *args, **kwargs)

    # action, startkey
    def get_word_filters(self, *args, **kwargs):
        return self.s.get("{}/v1/moderation/filter/word".format(self.root_url), *args, **kwargs)

    # organization, id
    def mark_all_comments_for_user_id_as_spam(self, *args, **kwargs):
        return self.s.post("{}/v1/moderation/spam/user".format(self.root_url), *args, **kwargs)

    def mark_comment_sensitive(self, comment, *args, **kwargs):
        return self.s.post("{}/v2/iaa/sensitive/comment/{}".format(self.root_url, comment), *args, **kwargs)

    # organization, comments
    def mark_comments_as_spam(self, *args, **kwargs):
        return self.s.post("{}/v1/moderation/spam".format(self.root_url), *args, **kwargs)

    def mark_post_sensitive(self, post, *args, **kwargs):
        return self.s.post("{}/v2/iaa/sensitive/post/{}".format(self.root_url, post), *args, **kwargs)

    def mark_user_sensitive(self, user, *args, **kwargs):
        return self.s.post("{}/v2/iaa/sensitive/user/{}".format(self.root_url, user), *args, **kwargs)

    # organization, id
    def mute_all_comments_for_user_id(self, *args, **kwargs):
        return self.s.post("{}/v1/moderation/mute/user".format(self.root_url), *args, **kwargs)

    # comments, organization
    def mute_comments(self, *args, **kwargs):
        return self.s.post("{}/v1/moderation/mute".format(self.root_url), *args, **kwargs)

    # displayable, value, notes
    def post_iaa_report(self, *args, **kwargs):
        return self.s.post("{}/v2/iaa/moderation/report".format(self.root_url), *args, **kwargs)

    # words, action, organization 
    def delete_word_filter(self, *args, **kwargs):
        return self.s.post("{}/v1/moderation/filter/word/delete".format(self.root_url), *args, **kwargs)

    def set_nsfw_enabled(self, val, *args, **kwargs):
        return self.s.post("{}/v2/profile/toggle/noSensitive/{}".format(self.root_url, val), *args, **kwargs)