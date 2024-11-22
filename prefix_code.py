# this would be extremeley wasteful:
words = ["apple", "app", "application", "banana", "band", "bandit"]
prefix_dict = {}
for word in words:
    for i in range(1, len(word) + 1):
        prefix = word[:i]
        if prefix not in prefix_dict:
            prefix_dict[prefix] = set() 
        prefix_dict[prefix].add(word) # python add() not add this word if it already exists
for prefix, words_set in prefix_dict.items():
    print(f"{prefix}: {words_set}")
    

# less wasteful if we implement the TrieNode:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True