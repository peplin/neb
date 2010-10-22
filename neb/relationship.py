from neb.api import TrinityResource

class Relationship(TrinityResource):
    def create(self, from_node, to, link_type, append=None, increment=None,
            **kwargs):
        params = dict(from_node=from_node, to=to, link_type=link_type,
                data=kwargs)
        if append:
            params[append] = append
        if increment:
            params['increment'] = increment
        return self.post(self._relationship_path(from_node), payload=params)

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

    def __str__(self):
        if hasattr(self, 'from_node') and hasattr(self, 'to'):
            return "<%s => %s>" % (self.from_node, self.to)
        else:
            return super(Relationship, self).__str__()
