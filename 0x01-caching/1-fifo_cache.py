#!/usr/bin/env python3
"""
Inheritance class
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching
    and is a caching system
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
                    self.cache_data[key] = item
                    self.queue.remove(key)
                else:
                    del self.cache_data[self.queue[0]]
                    print("DISCARD:", self.queue[0])
                    self.queue.pop(0)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
