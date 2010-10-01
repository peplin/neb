from trinity.api import TrinityResource

class Relationship(TrinityResource):
    def find(self, node_id):
        return self.get(self._relationship_path(node_id, relationship_id))

    def all(self, node_id):
        return self.get(self._relationship_path(node_id))

    @staticmethod
    def _relationship_path(node_id, relationship_id=None):
        if relationship_id:
            path = 'node/%d/relationships/%d' % (node_id, relationship_id)
        else:
            path = 'node/%d/relationships' % node_id
        return path

    def request(self, *args, **kwargs):
        response = super(Relationship, self).request(*args, **kwargs)
        return Relationship(data=response)
