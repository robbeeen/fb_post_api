"""
valid post id
"""
import json

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import PostFactory, UserFactory, CommentFactory, \
    ReactionFactory



class TestCase01GetPostAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX

    SECURITY = {}

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {}
        path_params = {"post_id": 1}
        query_params = {}
        headers = {}
        post_id = 1
        UserFactory()
        UserFactory()
        PostFactory(id=post_id)
        ReactionFactory(reaction="WOW", post_id=post_id, comment_id=None,
                        reacted_by_id=1)
        CommentFactory()
        ReactionFactory(reaction="LIT", post_id=None, comment_id=1,
                        reacted_by_id=1)
        CommentFactory(parent_comment_id=1, post_id=None)
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
