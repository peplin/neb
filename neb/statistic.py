from trinity.api import TrinityResource

class Statistic(TrinityResource):
    def calculate(self, node_id, statistic):
        return self.get(self._statistic_path(node_id, statistic))

    @staticmethod
    def _statistic_path(node_id, statistic):
        return 'node/%d/stats?stat=%s' % (node_id, statistic)

    def request(self, *args, **kwargs):
        response = super(Statistic, self).request(*args, **kwargs)
        return Statistic(data=response)
