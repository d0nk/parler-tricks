class PromoterCampaignManagementAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def approve_promoter_campaign(self, campaign, *args, **kwargs):
        return self.s.post("{}/v3/promotionNetwork/promoter/campaign/{}".format(self.root_url, campaign), *args, **kwargs)

    def get_current_status_of_promotion(self, *args, **kwargs):
        return self.s.get("{}/v3/promotionNetwork/promoter".format(self.root_url), *args, **kwargs)

    def get_details_for_campaign(self, campaign, *args, **kwargs):
        return self.s.get("{}/v3/promotionNetwork/promoter/campaign/{}".format(self.root_url, campaign), *args, **kwargs)

    def get_list_of_campaigns(self, *args, **kwargs):
        return self.s.get("{}/v3/promotionNetwork/promoter/campaigns".format(self.root_url), *args, **kwargs)

    def set_active_promoter(self, *args, **kwargs):
        return self.s.post("{}/v3/promotionNetwork/promoter/active".format(self.root_url), *args, **kwargs)

    def set_new_cpm_value_for_promoter(self, *args, **kwargs):
        return self.s.post("{}/v3/promotionNetwork/promoter/cpm".format(self.root_url), *args, **kwargs)

    def set_promoter_guidelines(self, *args, **kwargs):
        return self.s.post("{}/v3/promotionNetwork/promoter/guidelines".format(self.root_url), *args, **kwargs)