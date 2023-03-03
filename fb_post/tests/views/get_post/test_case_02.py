"""
invalid post id
"""
from unittest.mock import patch

import pytest
from django_swagger_utils.utils.test_utils import TestUtils


from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

class TestCase02GetPostAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {}

    @pytest.mark.django_db
    @patch('fb_post.adapters.fb_post_auth_adapter.FbPostAuthAdapter.'
           'is_user_exists')
    def test_case(self, user_exists, snapshot):
        body = {}
        path_params = {"post_id": 1}
        query_params = {}
        headers = {}
        user_exists.return_value = True
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)

