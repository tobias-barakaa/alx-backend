#!/usr/bin/python3
""" LFUCache module
"""
from collections import defaultdict
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - caching system following the LFU algorithm
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.last_used_time = {}

    def put(self, key, item):
        """ Add an item in the cache following LFU algorithm
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find the least frequently used item
            lfu_items = [k for k, v in self.frequency.items() if v == min(self.frequency.values())]
            lru_item = min(lfu_items, key=lambda k: self.last_used_time[k])

            # Discard the least recently used item in case of ties
            for k in lfu_items:
                if self.last_used_time[k] < self.last_used_time[lru_item]:
                    lru_item = k

            del self.cache_data[lru_item]
            del self.frequency[lru_item]
            del self.last_used_time[lru_item]
            print("DISCARD:", lru_item)

        self.cache_data[key] = item
        self.frequency[key] += 1
        self.last_used_time[key] = datetime.now()

    def get(self, key):
        """ Get an item by key following LFU algorithm
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.last_used_time[key] = datetime.now()
        return self.cache_data[key]
