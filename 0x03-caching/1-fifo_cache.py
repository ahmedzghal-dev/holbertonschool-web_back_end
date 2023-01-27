#!/usr/bin/python3
''' Create a class FIFOCache that inherits from
BaseCaching and is a caching system '''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    ''' FIFO  '''

    def __init__(self):
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        ''' insert item to dict '''
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_discarded = self.key_indexes.pop(0)
                del self.cache_data[item_discarded]
                print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        ''' get item from dict '''
        if key in self.cache_data:
            return self.cache_data[key]
        return None
