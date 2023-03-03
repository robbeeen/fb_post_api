"""
# TODO: Update test case description
"""
from unittest.mock import patch

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.adapter_dtos import UserDtoFactory

from ...factories.models import PostFactory, CommentFactory, \
    ReactionFactory


class TestCase01GetAllPostAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {}

    @pytest.mark.django_db
    @patch('fb_post.adapters.fb_post_auth_adapter.FbPostAuthAdapter.'
           'get_user_dtos')
    def test_case(self, user_dtos, snapshot):
        body = {}
        path_params = {}
        query_params = {"offset": 1, "limit": 5}
        headers = {}
        post_id = 1
        PostFactory(id=post_id, posted_by_id=1)
        ReactionFactory(reaction="WOW", post_id=post_id, comment_id=None,
                        reacted_by_id=1)
        CommentFactory()
        ReactionFactory(reaction="LIT", post_id=None, comment_id=1,
                        reacted_by_id=1)
        CommentFactory(parent_comment_id=1, post_id=None)
        user_dtos.return_value = [UserDtoFactory()]
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
