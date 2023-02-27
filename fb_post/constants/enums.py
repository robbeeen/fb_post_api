import enum
from ib_common.constants import BaseEnumClass


class ReactionENUM(BaseEnumClass, enum.Enum):
    WOW = 'WOW'
    LIKE = 'LIKE'
    LIT = 'LIT'
    THUMBS_UP = 'THUMBS_UP'
    ANGRY = 'ANGRY'
    SAD = 'SAD'
