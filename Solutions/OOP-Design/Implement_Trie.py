# https://leetcode.com/problems/implement-trie-prefix-tree/submissions/
# Medium

class Node:
    def __init__(self,val=None):
        self.val = val
        self.children = dict()
        self.end = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curr = self.head
        
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = Node(char)
                curr = curr.children[char]
            
        curr.end = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.head
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return curr.end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        curr = self.head
        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


"""
O(n) time for all methods
O(n) space for all methods
"""