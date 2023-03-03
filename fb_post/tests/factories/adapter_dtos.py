import factory

from fb_post.adapters.fb_post_auth_adapter import UserDto


class UserDtoFactory(factory.Factory):
    class Meta:
        model = UserDto

    user_id = factory.sequence(lambda n: n+1)
    name = factory.Sequence(lambda n: f" user_{n+1}")
    profile_pic = factory.LazyAttribute(lambda o: f" {o.name}@url")