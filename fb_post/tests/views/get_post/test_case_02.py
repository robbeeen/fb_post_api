"""
invalid post id
"""
from unittest.mock import create_autospec

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from fb_post.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from fb_post.models.post import Post
from fb_post.presenters.presenter_implementation import PresenterImplementation
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import UserFactory, PostFactory


class TestCase02GetPostAPITestCase(TestUtils):
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
        UserFactory()
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)

