import json

from django.http import HttpResponse

from fb_post.constants.exception_messages import INVALID_USER_ID
from fb_post.presenters.presenter_implementation import PresenterImplementation


class TestPresenterCreatePost:
    def test_response_for_valid_user(self):
        post_id = 2

        expected_response = {
            "post_id": post_id
        }

        presenter = PresenterImplementation()

        # Act
        response = presenter.get_success_post_response(post_id)

        # Assert
        assert json.loads(response.content) == expected_response

    def test_response_for_invalid_user(self,snapshot):
        # Arrange
        presenter = PresenterImplementation()

        # Act
        response = presenter.get_invalid_user_response()

        # Assert
        snapshot.assert_match(json.loads(response.content))
