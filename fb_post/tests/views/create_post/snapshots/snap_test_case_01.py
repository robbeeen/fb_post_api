# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreatePostAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01CreatePostAPITestCase.test_case body'] = {
    'post_id': 1
}
