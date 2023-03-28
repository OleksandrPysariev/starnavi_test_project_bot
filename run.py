from bot.src.facebook_actions.facebook_signup_action import SingUpAction
from bot.src.facebook_actions.facebook_make_posts_action import MakePostsAction
from bot.src.facebook_actions.facebook_like_posts_action import LikePostsAction
from bot.src.utils import purge
from settings import (
    NUMBER_OF_USERS,
)

if __name__ == '__main__':
    purge()

    signup = SingUpAction()
    make_posts = MakePostsAction()
    like_posts = LikePostsAction()

    print(f"[RUNNING]: Creating users...")
    signup.execute(NUMBER_OF_USERS)
    print(f"[SUCCESS]: Created users")
    print(f"[RUNNING]: Creating posts...")
    make_posts.execute()
    print(f"[SUCCESS]: Created posts")
    print(f"[RUNNING]: Creating likes...")
    like_posts.execute()
    print(f"[SUCCESS]: Created likes")
