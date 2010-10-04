from neb.api import TrinityResource

class NodeStatistic(TrinityResource):
    def calculate(self, node_id, statistic):
        return self.get(self._statistic_path(node_id), stat=statistic)

    @staticmethod
    def _statistic_path(node_id):
        return 'node/%s/stats' % node_id

    def request(self, *args, **kwargs):
        response = super(NodeStatistic, self).request(*args, **kwargs)
        return NodeStatistic(data=response)

    def __str__(self):
        if hasattr(self, 'results'):
            return "<%s>" % self.results
        else:
            return super(NodeStatistic, self).__str__()
