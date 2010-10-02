from neb.api import TrinityResource
from neb.relationship import Relationship
from neb.statistic import NodeStatistic

class Node(TrinityResource):
    def create(self, node_id, **kwargs):
        params = dict(id=node_id, node=kwargs)
        return self.post(self._node_path(), payload=params)

    def connect(self, to, type, **kwargs):
        if isinstance(to, Node):
            to = to.id
        return Relationship().create(start=self.id, to=to, type=type, **kwargs) 

    def statistic(self, stat):
        return NodeStatistic().calculate(node_id=self.id, stat=stat)

    @staticmethod
    def _node_path(node_id=None):
        if node_id:
            path = 'node/%s' % node_id
        else:
            path = 'node'
        return path

    def request(self, *args, **kwargs):
        response = super(Node, self).request(*args, **kwargs)
        return Node(data=response)
