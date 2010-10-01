import unittest
import mockito

from neb.tests.mock import mock_trinity
from neb.node import Node
import neb

class NodeTests(unittest.TestCase):
    def setUp(self):
        super(NodeTests, self).setUp()
        mock_trinity()

    def tearDown(self):
        super(NodeTests, self).tearDown()
        mockito.unstub()

    def test_find(self):
        e = trinity.node.Node().find(203543)
