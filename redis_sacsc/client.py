# -*- coding: utf-8 -*-

import redis


class CachedRedis(redis.Redis):
    def __init__(self, manager, opt_in, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self._manager = manager
        self._client_id = super().client_id()
        self.opt_in = opt_in
        try:
            if self.opt_in:
                self.execute_command(
                    "CLIENT",
                    "TRACKING",
                    "ON",
                    "redirect",
                    self._manager.client_id,
                    "OPTIN",
                )
            else:
                self.execute_command(
                    "CLIENT", "TRACKING", "ON", "redirect", self._manager.client_id
                )
        except redis.exceptions.ResponseError:
            raise NotImplementedError(
                "This redis version does not support this feature"
            )

    def close(self):
        self.execute_command("CLIENT", "TRACKING", "OFF")
        super().close()

    def get(self, name, opt_cache=False):
        try:
            value = self._manager.cache[name]
        except KeyError:
            if self.opt_in and opt_cache:
                self.__cache_next()
            value = super().get(name)
            if (self.opt_in and opt_cache) or not self.opt_in:
                self._manager.cache[name] = value
        except redis.exceptions.ConnectionError:
            print("reset called" * 20)
            self._manager.reset()
            raise
        return value

    def __cache_next(self):
        self.execute_command("CACHING", "NOREPLY")
