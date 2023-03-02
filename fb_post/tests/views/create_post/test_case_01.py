"""
# For valid User
"""
from unittest.mock import patch

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from fb_post.models.post import Post
from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

from ...factories.models import PostFactory


class TestCase01CreatePostAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {}

    @pytest.mark.django_db
    @patch('fb_post.adapters.fb_post_auth_adapter.FbPostAuthAdapter.'
           'is_user_exists')
    def test_case(self, user_exists, snapshot):
        body = {'content': 'string', 'posted_by': 1}
        path_params = {}
        query_params = {}
        headers = {}
        user_id = 1
        expected_output = True
        user_exists.return_value = True
        PostFactory(posted_by_id=user_id, content="string")
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)

        actual_output = Post.objects.filter(posted_by_id=user_id,
                                            content="string").exists()
        assert actual_output == expected_output
