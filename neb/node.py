from neb.api import TrinityResource
from neb.relationship import Relationship
from neb.statistic import NodeStatistic

class Node(TrinityResource):
    def create(self, node_id, **kwargs):
        if isinstance(node_id, str) or isinstance(node_id, unicode):
            node_id = node_id.replace('/', '-')
        params = dict(id=node_id, node=kwargs)
        return self.post(self._node_path(), payload=params)

    def connect(self, to, link_type, append=None, increment=None, **kwargs):
        if isinstance(to, Node):
            to = to.id
        return Relationship().create(from_node=self.id, to=to,
                link_type=link_type, append=append, increment=increment,
                **kwargs) 

    def statistic(self, statistic):
        return NodeStatistic().calculate(node_id=self.id, statistic=statistic)

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

    def __str__(self):
        if hasattr(self, 'id'):
            return "<%s>" % self.id
        else:
            return super(Node, self).__str__()
