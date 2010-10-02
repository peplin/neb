from nose.tools import eq_
import json
import unittest
import mockito

from neb.relationship import Relationship
from neb.api import TrinityResource
import neb

fake_relationship = {'from_node': 'peplin', 'to': 'bueda',
        'data': {'other': 'data'}, 'link_type': 'works_for'}

class RelationshipTests(unittest.TestCase):
    def setUp(self):
        super(RelationshipTests, self).setUp()
        mockito.when(TrinityResource).request(
                mockito.any(), path=mockito.any(), payload=mockito.any(),
                headers=mockito.any()).thenReturn(json.dumps(fake_relationship))
        self.relationship = Relationship().create(start='bueda',
                to='peplin', type='is_a')

    def tearDown(self):
        super(RelationshipTests, self).tearDown()
        mockito.unstub()

    def test_create(self):
        assert self.relationship

    def test_from(self):
        eq_(self.relationship.from_node, fake_relationship['from_node'])

    def test_to(self):
        eq_(self.relationship.to, fake_relationship['to'])

    def test_data(self):
        eq_(self.relationship.data, fake_relationship['data'])

    def test_type(self):
        eq_(self.relationship.link_type, fake_relationship['link_type'])
