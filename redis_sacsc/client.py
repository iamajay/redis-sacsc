import redis
from redis.exceptions import ResponseError


class Redis(redis.Redis):
    def __init__(self, manager, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        import pdb
        pdb.set_trace()
        self._manager = manager
        self._client_id = super().client_id()
        try:
            self.execute_command('CLIENT', 'TRACKING', 'ON', 'redirect', self._manager.client_id)
        except ResponseError:
            raise NotImplementedError("the redis version you are using is not compatible with this feature")

    def close(self):
        self.execute_command('CLIENT', 'TRACKING', 'OFF')
        super().close()

    def get(self, name):
        try:
            value = self._manager.cache[name]
        except KeyError:
            value = super().get(name)
            self._manager.cache[name] = value
        return value
