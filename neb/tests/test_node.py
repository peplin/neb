import json
import unittest
import mockito

from neb.node import Node
from neb.api import TrinityResource
import neb

fake_node = {'id': 'bueda', 'node': {'username': 'bueda', 'user_id': 12345}}

class NodeTests(unittest.TestCase):
    def setUp(self):
        super(NodeTests, self).setUp()
        mockito.when(TrinityResource).request(
                mockito.any(), path=mockito.any(), payload=mockito.any(),
                headers=mockito.any()).thenReturn(json.dumps(fake_node))
        self.data = {'username': 'bueda', 'user_id': 12345}
        self.node = Node().create(node_id='bueda', node=self.data)

    def tearDown(self):
        super(NodeTests, self).tearDown()
        mockito.unstub()

    def test_create(self):
        assert self.node

    def test_connect_to_id(self):
        relationship = self.node.connect(to='peplin', type='works_for')
        assert relationship

    def test_connect_to_node(self):
        employer = self.node
        employee = Node().create(node_id='peplin', node=self.data)
        relationship = employee.connect(to=employer, type='works_for')
        assert relationship

    def test_statistic(self):
        statistic = self.node.statistic(stat='topics')
        assert statistic
