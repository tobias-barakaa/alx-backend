#!/usr/bin/env python3
"""
class that inherits from BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    class MRUCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        constructor
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the item value
        for the key key.
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.queue.remove(key)
                else:
                    del self.cache_data[self.queue[-1]]
                    print("DISCARD:", self.queue[-1])
                    self.queue.pop(-1)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
