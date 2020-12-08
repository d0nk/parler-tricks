class NotificationAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def delete_all_notifications(self, *args, **kwargs):
        return self.s.delete("{}/v1/notification/all".format(self.root_url), *args, **kwargs)

    # id
    def delete_notification(self, *args, **kwargs):
        return self.s.delete("{}/v1/notification".format(self.root_url), *args, **kwargs)

    def get_badge_count(self, *args, **kwargs):
        return self.s.get("{}/v1/notification/count".format(self.root_url), *args, **kwargs)

    # startkey, action
    def get_notifications(self, *args, **kwargs):
        return self.s.get("{}/v1/notification".format(self.root_url), *args, **kwargs)
