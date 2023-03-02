import datetime
import factory
from fb_post.models.comment import Comment
from fb_post.models.reaction import Reaction
from fb_post.models.post import Post


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    id = factory.Sequence(lambda n: n + 1)
    content = factory.Sequence(lambda n: f" content {n}")
    posted_at = datetime.datetime(2023, 2, 1, 15, 6, 0)
    posted_by_id = factory.sequence(lambda n: n + 1)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    id = factory.sequence(lambda n: n + 1)
    content = factory.sequence(lambda n: f" content {n}")
    commented_at = datetime.datetime(2023, 2, 1, 15, 6, 0)
    commented_by_id = factory.sequence(lambda n: n + 1)
    post_id = factory.sequence(lambda n: n + 1)
    parent_comment_id = None


class ReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction

    post_id = factory.sequence(lambda n: n + 1)
    comment_id = factory.sequence(lambda n: n + 1)
    reaction = factory.Iterator(["HAHA", "WOW", "SAD"])
    reacted_at = datetime.datetime(2023, 2, 1, 15, 6, 0)
    reacted_by_id = factory.sequence(lambda n: n + 1)
