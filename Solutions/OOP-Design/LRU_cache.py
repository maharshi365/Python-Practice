from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.dictionary = OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dictionary:
            val = self.dictionary[key]
            del self.dictionary[key]
            self.dictionary[key] = val
            return val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.dictionary:
            if self.count < self.capacity:
                self.dictionary[key] = value
                self.count += 1
            else:
                del self.dictionary[next(iter(self.dictionary))]
                self.dictionary[key] = value
        else:
            val = self.dictionary[key]
            del self.dictionary[key]
            self.dictionary[key] = value
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)