import json
from itertools import count

from django.http import HttpResponse

from fb_post.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from fb_post.constants.exception_messages import INVALID_USER_ID, \
    INVALID_POST_ID


def get_reaction_on_post(reactions_dtos, post_id):
    list_of_reactions = []
    for reactions_dto in reactions_dtos:
        if reactions_dto.post_id == post_id:
            list_of_reactions.append(reactions_dto.type)

    return {"count": len(list_of_reactions),
            "type": list_of_reactions
            }


def get_commenter(comments_on_post_dto, commenter_dtos ):
    user_id = comments_on_post_dto.commented_by_id
    for commenter_dto in commenter_dtos:
        if commenter_dto.user_id == user_id:
            return {
                "name": commenter_dto.name,
                "user_id": commenter_dto.user_id,
                "profile_pic": commenter_dto.profile_pic
            }


def get_reply_commenter(reply_dto, user_dtos):
    for user_dto in user_dtos:
        if user_dto.user_id == reply_dto.commented_by_id:
            return {
                "name": user_dto.name,
                "user_id": user_dto.user_id,
                "profile_pic": user_dto.profile_pic
            }


def get_reaction_on_comment(reactions_dtos, comment_id):
    list_of_reactions = []
    for reactions_dto in reactions_dtos:
        if reactions_dto.comment_id == comment_id:
            list_of_reactions.append(reactions_dto.type)

    return {
        "count": len(list_of_reactions),
        "type": list_of_reactions
    }


def get_replies(replies_dtos, user_dtos, comment_id, reactions_dtos):
    list_of_replies = []
    for reply_on_comment_dto in replies_dtos:
        if reply_on_comment_dto.parent_comment_id == comment_id:
            reply_dict = dict()
            reply_dict['comment_id'] = reply_on_comment_dto.comment_id
            reply_dict['commenter'] = get_reply_commenter(reply_on_comment_dto,
                                                          user_dtos)
            reply_dict['commented_at'] = reply_on_comment_dto.commented_at
            reply_dict[
                'comment_content'] = reply_on_comment_dto.comment_content
            reply_dict['reactions'] = get_reaction_on_comment(
                reactions_dtos, reply_on_comment_dto.comment_id)
            list_of_replies.append(reply_dict)

    return list_of_replies


def get_comments(comments_on_post_dtos, replies_dtos, user_dtos,
                 post_id, reactions_dtos):
    list_of_comments = []

    for comments_on_post_dto in comments_on_post_dtos:
        if comments_on_post_dto.post_id == post_id:
            reply_count = 0
            for reply_dto in replies_dtos:
                if reply_dto.parent_comment_id == comments_on_post_dto.comment_id:
                    reply_count += 1
            comment_dict = dict()
            comment_dict['comment_id'] = comments_on_post_dto.comment_id
            comment_dict['commenter'] = get_commenter(comments_on_post_dto,
                                                      user_dtos)
            comment_dict['commented_at'] = comments_on_post_dto.commented_at
            comment_dict[
                'comment_content'] = comments_on_post_dto.comment_content
            comment_dict['reactions'] = get_reaction_on_comment(
                reactions_dtos, comments_on_post_dto.comment_id)

            comment_dict['replies_count'] = reply_count
            comment_dict['replies'] = get_replies(replies_dtos, user_dtos,
                                                  comments_on_post_dto.comment_id,
                                                  reactions_dtos)
            list_of_comments.append(comment_dict)
    return list_of_comments


def get_user(user_dtos, post_dto):
    for user_dto in user_dtos:
        if user_dto.user_id == post_dto.posted_by_id:
            return {
                "name": user_dto.name,
                "user_id": user_dto.user_id,
                "profile_pic": user_dto.profile_pic
            }


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

    def failed_get_post_response(self) -> HttpResponse:
        response_dict = {
            "response": INVALID_POST_ID[0],
            "http_status_code": 400,
            "res_status": INVALID_POST_ID[1]
        }

        return HttpResponse(content=json.dumps(response_dict),
                            status=response_dict["http_status_code"])

    def success_get_post_response(self, response_dto):
        post_dto = response_dto.post_dto
        user_dtos = response_dto.user_dtos
        comments_on_post_dtos = response_dto.comment_dtos
        replies_dtos = response_dto.reply_dtos
        reactions_dtos = response_dto.reactions_dtos

        response = {
            "post_id": post_dto.post_id,
            "posted_by": get_user(user_dtos, post_dto),
            "posted_at": post_dto.posted_at,
            "post_content": post_dto.content,
            "reactions": get_reaction_on_post(reactions_dtos,
                                              post_dto.post_id),
            "comments": get_comments(comments_on_post_dtos, replies_dtos,
                                     user_dtos,
                                     post_dto.post_id,
                                     reactions_dtos),
            "comments_count": len(comments_on_post_dtos)
        }

        return HttpResponse(content=json.dumps(response, default=str),
                            status=200)
