

REQUEST_BODY_JSON = """
{
    "post_id": 1
}
"""


RESPONSE_200_JSON = """
{
    "post_id": 1,
    "posted_by": {
        "name": "string",
        "user_id": 1,
        "profile_pic": "string"
    },
    "posted_at": "string",
    "post_content": "string",
    "reactions": {
        "count": 1,
        "type": [
            "string"
        ]
    },
    "comments": [
        {
            "comment_id": 1,
            "commenter": {
                "name": "string",
                "user_id": 1,
                "profile_pic": "string"
            },
            "commented_at": "string",
            "comment_content": "string",
            "reactions": {
                "count": 1,
                "type": [
                    "string"
                ]
            },
            "replies_count": 1,
            "replies": [
                {
                    "comment_id": 1,
                    "commenter": {
                        "name": "string",
                        "user_id": 1,
                        "profile_pic": "string"
                    },
                    "commented_at": "string",
                    "comment_content": "string",
                    "reactions": {
                        "count": 1,
                        "type": [
                            "string"
                        ]
                    }
                }
            ]
        }
    ],
    "comments_count": 1
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_POST_ID"
}
"""

