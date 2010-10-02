from neb.api import TrinityResource

class NodeStatistic(TrinityResource):
    def calculate(self, node_id, stat):
        return self.get(self._statistic_path(node_id, stat))

    @staticmethod
    def _statistic_path(node_id, statistic):
        return 'node/%s/stats?stat=%s' % (node_id, statistic)

    def request(self, *args, **kwargs):
        response = super(NodeStatistic, self).request(*args, **kwargs)
        return NodeStatistic(data=response)
