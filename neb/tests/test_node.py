from nose.tools import eq_, ok_
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
        self.node = Node().create('bueda',
                username=fake_node['node']['username'],
                user_id=fake_node['node']['user_id'])

    def tearDown(self):
        super(NodeTests, self).tearDown()
        mockito.unstub()

    def test_create(self):
        ok_(self.node)

    def test_id(self):
        eq_(self.node.id, fake_node['id'])

    def test_data(self):
        eq_(self.node.node, fake_node['node'])

    def test_connect_to_id(self):
        data = {'username': 'peplin', 'user_id': 6789}
        node = Node().create('peplin', **data)
        relationship = self.node.connect(to='peplin', link_type='works_for')
        ok_(relationship)

    def test_connect_to_node(self):
        employer = self.node
        employee = Node().create('peplin', **self.data)
        relationship = employee.connect(to=employer, link_type='works_for')
        ok_(relationship)

    def test_statistic(self):
        statistic = self.node.statistic(statistic='topics')
        ok_(statistic)
