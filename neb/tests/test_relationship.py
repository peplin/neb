import unittest
import mockito

from neb.tests.mock import mock_trinity
from neb.node import Relationship
import neb

class RelationshipTests(unittest.TestCase):
    def setUp(self):
        super(RelationshipTests, self).setUp()
        mock_trinity()

    def tearDown(self):
        super(RelationshipTests, self).tearDown()
        mockito.unstub()

    def test_find(self):
        e = trinity.node.Relationship().find(203543, 'is_a')
