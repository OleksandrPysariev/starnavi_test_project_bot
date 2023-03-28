import random

from ..request_maker import req_driver as requests
from bot.src.facebook_actions.facebook_base_action import HTTPActionWithCreds
from settings import MAX_LIKES_PER_USER, ADDRESS


class LikePostsAction(HTTPActionWithCreds):
    def __init__(self):
        super(LikePostsAction, self).__init__()
        self.route = "api/like/post"
        self.method = "post"
        self.number_of_requests = MAX_LIKES_PER_USER

    @staticmethod
    def get_random_post_id():
        r = requests.get(f"http://{ADDRESS}/api/post/all").json()
        count = r.get("count")
        r = requests.get(f"http://{ADDRESS}/api/post/all", params={"page_size": count}).json()
        return random.choice(r.get("results")).get("id")

    @staticmethod
    def build_data():
        return {"post": LikePostsAction.get_random_post_id()}
