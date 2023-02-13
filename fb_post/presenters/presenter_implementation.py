from django.http import HttpResponse
from typing import Dict
import json
from fb_post.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from fb_post.constants.exception_messages import INVALID_USER_ID


class PresenterImplementation(PresenterInterface):
    def get_invalid_user_response(self) -> HttpResponse:
        response_dict = {
            "response": INVALID_USER_ID[0],
            "http_status_code": 400,
            "res_status": INVALID_USER_ID[1]
        }

        return HttpResponse(content=json.dumps(response_dict),
                            status=response_dict["http_status_code"])

    def get_success_post_response(self, post_id: int) -> HttpResponse:
        post_id_dict = {
            "post_id": post_id
        }
        return HttpResponse(content=json.dumps(post_id_dict),
                            status=200)
