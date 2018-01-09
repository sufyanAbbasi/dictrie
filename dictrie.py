from UserDict import UserDict
from collections import deque

class Dictrie(UserDict, object):

    def __init__(self, *wordslists, **kwargs):
        init_trie = kwargs.get('dict', {})
        super(Dictrie, self).__init__(init_trie)
        for words in wordslists:
            self.build_trie(words)

    # returns if word is a valid word in the dictionary
    def is_word(self, word):
        return word in self and ' ' in self[word]

    # returns a generator to produce all words in the trie beginning with
    # the root from shortest to longest
    def get_words(self, root):
        queue = deque([root])
        while queue:
            curr_str = queue.popleft()
            if not self[curr_str]:
                yield curr_str.strip()
            else:
                queue.extend(curr_str + key for key in sorted(self[curr_str].iterkeys()))

    # builds the trie given an iterator of words
    def build_trie(self, words):
        words = list(words)
        for word in words:
            self[' '] = word

    def __iter__(self):
        queue = deque(sorted(self.iterkeys()))
        while queue:
            curr_str = queue.popleft()
            if not self[curr_str]:
                yield curr_str.strip()
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