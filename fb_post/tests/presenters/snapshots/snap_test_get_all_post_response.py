# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestPresenterGetPost.test_response_for_valid_posts response_content'] = [
    {
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
                        'commenter': {
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
    },
    {
        'comments': [
            {
                'comment_content': ' content 2',
                'comment_id': 3,
                'commented_at': '2023-02-01 15:06:00',
                'commenter': {
                    'name': ' user_4',
                    'profile_pic': '  user_4@url',
                    'user_id': 3
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
                        'comment_content': ' content 3',
                        'comment_id': 4,
                        'commented_at': '2023-02-01 15:06:00',
                        'commenter': {
                            'name': ' user_4',
                            'profile_pic': '  user_4@url',
                            'user_id': 3
                        },
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
        'post_id': 2,
        'posted_at': '2023-02-01 15:06:00',
        'posted_by': {
            'name': ' user_3',
            'profile_pic': '  user_3@url',
            'user_id': 2
        },
        'reactions': {
            'count': 1,
            'type': [
                'WOW'
            ]
        }
    }
]

snapshots['TestPresenterGetPost.test_response_for_valid_posts response_status_code'] = 200
