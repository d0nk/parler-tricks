class ViolationAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def create_report(self, *args, **kwargs):
        return self.s.post("{}/v3/contentModeration/report".format(self.root_url), *args, **kwargs)

    def get_details_for_report_with_id(self, report, *args, **kwargs):
        return self.s.get("{}/v3/contentModeration/report/{}".format(self.root_url, report), *args, **kwargs)

    # startPage, limit
    def get_list_of_reports(self, *args, **kwargs):
        return self.s.get("{}/v3/contentModeration/reports".format(self.root_url), *args, **kwargs)

    def get_stats(self, *args, **kwargs):
        return self.s.get("{}/v3/contentModeration/stats".format(self.root_url), *args, **kwargs)
