# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestPresenterCreatePost.test_response_for_invalid_user 1'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_USER_ID',
    'response': 'User Not Found'
}
