"""
# For valid User
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from fb_post.models.post import Post
from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.models.user import User
from ...factories.models import UserFactory, PostFactory


class TestCase01CreatePostAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {}

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {'content': 'string', 'posted_by': 1}
        path_params = {}
        query_params = {}
        headers = {}
        user_id = 1
        expected_output = True
        UserFactory(id=user_id)
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)

        actual_output = Post.objects.filter(posted_by=1,
                                            content="string").exists()
        assert actual_output == expected_output
