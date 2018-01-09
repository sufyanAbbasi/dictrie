from UserDict import UserDict
from collections import deque

class Dictrie(UserDict, object):
    
    def __init__(self, *wordslists):
        super(Dictrie, self).__init__()
        for words in wordslists:
            self.build_trie(words)
        
    def is_word(self, word):
        return word in self and ' ' in self[word]
    
    def get_words(self, root):
        queue = deque([root])
        while queue:
            curr_str = queue.popleft()
            if not self[curr_str]:
                yield curr_str.strip()
            else:
                queue.extend(curr_str + key for key in sorted(self[curr_str].iterkeys()))
    
    def build_trie(self, words):
        words = list(words)
        for word in words:
            self[' '] = word

    def __iter__(self):
        queue = deque(sorted(self.iterkeys()))
        while queue:
            curr_str = queue.popleft()
            if not self[curr_str]:
                yield curr_str
            else:
                queue.extend(curr_str + key for key in sorted(self[curr_str].iterkeys()))
    
    def __contains__(self, key):
        sub_trie = self.data
        for char in key:
            if char in sub_trie:
                sub_trie = sub_trie[char]
            else:
                return False
        return True
    
    def __getitem__(self, key):
        sub_trie = self.data
        for char in key:
            if char in sub_trie:
                sub_trie = sub_trie[char]
            else:
                raise KeyError(key)
        return sub_trie
    
    def __setitem__(self, key, item):
        sub_trie = self.data
        for char in item.strip() + ' ':
            sub_trie = sub_trie.setdefault(char, {})