# -*- coding: utf-8 -*-

from collections import OrderedDict


class LRUCache(OrderedDict):
    def __init__(self, manager, maxsize=256, *args, **kwargs):
        self.maxsize = maxsize
        self.manager = manager
        super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.manager.add(key)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]
            self.manager.discard(oldest)
