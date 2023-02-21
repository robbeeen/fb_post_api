from typing import List

from fb_post.interactors.storage_interfaces.dtos import ReactionDto
from fb_post.interactors.storage_interfaces.reaction_storage_interface import \
    ReactionStorageInterface
from fb_post.models.reaction import Reaction


class ReactionStorageImplementation(ReactionStorageInterface):
    def get_reactions(self, post_id, comment_ids):
        reactions = Reaction.objects.filter(post_id=post_id,
                                            comment_id__in=comment_ids)
        reaction_post_dtos = [
            self._prepare_reaction_post_dto(reaction)
            for reaction in reactions
        ]

        return reaction_post_dtos

    @staticmethod
    def _prepare_reaction_post_dto(reaction):
        return ReactionDto(
            post_id=reaction.post_id,
            comment_id=reaction.comment_id,
            type=reaction.reaction
        )
