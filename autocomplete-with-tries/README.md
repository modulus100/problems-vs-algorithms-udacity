This trie is a tree data structure but has many branches. In order  
to solve a problem with many branches I use a dictionary. It helps  
to keep reference to a next node. Each trie node keeps a char of a word  
which has been inserted to the trie. The  end_of_word property  
denotes where inserted word ends, it helps during the search by suffix.  
I general it's just a tree but children but has additional properties.  

Space complexity: **O(nm)** . Where n - number of words and m - word length.     
Time complexity: insert **O(log(n))**, find **O(log(n))**, suffixes **O(nmlog(n))**