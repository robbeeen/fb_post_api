import json
from collections import defaultdict
from typing import List, Any, Dict

from django.http import HttpResponse
from django_swagger_utils.drf_server.exceptions import BadRequest

from fb_post.adapters.fb_post_auth_adapter import UserDto
from fb_post.constants.exception_messages import INVALID_OFFSET_LENGTH, \
    INVALID_LIMIT_LENGTH
from fb_post.interactors.presenter_interfaces.dtos import GetPostResponseDto
from fb_post.interactors.presenter_interfaces.presenter_interface_get_all_post import \
    PresenterInterfaceGetAllPost
from fb_post.interactors.storage_interfaces.dtos import ReactionDto, CommentDto


class PresenterImplementationGetAllPost(PresenterInterfaceGetAllPost):

    def raise_exception_for_invalid_offset_length(self):
        raise BadRequest(*INVALID_OFFSET_LENGTH)

    def raise_exception_for_invalid_limit_length(self):
        raise BadRequest(*INVALID_LIMIT_LENGTH)

    def get_success_all_post_response(self,
                                      response_dtos: List[
                                          GetPostResponseDto]) -> HttpResponse:
        list_of_post = []
        for response_dto in response_dtos:
            post_dto = response_dto.post_dto
            user_dtos = response_dto.user_dtos
            comments_on_post_dtos = response_dto.comment_dtos
            replies_dtos = response_dto.reply_dtos
            reactions_on_post_dtos = response_dto.reactions_on_post_dtos
            reactions_on_comments_dtos = response_dto.reactions_on_comments_dtos

            comment_reaction_dict = defaultdict(list)
            for reactions_on_comments_dto in reactions_on_comments_dtos:
                comment_reaction_dict[
                    reactions_on_comments_dto.comment_id].append(
                    reactions_on_comments_dto)

            reply_comment_dict = defaultdict(list)
            for replies_dto in replies_dtos:
                reply_comment_dict[replies_dto.parent_comment_id].append(
                    replies_dto)

            user_id_wise_user_dto = {
                user_dto.user_id: user_dto
                for user_dto in user_dtos
            }

            response = {
                "post_id": post_dto.post_id,
                "posted_by": self._get_user(
                    user_id_wise_user_dto[post_dto.posted_by_id]),
                "posted_at": post_dto.posted_at,
                "post_content": post_dto.content,
                "reactions": self._get_reaction_on_post(
                    reactions_on_post_dtos),
                "comments": self._get_comments(comments_on_post_dtos,
                                               user_id_wise_user_dto,
                                               reply_comment_dict,
                                               comment_reaction_dict),
                "comments_count": len(comments_on_post_dtos)
            }
            list_of_post.append(response)
        return HttpResponse(content=json.dumps(list_of_post, default=str),
                            status=200)

    @staticmethod
    def _get_reaction_on_post(reactions_dtos: List[ReactionDto]) -> \
            Dict[str, Any]:

        list_of_reactions = {
            reactions_dto.type for reactions_dto in reactions_dtos
        }

        return {
            "count": len(list_of_reactions),
            "type": list(list_of_reactions)
        }

    @staticmethod
    def _get_reaction_on_comment(reactions_dtos_list: List[ReactionDto],
                                 ) -> Dict[str, Any]:

        list_of_reactions = {
            reactions_dto.type for reactions_dto in reactions_dtos_list
        }

        return {
            "count": len(list_of_reactions),
            "type": list(list_of_reactions)
        }

    @staticmethod
    def _get_replies(self, user_dto: UserDto,
                     comment_reply_dto_list: List[CommentDto],
                     comment_reaction_dict: Dict[
                         int, List[ReactionDto]]) -> \
            List[
                Dict[str, Any]]:

        list_of_replies = []
        for reply_on_comment_dto in comment_reply_dto_list:
            reply_dict = {'comment_id': reply_on_comment_dto.comment_id,
                          'commenter': self._get_user(user_dto),
                          'commented_at': reply_on_comment_dto.commented_at,
                          'comment_content': reply_on_comment_dto.comment_content,
                          'reactions': self._get_reaction_on_comment(
                              comment_reaction_dict[
                                  reply_on_comment_dto.comment_id])}

            list_of_replies.append(reply_dict)

        return list_of_replies

    def _get_comments(self, comments_on_post_dtos: List[CommentDto],
                      user_id_wise_user_dto: Dict[int, UserDto],
                      reply_comment_dict: Dict[int, List[CommentDto]],
                      comment_reaction_dict: Dict[
                          int, List[ReactionDto]]) -> \
            List[Dict[str, Any]]:
        list_of_comments = []

        for comments_on_post_dto in comments_on_post_dtos:
            comment_dict = {'comment_id': comments_on_post_dto.comment_id,
                            'commenter': self._get_user(
                                user_id_wise_user_dto[
                                    comments_on_post_dto.commented_by_id]),
                            'commented_at': comments_on_post_dto.commented_at,
                            'comment_content': comments_on_post_dto.comment_content,
                            'reactions': self._get_reaction_on_comment(
                                comment_reaction_dict[
                                    comments_on_post_dto.comment_id]),
                            'replies_count': len(
                                reply_comment_dict[
                                    comments_on_post_dto.comment_id]),
                            'replies': self._get_replies(self,
                                                         user_id_wise_user_dto[
                                                             comments_on_post_dto.commented_by_id],
                                                         reply_comment_dict[
                                                             comments_on_post_dto.comment_id],
                                                         comment_reaction_dict)}

            list_of_comments.append(comment_dict)
        return list_of_comments

    @staticmethod
    def _get_user(user_dto: UserDto) -> Dict[str, Any]:
        return {
            "name": user_dto.name,
            "user_id": user_dto.user_id,
            "profile_pic": user_dto.profile_pic
        }
