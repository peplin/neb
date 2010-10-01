import unittest
import mockito

from neb.tests.mock import mock_trinity
from neb.node import Statistic
import neb

class StatisticTests(unittest.TestCase):
    def setUp(self):
        super(StatisticTests, self).setUp()
        mock_trinity()

    def tearDown(self):
        super(StatisticTests, self).tearDown()
        mockito.unstub()

    def test_find(self):
        e = trinity.node.Statistic().find(203543, 'topics')
