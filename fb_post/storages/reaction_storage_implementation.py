from typing import List

from fb_post.interactors.storage_interfaces.dtos import ReactionDto
from fb_post.interactors.storage_interfaces.reaction_storage_interface import \
    ReactionStorageInterface
from fb_post.models.reaction import Reaction


class ReactionStorageImplementation(ReactionStorageInterface):
    def get_reactions_on_post(self, post_id: int) -> List[ReactionDto]:
        reactions = Reaction.objects.filter(
            post_id=post_id)
        reaction_post_dtos = [
            self._prepare_reaction_dto_using_reaction_object(reaction)
            for reaction in reactions
        ]
        return reaction_post_dtos

    def get_reactions_on_comments(self, comment_ids: List[int]) -> List[
        ReactionDto]:
        reactions = Reaction.objects.filter(
            comment_id__in=comment_ids)
        reaction_post_dtos = [
            self._prepare_reaction_dto_using_reaction_object(reaction)
            for reaction in reactions
        ]

        return reaction_post_dtos

    @staticmethod
    def _prepare_reaction_dto_using_reaction_object(reaction: Reaction) -> ReactionDto:
        return ReactionDto(
            post_id=reaction.post_id,
            comment_id=reaction.comment_id,
            type=reaction.reaction
        )
