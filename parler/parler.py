from parler.authentication import AuthenticationAPI
from parler.authentication_v2 import V2AuthenticationAPI
from parler.campaign_management import CampaignManagementAPI
from parler.campaign_promoter_management import CampaignManagementPromoterAPI
from parler.comments import CommentsAPI
from parler.contacts_uploader import ContactsUploaderAPI
from parler.content_moderation import ContentModerationAPI
from parler.conversion import ConversionAPI
from parler.deposit import DepositAPI
from parler.discover import DiscoverAPI
from parler.feed import FeedAPI
from parler.feedback import FeedbackAPI
from parler.flags import FlagsAPI
from parler.follow import FollowAPI
from parler.image import ImageAPI
from parler.link import LinkAPI
from parler.messaging import MessagingAPI
from parler.moderation import ModerationAPI
from parler.notification import NotificationAPI
from parler.parler_data import ParlerDataAPI
from parler.parler_video import ParlerVideoAPI
from parler.posts import PostsAPI
from parler.promoter_campaign_management import PromoterCampaignManagementAPI
from parler.search import SearchAPI
from parler.settings import SettingsAPI
from parler.tipping import TippingAPI
from parler.transaction import TransactionAPI
from parler.user_verification import UserVerificationAPI
from parler.user import UserAPI
from parler.violation import ViolationAPI
from parler.wallet_card import WalletCardAPI
from parler.wallet_general import WalletGeneralAPI
from parler.wallet import WalletAPI
import requests

class Parler:
    '''
    the api is accessible at api.parler.com and par.pw.
    staging api = api.speak-free.com
    mst and jst cookie are same as on web
    '''
    def __init__(self, mst=None, jst=None, root_url="https://api.parler.com"):
        session = requests.Session()
        session.headers['User-Agent'] = 'Parler%20Staging/545 CFNetwork/978.0.7 Darwin 18.7.0'
        if mst is not None:
            session.cookies['mst'] = mst
        if jst is not None:
            session.cookies['jst'] = jst

        self.authentication_api = AuthenticationAPI(session, root_url)
        self.v2_authentication_api = V2AuthenticationAPI(session, root_url)
        self.campaign_management_api = CampaignManagementAPI(session, root_url)
        self.campaign_management_promoter_api = CampaignManagementPromoterAPI(session, root_url)
        self.comments_api = CommentsAPI(session, root_url)
        self.contacts_uploader_api = ContactsUploaderAPI(session, root_url)
        self.content_moderation_api = ContentModerationAPI(session, root_url)
        self.conversion_api = ConversionAPI(session, root_url)
        self.deposit_api = DepositAPI(session, root_url)
        self.discover_api = DiscoverAPI(session, root_url)
        self.feed_api = FeedAPI(session, root_url)
        self.feedback_api = FeedbackAPI(session, root_url)
        self.flags_api = FlagsAPI(session, root_url)
        self.follow_api = FollowAPI(session, root_url)
        self.image_api = ImageAPI(session, root_url)
        self.link_api = LinkAPI(session, root_url)
        self.messaging_api = MessagingAPI(session, root_url)
        self.moderation_api = ModerationAPI(session, root_url)
        self.notification_api = NotificationAPI(session, root_url)
        self.parler_data_api = ParlerDataAPI(session, root_url)
        self.parler_video_api = ParlerVideoAPI(session, root_url)
        self.posts_api = PostsAPI(session, root_url)
        self.promoter_campaign_management = PromoterCampaignManagementAPI(session, root_url)
        self.search_api = SearchAPI(session, root_url)
        self.settings_api = SettingsAPI(session, root_url)
        self.tipping_api = TippingAPI(session, root_url)
        self.transaction_api = TransactionAPI(session, root_url)
        self.user_api = UserAPI(session, root_url)
        self.user_verification = UserVerificationAPI(session, root_url)
        self.violation_api = ViolationAPI(session, root_url)
        self.wallet_card_api = WalletCardAPI(session, root_url)
        self.wallet_general_api = WalletGeneralAPI(session, root_url)
        self.wallet_api = WalletAPI(session, root_url)
