# from ipywidgets import widgets
# from IPython.display import display
# from ipywidgets import interact
#
#
# def f(prefix):
#     if prefix != '':
#         prefixNode = MyTrie.find(prefix)
#         if prefixNode:
#             print('\n'.join(prefixNode.suffixes()))
#         else:
#             print(prefix + " not found")
#     else:
#         print('')
# interact(f,prefix='');
#
#
# # Represents a single node in the Trie
# class TrieNode:
#     def __init__(self):
#         ## Initialize this node in the Trie
#         pass
#
#     def insert(self, char):
#         ## Add a child node in this Trie
#         pass
#
#     def suffixes(self, suffix=''):
#         pass
#
#
# ## Recursive function that collects the suffix for
# ## all complete words below this point
# # Add a child node in this Trie
#
#
# # The Trie itself containing the root node and insert/find functions
# class Trie:
#     def __init__(self):
#         pass
#
#     # Initialize this Trie (add a root node)
#
#     def insert(self, word):
#         pass
#
#     # Add a word to the Trie
#
#     def find(self, prefix):
#         pass
# # Find the Trie node that represents this prefix
#
#
# MyTrie = Trie()
# wordList = [
#     "ant", "anthology", "antagonist", "antonym",
#     "fun", "function", "factory",
#     "trie", "trigger", "trigonometry", "tripod"
# ]
# for word in wordList:
#     MyTrie.insert(word)
