
class CampaignManagementAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def delete_campaign(self, identifier, *args, **kwargs):
        return self.s.delete("{}/v3/promotionNetwork/campaign/{}".format(self.root_url, identifier), *args, *kwargs)

    def get_current_users_stats_for_promotion(self, *args, **kwargs):
        return self.s.get("{}/v3/promotionNetwork/stats".format(self.root_url), *args, *kwargs)

    def get_details_for_campaign(self, identifier, *args, **kwargs):
        return self.s.get("{}/v3/promotionNetwork/campaign/{}".format(self.root_url, identifier), *args, *kwargs)

    def get_list_of_campaigns(self, *args, **kwargs):
        return self.s.get("{}/v3/promotionNetwork/campaigns".format(self.root_url), *args, *kwargs)

    def set_details_for_campaign(self, identifier, *args, **kwargs):
        return self.s.post("{}/v3/promotionNetwork/campaign/{}".format(self.root_url, identifier), *args, *kwargs)

    def start_creating_new_campaign(self, *args, **kwargs):
        return self.s.post("{}/v3/promotionNetwork/campaign".format(self.root_url), *args, *kwargs)

    def submit_campaign(self, identifier, *args, **kwargs):
        return self.s.post("{}/v3/promotionNetwork/campaign/{}/submit".format(self.root_url, identifier), *args, *kwargs)