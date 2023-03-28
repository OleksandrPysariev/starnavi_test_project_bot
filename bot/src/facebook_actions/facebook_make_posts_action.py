from bot.src.faker import fake
from .facebook_base_action import HTTPActionWithCreds
from settings import MAX_POSTS_PER_USER


class MakePostsAction(HTTPActionWithCreds):
    def __init__(self):
        super(MakePostsAction, self).__init__()
        self.route = "api/post/create"
        self.method = "post"
        self.number_of_requests = MAX_POSTS_PER_USER

    @staticmethod
    def build_data() -> dict:
        return {
            "title": fake.title,
            "body": fake.body,
        }
