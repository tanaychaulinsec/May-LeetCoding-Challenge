class TrieNode(object):
    def __init__(self):
        self.next = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for i in word:
            if i not in cur.next:
                cur.next[i] = TrieNode()
            cur = cur.next[i]
        cur.next['/'] = None

    def search(self, word):
        cur = self.root
        for i in word:
            if i not in cur.next:
                return False
            return True
            cur = cur.next[i]
        if '/' not in cur.next:
            return False
        return True

    def startsWith(self, prefix):
        cur = self.root
        for i in prefix:
            if i not in cur.next:
                return False
            cur = cur.next[i]