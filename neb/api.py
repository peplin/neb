import json
from restkit import Resource

class TrinityAPIError(Exception):
    pass

class TrinityResource(Resource):
    def __init__(self, use_ssl=False, data=None):
        self.host = self.base_uri(use_ssl)
        super(TrinityResource, self).__init__(self.host, follow_redirect=True)
        if data:
            self.from_dict(json.loads(data))

    def base_uri(self, use_ssl=False):
        base = 'http://THE_IP_ADDRESS_TODO'
        base = base.replace('http://', 'https://') if use_ssl else base
        return base

    def request(self, *args, **kwargs):
        response = super(TrinityResource, self).request(*args, **kwargs)
        return response.body_string()

    def from_dict(self, data):
        for key, value in data.iteritems():
            safe_key = key.replace('-', '_')
            setattr(self, safe_key, value)
