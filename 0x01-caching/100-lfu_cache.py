#!/usr/bin/env python3
"""
class that inherits from BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    class LFUCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        super().__init__()
        self.queue = []
        self.frequency = {}
        
    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the item value
        for the key key.
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.evict_least_frequent()
            self.cache_data[key] = item
            self.queue.append(key)
            self.increment_frequency(key)

    def get(self, key):
        """
        check if key exists in self.cache_data
        """
        if key in self.cache_data:
            self.increment_frequency(key)
            return self.cache_data[key]
        return None

    def evict_least_frequent(self):
        if self.queue:
            least_frequent_key = min(self.queue, key=lambda k: self.frequency.get(k, 0))
            self.queue.remove(least_frequent_key)
            print("DISCARD:", least_frequent_key)
            del self.cache_data[least_frequent_key]
            del self.frequency[least_frequent_key]

    def increment_frequency(self, key):
        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1
