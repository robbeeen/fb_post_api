# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestPresenterGetPost.test_response_for_valid_post response_content'] = {
    'comments': [
        {
            'comment_content': ' content 0',
            'comment_id': 1,
            'commented_at': '2023-02-01 15:06:00',
            'commenter': {
                'name': ' user_1',
                'profile_pic': '  user_1@url',
                'user_id': 1
            },
            'reactions': {
                'count': 2,
                'type': [
                    'WOW',
                    'LIT'
                ]
            },
            'replies': [
                {
                    'comment_content': ' content 1',
                    'comment_id': 2,
                    'commented_at': '2023-02-01 15:06:00',
                    'commenter': None,
                    'reactions': {
                        'count': 0,
                        'type': [
                        ]
                    }
                }
            ],
            'replies_count': 1
        }
    ],
    'comments_count': 1,
    'post_content': 'Content 1',
    'post_id': 1,
    'posted_at': '2023-02-01 15:06:00',
    'posted_by': {
        'name': ' user_1',
        'profile_pic': '  user_1@url',
        'user_id': 1
    },
    'reactions': {
        'count': 1,
        'type': [
            'WOW'
        ]
    }
}

snapshots['TestPresenterGetPost.test_response_for_valid_post response_status_code'] = 200

snapshots['TestPresenterGetPost.test_response_for_valid_post_only response_content'] = {
    'comments': [
    ],
    'comments_count': 0,
    'post_content': 'Content 1',
    'post_id': 1,
    'posted_at': '2023-02-01 15:06:00',
    'posted_by': {
        'name': ' user_1',
        'profile_pic': '  user_1@url',
        'user_id': 1
    },
    'reactions': {
        'count': 0,
        'type': [
        ]
    }
}

snapshots['TestPresenterGetPost.test_response_for_valid_post_only response_status_code'] = 200

snapshots['TestPresenterGetPost.test_response_for_valid_post_and_comment_only response_content'] = {
    'comments': [
        {
            'comment_content': ' content 0',
            'comment_id': 1,
            'commented_at': '2023-02-01 15:06:00',
            'commenter': {
                'name': ' user_1',
                'profile_pic': '  user_1@url',
                'user_id': 1
            },
            'reactions': {
                'count': 0,
                'type': [
                ]
            },
            'replies': [
            ],
            'replies_count': 0
        }
    ],
    'comments_count': 1,
    'post_content': 'Content 1',
    'post_id': 1,
    'posted_at': '2023-02-01 15:06:00',
    'posted_by': {
        'name': ' user_1',
        'profile_pic': '  user_1@url',
        'user_id': 1
    },
    'reactions': {
        'count': 0,
        'type': [
        ]
    }
}

snapshots['TestPresenterGetPost.test_response_for_valid_post_and_comment_only response_status_code'] = 200

snapshots['TestPresenterGetPost.test_response_for_valid_post_comment_replies_only response_content'] = {
    'comments': [
        {
            'comment_content': ' content 0',
            'comment_id': 1,
            'commented_at': '2023-02-01 15:06:00',
            'commenter': {
                'name': ' user_1',
                'profile_pic': '  user_1@url',
                'user_id': 1
            },
            'reactions': {
                'count': 0,
                'type': [
                ]
            },
            'replies': [
                {
                    'comment_content': ' content 1',
                    'comment_id': 2,
                    'commented_at': '2023-02-01 15:06:00',
                    'commenter': None,
                    'reactions': {
                        'count': 0,
                        'type': [
                        ]
                    }
                }
            ],
            'replies_count': 1
        }
    ],
    'comments_count': 1,
    'post_content': 'Content 1',
    'post_id': 1,
    'posted_at': '2023-02-01 15:06:00',
    'posted_by': {
        'name': ' user_1',
        'profile_pic': '  user_1@url',
        'user_id': 1
    },
    'reactions': {
        'count': 0,
        'type': [
        ]
    }
}

snapshots['TestPresenterGetPost.test_response_for_valid_post_comment_replies_only response_status_code'] = 200

snapshots['TestPresenterGetPost.test_response_for_valid_post_comment_reactions_only response_content'] = {
    'comments': [
        {
            'comment_content': ' content 0',
            'comment_id': 1,
            'commented_at': '2023-02-01 15:06:00',
            'commenter': {
                'name': ' user_1',
                'profile_pic': '  user_1@url',
                'user_id': 1
            },
            'reactions': {
                'count': 1,
                'type': [
                    'LIT'
                ]
            },
            'replies': [
            ],
            'replies_count': 0
        }
    ],
    'comments_count': 1,
    'post_content': 'Content 1',
    'post_id': 1,
    'posted_at': '2023-02-01 15:06:00',
    'posted_by': {
        'name': ' user_1',
        'profile_pic': '  user_1@url',
        'user_id': 1
    },
    'reactions': {
        'count': 1,
        'type': [
            'WOW'
        ]
    }
}

snapshots['TestPresenterGetPost.test_response_for_valid_post_comment_reactions_only response_status_code'] = 200

snapshots['TestPresenterGetPost.test_response_for_valid_post_reactions_only response_content'] = {
    'comments': [
    ],
    'comments_count': 0,
    'post_content': 'Content 1',
    'post_id': 1,
    'posted_at': '2023-02-01 15:06:00',
    'posted_by': {
        'name': ' user_1',
        'profile_pic': '  user_1@url',
        'user_id': 1
    },
    'reactions': {
        'count': 1,
        'type': [
            'WOW'
        ]
    }
}

snapshots['TestPresenterGetPost.test_response_for_valid_post_reactions_only response_status_code'] = 200

snapshots['TestPresenterGetPost.test_response_for_valid_comment_reactions_only response_content'] = {
    'comments': [
        {
            'comment_content': ' content 0',
            'comment_id': 1,
            'commented_at': '2023-02-01 15:06:00',
            'commenter': {
                'name': ' user_1',
                'profile_pic': '  user_1@url',
                'user_id': 1
            },
            'reactions': {
                'count': 1,
                'type': [
                    'LIT'
                ]
            },
            'replies': [
            ],
            'replies_count': 0
        }
    ],
    'comments_count': 1,
    'post_content': 'Content 1',
    'post_id': 1,
    'posted_at': '2023-02-01 15:06:00',
    'posted_by': {
        'name': ' user_1',
        'profile_pic': '  user_1@url',
        'user_id': 1
    },
    'reactions': {
        'count': 0,
        'type': [
        ]
    }
}

snapshots['TestPresenterGetPost.test_response_for_valid_comment_reactions_only response_status_code'] = 200
