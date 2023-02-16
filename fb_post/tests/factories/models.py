from datetime import datetime
import factory
from fb_post.models.user import User
from fb_post.models.post import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id = factory.sequence(lambda n: n+1)
    name = factory.Sequence(lambda n: 'user %s' % n)
    profile_pic = factory.LazyAttribute(lambda o: '%s@url' % o.name)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    id = factory.Sequence(lambda n: n+1)
    content = factory.Sequence(lambda n: 'Content %s' % n)
    posted_at = factory.LazyFunction(datetime.now)
    posted_by = factory.SubFactory(UserFactory)
