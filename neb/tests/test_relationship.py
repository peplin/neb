from nose.tools import eq_, ok_
import json
import unittest
import mockito

from neb.relationship import Relationship
from neb.api import TrinityResource
import neb

class RelationshipTests(unittest.TestCase):
    fake_relationship = {'from_node': 'peplin', 'to': 'bueda',
            'data': {'other': 'data'}, 'link_type': 'works_for'}

    def setUp(self):
        super(RelationshipTests, self).setUp()
        mockito.when(TrinityResource).request(
                mockito.any(), path=mockito.any(), payload=mockito.any(),
                headers=mockito.any()).thenReturn(
                    json.dumps(self.fake_relationship))
        self.relationship = Relationship().create(
                from_node=self.fake_relationship['from_node'],
                to=self.fake_relationship['to'],
                link_type=self.fake_relationship['link_type'],
                **self.fake_relationship['data'])

    def tearDown(self):
        super(RelationshipTests, self).tearDown()
        mockito.unstub()

    def test_create(self):
        ok_(self.relationship)

    def test_from(self):
        eq_(self.relationship.from_node, self.fake_relationship['from_node'])

    def test_to(self):
        eq_(self.relationship.to, self.fake_relationship['to'])

    def test_data(self):
        eq_(self.relationship.data, self.fake_relationship['data'])

    def test_type(self):
        eq_(self.relationship.link_type, self.fake_relationship['link_type'])

class ExtendedRelationshipTests(unittest.TestCase):
    fake_relationship = {'from_node': 'peplin', 'to': 'bueda',
            'data': {'other': 'data', 'new_data': 'banf', 'count': 1},
            'link_type': 'works_for'}

    def setUp(self):
        super(ExtendedRelationshipTests, self).setUp()
        mockito.when(TrinityResource).request(
                mockito.any(), path=mockito.any(), payload=mockito.any(),
                headers=mockito.any()).thenReturn(
                    json.dumps(self.fake_relationship))
        self.relationship = Relationship().create(
                from_node=self.fake_relationship['from_node'],
                to=self.fake_relationship['to'],
                link_type=self.fake_relationship['link_type'],
                **self.fake_relationship['data'])

    def tearDown(self):
        super(ExtendedRelationshipTests, self).tearDown()
        mockito.unstub()

    def test_create(self):
        ok_(self.relationship)
        ok_('append' not in self.relationship.data)

    def test_data(self):
        eq_(self.relationship.data, self.fake_relationship['data'])

    def test_increment(self):
        relationship = Relationship().create(
                from_node=self.fake_relationship['from_node'],
                to=self.fake_relationship['to'],
                link_type=self.fake_relationship['link_type'],
                increment=['count'],
                **self.fake_relationship['data'])

        ok_('increment' not in relationship.data)
