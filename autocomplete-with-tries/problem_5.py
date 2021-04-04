import string

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact


# def f(prefix):
#     if prefix != '':
#         prefixNode = MyTrie.find(prefix)
#         if prefixNode:
#             print('\n'.join(prefixNode.suffixes()))
#         else:
#             print(prefix + " not found")
#     else:
#         print('')
# interact(f,prefix='')


# Represents a single node in the Trie
class TrieNode:
    def __init__(self, char=''):
        # Initialize this node in the Trie
        self.children: dict[string, TrieNode] = {}
        self.char: string = char

    def insert(self, char):
        # Add a child node in this Trie
        self.children[char] = TrieNode(char)

    def suffixes(self, suffix=''):
        pass


## Recursive function that collects the suffix for
## all complete words below this point
# Add a child node in this Trie


# The Trie itself containing the root node and insert/find functions
class Trie:
    # Initialize this Trie (add a root node)
    def __init__(self):
        self.root = TrieNode()

    # Add a word to the Trie
    def insert(self, word: string):
        children = self.root.children

        for char in word:
            if char not in children:
                children[char] = TrieNode(char)
            children = children[char].children

    # Find the Trie node that represents this prefix
    def find(self, prefix: string) -> TrieNode or None:
        last_index = len(prefix) - 1
        i = 0
        node = self.root

        for char in prefix:
            if char not in node.children:
                return None
            if i == last_index:
                return node
            node = node.children[char]

        return node



myTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    myTrie.insert(word)

node = myTrie.find("ant")
print(node.char)
