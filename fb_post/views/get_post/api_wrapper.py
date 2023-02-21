from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.get_post_interactor import GetPostInteractor
from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.comment_storage_implementation import \
    CommentStorageImplementation
from ...storages.post_storage_implementation import PostStorageImplementation
from fb_post.storages.reaction_storage_implementation import \
    ReactionStorageImplementation

from ...storages.user_storage_implementation import UserStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['post_id']
    post_storage = PostStorageImplementation()
    user_storage = UserStorageImplementation()
    comment_storage = CommentStorageImplementation()
    reaction_storage = ReactionStorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetPostInteractor(
        post_storage=post_storage,
        user_storage=user_storage,
        comment_storage=comment_storage,
        reaction_storage=reaction_storage,
        presenter=presenter,
        post_id=post_id
    )

    response = interactor.get_post_wrapper(post_id=post_id)

    http_response = response
    return response
