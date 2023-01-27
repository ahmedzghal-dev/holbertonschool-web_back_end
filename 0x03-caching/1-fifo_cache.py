#!/usr/bin/python3
''' Create a class FIFOCache that inherits from
BaseCaching and is a caching system '''

BaseCaching = __import__('base_caching').BaseCaching


class FIFO_Cache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return None
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard_key = next(iter(self.cache_data))
            self.cache_data.pop(discard_key)
            print("DISCARD: {}".format(discard_key))
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
