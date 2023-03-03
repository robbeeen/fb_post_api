from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.get_all_post_interactor import GetAllPostInteractor
from ...presenters.get_all_post_presenter_implementation import \
    PresenterImplementationGetAllPost
from ...presenters.get_post_presenter_implementation import \
    PresenterImplementationGetPost
from ...storages.comment_storage_implementation import \
    CommentStorageImplementation
from ...storages.post_storage_implementation import PostStorageImplementation
from ...storages.reaction_storage_implementation import \
    ReactionStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    sortby = kwargs['request_query_params'].sortby
    offset = kwargs['request_query_params'].offset
    limit = kwargs['request_query_params'].limit
    filterby = kwargs['request_query_params'].filterby
    sortby_order = kwargs['request_query_params'].sortby_order
    post_storage = PostStorageImplementation()
    comment_storage = CommentStorageImplementation()
    reaction_storage = ReactionStorageImplementation()
    presenter = PresenterImplementationGetAllPost()
    get_post_presenter = PresenterImplementationGetPost()
    interactor = GetAllPostInteractor(post_storage=post_storage,
                                      comment_storage=comment_storage,
                                      reaction_storage=reaction_storage,
                                      presenter=presenter,
                                      get_post_presenter=get_post_presenter)

    response = interactor.get_all_post_wrapper(sortby=sortby, offset=offset,
                                               limit=limit, filterby=filterby,
                                               sortby_order=sortby_order)

    return response
