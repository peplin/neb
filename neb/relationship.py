from neb.api import TrinityResource

class Relationship(TrinityResource):
    def create(self, start, to, type, **kwargs):
        params = dict(start=start, to=to, type=type, data=kwargs)
        return self.post(self._relationship_path(start), payload=params)

    @staticmethod
    def _relationship_path(node_id, relationship_id=None):
        if relationship_id:
            path = 'node/%s/relationships/%d' % (node_id, relationship_id)
        else:
            path = 'node/%s/relationships' % node_id
        return path

    def request(self, *args, **kwargs):
        response = super(Relationship, self).request(*args, **kwargs)
        return Relationship(data=response)
