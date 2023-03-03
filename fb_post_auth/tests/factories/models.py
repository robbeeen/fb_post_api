import factory

from fb_post_auth.models.user import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id = factory.sequence(lambda n: n + 1)
    name = factory.Sequence(lambda n: f" user_{n+1}")
    profile_pic = factory.LazyAttribute(lambda o: f" {o.name}@url")
