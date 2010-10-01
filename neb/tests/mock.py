from mockito import when
import mockito
import os

from neb.node import Node
from neb.relationship import Relationship
from neb.statistic import NodeStatistic

fake_error = open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
        'data', '2035230.xml')).read()

def mock_trinity():
    when(Node).request(
            mockito.any(), mockito.any()).thenReturn(Node(fake_node))
    when(Relationship).request(mockito.any(), mockito.any()
            ).thenReturn(Relationship(fake_relationship))
    when(NodeStatistic).request(mockito.any(), mockito.any()
            ).thenReturn(NodeStatistic(fake_node_statistics))
