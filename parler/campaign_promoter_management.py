
class CampaignManagementPromoterAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def add_promoter_for_request(self, identifier, *args, **kwargs):
        return self.s.post("{}/v3/promotionNetwork/campaign/{}/promoter".format(self.root_url, identifier), *args, **kwargs)

    def get_details_for_promoter(self, campaignId, promoterId, *args, **kwargs):
        return self.s.get("{}/v3/promotionNetwork/campaign/{}/promoter/{}".format(self.root_url, campaignId, promoterId), *args, **kwargs)

    def get_current_list_of_promoters_for_campaign(self, campaignId, *args, **kwargs):
        return self.s.get("{}/v3/promotionNetwork/campaign/{}/promoters".format(self.root_url, campaignId), *args, **kwargs)

    def get_list_of_possible_promoters_for_campaign(self, campaignId, *args, **kwargs):
        return self.s.get("{}/v3/promotionNetwork/campaign/{}/promoters/new".format(self.root_url, campaignId), *args, **kwargs)

    def remove_promoter_from_campaign(self, campaignId, promoterId, *args, **kwargs):
        return self.s.delete("{}/v3/promotionNetwork/campaign/{}/promoter/{}".format(self.root_url, campaignId, promoterId), *args, **kwargs)

