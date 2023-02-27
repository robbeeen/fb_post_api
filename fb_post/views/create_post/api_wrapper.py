from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from fb_post.storages.user_storage_implementation import \
    UserStorageImplementation
from fb_post.presenters.get_post_presenter_implementation import PresenterImplementationGetPost
from fb_post.interactors.create_post_interactor import CreatePostInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs) -> int:
    request_data = kwargs['request_data']
    user_id = request_data['posted_by']
    post_content = request_data['content']

    user_storage = UserStorageImplementation()
    post_storage = PostStorageImplementation()
    presenter = PresenterImplementationGetPost()

    interactor = CreatePostInteractor(user_storage=user_storage,
                                      post_storage=post_storage,
                                      presenter=presenter,
                                      post_content=post_content)

    response = interactor.create_post_wrapper(
        user_id=user_id, post_content=post_content)

    return response
