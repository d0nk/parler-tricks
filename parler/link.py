class LinkAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    # link
    def post_links_with_url(self, *args, **kwargs):
        return self.s.post("{}/v1/link".format(self.root_url), *args, **kwargs)

    # link
    def post_link_with_giphy(self, *args, **kwargs):
        return self.s.post("{}/v1/link".format(self.root_url), *args, **kwargs)

    # longURL, metadata, link, links
    def post_url_link(self, *args, **kwargs):
        return self.s.post("{}/v1/link".format(self.root_url), *args, **kwargs)
