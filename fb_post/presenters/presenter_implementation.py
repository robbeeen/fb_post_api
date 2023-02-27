import json
from typing import List, Any, Dict

from django.http import HttpResponse

from fb_post.interactors.presenter_interfaces.dtos import GetPostResponseDto
from fb_post.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from fb_post.constants.exception_messages import INVALID_USER_ID, \
    INVALID_POST_ID
from fb_post.interactors.storage_interfaces.dtos import UserDto, PostDto, \
    ReactionDto, CommentDto


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

    def get_invalid_get_post_response(self) -> HttpResponse:
        response_dict = {
            "response": INVALID_POST_ID[0],
            "http_status_code": 400,
            "res_status": INVALID_POST_ID[1]
        }

        return HttpResponse(content=json.dumps(response_dict),
                            status=response_dict["http_status_code"])

    def get_success_get_post_response(self,
                                      response_dto: GetPostResponseDto) -> HttpResponse:
        post_dto = response_dto.post_dto
        user_dtos = response_dto.user_dtos
        comments_on_post_dtos = response_dto.comment_dtos
        replies_dtos = response_dto.reply_dtos
        reactions_on_post_dtos = response_dto.reactions_on_post_dtos
        reactions_on_comments_dtos = response_dto.reactions_on_comments_dtos

        comment_reply_dict = dict()
        for comments_on_post_dto in comments_on_post_dtos:
            list_of_replies = []
            for replies_dto in replies_dtos:
                if comments_on_post_dto.comment_id == replies_dto.parent_comment_id:
                    list_of_replies.append(replies_dto)
            comment_reply_dict[
                comments_on_post_dto.comment_id] = list_of_replies

        comment_reaction_dict = dict()

        for comments_on_post_dto in comments_on_post_dtos:
            list_of_reactions = []
            for reactions_on_comments_dto in reactions_on_comments_dtos:
                if comments_on_post_dto.comment_id == reactions_on_comments_dto.comment_id:
                    list_of_reactions.append(reactions_on_comments_dto)
            comment_reaction_dict[
                comments_on_post_dto.comment_id] = list_of_reactions

        response = {
            "post_id": post_dto.post_id,
            "posted_by": self._get_user(user_dtos, post_dto.posted_by_id),
            "posted_at": post_dto.posted_at,
            "post_content": post_dto.content,
            "reactions": self._get_reaction_on_post(reactions_on_post_dtos),
            "comments": self._get_comments(self, comments_on_post_dtos,
                                           user_dtos,
                                           comment_reply_dict,
                                           comment_reaction_dict),
            "comments_count": len(comments_on_post_dtos)
        }
        return HttpResponse(content=json.dumps(response, default=str),
                            status=200)

    @staticmethod
    def _get_reaction_on_post(reactions_dtos: List[ReactionDto]) -> \
            Dict[str, Any]:
        list_of_reactions = []
        for reactions_dto in reactions_dtos:
            list_of_reactions.append(reactions_dto.type)

        return {"count": len(list_of_reactions),
                "type": list(set(list_of_reactions))
                }

    @staticmethod
    def _get_commenter(user_id: int,
                       commenter_dtos: List[UserDto]) -> Dict[str, Any]:
        for commenter_dto in commenter_dtos:
            if commenter_dto.user_id == user_id:
                return {
                    "name": commenter_dto.name,
                    "user_id": commenter_dto.user_id,
                    "profile_pic": commenter_dto.profile_pic
                }

    @staticmethod
    def _get_reply_commenter(user_id: int,
                             user_dtos: List[UserDto]) -> \
            Dict[str, Any]:
        for user_dto in user_dtos:
            if user_dto.user_id == user_id:
                return {
                    "name": user_dto.name,
                    "user_id": user_dto.user_id,
                    "profile_pic": user_dto.profile_pic
                }

    @staticmethod
    def _get_reaction_on_comment(reactions_dtos_list: List[ReactionDto],
                                 ) -> Dict[str, Any]:

        list_of_type = []

        for reaction_dto in reactions_dtos_list:
            list_of_type.append(reaction_dto.type)

        return {
            "count": len(reactions_dtos_list),
            "type": list(set(list_of_type))
        }

    @staticmethod
    def _get_replies(self, user_dtos: List[UserDto],
                     comment_reply_dto_list: List[CommentDto],
                     comment_reaction_dict: Dict[int, List[ReactionDto]]) -> \
            List[
                Dict[str, Any]]:
        list_of_replies = []
        for reply_on_comment_dto in comment_reply_dto_list:
            reply_dict = dict()
            reply_dict['comment_id'] = reply_on_comment_dto.comment_id
            reply_dict['commenter'] = self._get_reply_commenter(
                reply_on_comment_dto.commented_by_id,
                user_dtos)
            reply_dict['commented_at'] = reply_on_comment_dto.commented_at
            reply_dict[
                'comment_content'] = reply_on_comment_dto.comment_content
            if comment_reaction_dict.get(
                    reply_on_comment_dto.comment_id) is not None:
                reply_dict['reactions'] = self._get_reaction_on_comment(
                    comment_reaction_dict[reply_on_comment_dto.comment_id])
            else:
                reply_dict['reactions'] = {
                    "count": 0,
                    "type": []
                }

                list_of_replies.append(reply_dict)

        return list_of_replies

    @staticmethod
    def _get_comments(self, comments_on_post_dtos: List[CommentDto],
                      user_dtos: List[UserDto],
                      comment_reply_dict: Dict[int, List[CommentDto]],
                      comment_reaction_dict: Dict[int, List[ReactionDto]]) -> \
            List[Dict[str, Any]]:
        list_of_comments = []

        for comments_on_post_dto in comments_on_post_dtos:
            comment_dict = dict()
            comment_dict['comment_id'] = comments_on_post_dto.comment_id
            comment_dict['commenter'] = self._get_commenter(
                comments_on_post_dto.commented_by_id,
                user_dtos)
            comment_dict[
                'commented_at'] = comments_on_post_dto.commented_at
            comment_dict[
                'comment_content'] = comments_on_post_dto.comment_content
            comment_dict['reactions'] = self._get_reaction_on_comment(
                comment_reaction_dict[comments_on_post_dto.comment_id]
            )

            comment_dict['replies_count'] = len(
                comment_reply_dict[comments_on_post_dto.comment_id])
            comment_dict['replies'] = self._get_replies(self, user_dtos,
                                                        comment_reply_dict[
                                                            comments_on_post_dto.comment_id],
                                                        comment_reaction_dict)
            list_of_comments.append(comment_dict)
        return list_of_comments

    @staticmethod
    def _get_user(user_dtos: List[UserDto], posted_by_id: int) -> Dict[
                str, Any]:
        for user_dto in user_dtos:
            if user_dto.user_id == posted_by_id:
                return {
                    "name": user_dto.name,
                    "user_id": user_dto.user_id,
                    "profile_pic": user_dto.profile_pic
                }
