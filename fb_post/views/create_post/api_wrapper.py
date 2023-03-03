from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from fb_post.interactors.create_post_interactor import CreatePostInteractor
from ...presenters.create_post_presenter_implementation import \
    PresenterImplementationCreatePost


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs) -> int:
    request_data = kwargs['request_data']
    user_id = request_data['posted_by']
    post_content = request_data['content']

    post_storage = PostStorageImplementation()
    presenter = PresenterImplementationCreatePost()

    interactor = CreatePostInteractor(post_storage=post_storage,
                                      presenter=presenter)

    response = interactor.create_post_wrapper(
        user_id=user_id, post_content=post_content)

    return response
