# -*- coding: utf-8 -*-

import redis


class Redis(redis.Redis):
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

    def get(self, name, cache=False):
        try:
            value = self._manager.cache[name]
        except KeyError:
            value = super().get(name)
            self._manager.cache[name] = value
        return value
