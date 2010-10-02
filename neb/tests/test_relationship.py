import json
import unittest
import mockito

from neb.relationship import Relationship
from neb.api import TrinityResource
import neb

fake_relationship = {'from': 'peplin', 'to': 'bueda',
        'data': {'other': 'data'}, 'type': 'works_for'}

class RelationshipTests(unittest.TestCase):
    def setUp(self):
        super(RelationshipTests, self).setUp()
        mockito.when(TrinityResource).request(
                mockito.any(), path=mockito.any(), payload=mockito.any(),
                headers=mockito.any()).thenReturn(json.dumps(fake_relationship))

    def tearDown(self):
        super(RelationshipTests, self).tearDown()
        mockito.unstub()

    def test_create(self):
        relationship = Relationship().create(start='bueda',
                to='peplin', type='is_a')
        assert relationship
