import json
import unittest
import mockito

from neb.statistic import NodeStatistic
from neb.api import TrinityResource
import neb

fake_node_statistics = {'zing': 'bat'}

class NodeStatisticTests(unittest.TestCase):
    def setUp(self):
        super(NodeStatisticTests, self).setUp()
        mockito.when(TrinityResource).request(
                mockito.any(), path=mockito.any(), payload=mockito.any(),
                headers=mockito.any()).thenReturn(
                json.dumps(fake_node_statistics))

    def tearDown(self):
        super(NodeStatisticTests, self).tearDown()
        mockito.unstub()

    def test_calculate(self):
        statistic = NodeStatistic().calculate(node_id='bueda',
                stat='topics')
        assert statistic
