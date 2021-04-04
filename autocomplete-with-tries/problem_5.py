import string

from ipywidgets import interact


# Represents a single node in the Trie
class TrieNode:
    def __init__(self, char='', end_of_word=False):
        # Initialize this node in the Trie
        self.children: dict[string, TrieNode] = {}
        self.char: string = char
        self.end_of_word = end_of_word

    def insert(self, char):
        # Add a child node in this Trie
        self.children[char] = TrieNode(char)

    def suffixes(self, suffix='') -> list[string]:
        suffixes = []
        self.collect_suffixes(self, suffix, suffixes)
        return suffixes

    def collect_suffixes(self, node, word: string, suffixes: list):
        if (not node.children or node.end_of_word) and word != '':
            suffixes.append(word)
        for child in node.children.values():
            self.collect_suffixes(child, word + child.char, suffixes)



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
        last_index = len(word) - 1

        for i, char in enumerate(word):
            if char not in children:
                children[char] = TrieNode(char, i == last_index)
            children = children[char].children

    # Find the Trie node that represents this prefix
    def find(self, prefix: string) -> TrieNode or None:
        node = self.root

        for char in prefix:
            if char == node.char:
                return node
            if char not in node.children:
                return None
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


def f(prefix):
    if prefix != '':
        prefixNode = myTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f,prefix='')


print("Test return all words when empty suffix")
node = myTrie.find("")
print(node.suffixes())

if node.suffixes() == wordList:
    print("Pass")

print("\nTest returns y when suffix trigonometr")
node = myTrie.find("trigonometr")
print(node.suffixes())

if node.suffixes() == ["trigonometry"]:
    print("Pass")

print("\nTest node not found when suffix doesn't match")
node = myTrie.find("trololo")

if node is None:
    print("Pass")
