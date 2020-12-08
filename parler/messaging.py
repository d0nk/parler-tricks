class MessagingAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def accept_conversation(self, _id, *args, **kwargs):
        return self.s.post("{}/v1/messaging/conversations/{}/accept".format(self.root_url, _id), *args, **kwargs)

    def find_or_create_conversation_with_user(self, user, *args, **kwargs):
        return self.s.get("{}/v1/messaging/conversations/user/{}".format(self.root_url, user), *args, **kwargs)

    # limit
    def get_conversation_requests(self, *args, **kwargs):
        return self.s.get("{}/v1/messaging/conversations/requests".format(self.root_url), *args, **kwargs)

    # limit, startkey
    def get_conversations(self, *args, **kwargs):
        return self.s.get("{}/v1/messaging/conversations".format(self.root_url), *args, **kwargs)

    def get_conversation(self, _id, *args, **kwargs):
        return self.s.get("{}/v1/messaging/conversations/{}".format(self.root_url, _id), *args, **kwargs)

    # limit, startkey
    def get_messages_for_conversation(self, _id, *args, **kwargs):
        return self.s.get("{}/v1/messaging/conversations/{}/messages".format(self.root_url, _id), *args, **kwargs)

    def get_messaging_counts(self, *args, **kwargs):
        return self.s.get("{}/v1/messaging/counts".format(self.root_url), *args, **kwargs)

    # limit, startkey
    def get_unread_conversations(self, *args, **kwargs):
        return self.s.get("{}/v1/messaging/conversations/unread".format(self.root_url), *args, **kwargs)

    def hide_conversation(self, _id, *args, **kwargs):
        return self.s.post("{}/v1/messaging/conversations/{}/hide".format(self.root_url, _id), *args, **kwargs)

    def mark_all_message_requests_read(self, *args, **kwargs):
        return self.s.post("{}/v1/messaging/conversations/requests".format(self.root_url), *args, **kwargs)

    def mark_conversation_as_read(self, _id, *args, **kwargs):
        return self.s.post("{}/v1/messaging/conversations/{}/read".format(self.root_url, _id), *args, **kwargs)

    def post_message(self, _id, *args, **kwargs):
        return self.s.post("{}/v1/messaging/conversations/{}/messages".format(self.root_url, _id), *args, **kwargs)

    # search, startkey
    def search_for_mutual_follow_users(self, *args, **kwargs):
        return self.s.get("{}/v1/messaging/conversations/user/".format(self.root_url), *args, **kwargs)
