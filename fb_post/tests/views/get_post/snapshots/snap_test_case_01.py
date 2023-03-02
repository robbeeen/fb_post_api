# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetPostAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetPostAPITestCase.test_case body'] = {
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
    'post_content': ' content 0',
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
