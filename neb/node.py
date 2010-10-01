from trinity.api import TrinityResource

class Node(TrinityResource):
    def find(self, node_id):
        return self.get(self._node_path(node_id))
    
    @staticmethod
    def _node_path(node_id):
        return 'node/%(node_id)d' % node_id

    def request(self, *args, **kwargs):
        response = super(Node, self).request(*args, **kwargs)
        return Node(data=response)
