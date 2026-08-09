## Problem2
# Longest Word in Dictionary(https://leetcode.com/problems/longest-word-in-dictionary/)
# ==============================================================================
# TIME & SPACE COMPLEXITY ANALYSIS
# ==============================================================================
# Let N = total number of words in the dictionary
# Let L = average / maximum length of a word
# Let Σ = size of the alphabet (Σ = 26 for lowercase English letters)
#
# 1. TIME COMPLEXITY: O(N * L)
#    - Trie Insertion:
#      Inserting N words into the Trie, where each word has up to L characters,
#      takes O(N * L) time.
#    - Depth-First Search (DFS):
#      In the worst case, every node in the Trie is visited once. Since the 
#      maximum number of nodes in the Trie is bounded by O(N * L), traversing 
#      the Trie takes O(N * L) time. At each child node, checking lengths and
#      updating `result` takes O(1) time.
#    - Total Time Complexity: O(N * L)
#
# 2. SPACE COMPLEXITY: O(N * L)
#    - Trie Storage:
#      In the worst case (no shared prefixes), the Trie contains O(N * L) nodes.
#      Each node stores an array of size 26 (constant memory O(Σ)) and a string reference.
#    - Recursion Stack:
#      The maximum depth of the DFS call stack is the length of the longest 
#      valid word, which is O(L).
#    - Total Space Complexity: O(N * L)
# ==============================================================================

class TrieNode:
    def __init__(self, end: str = None):
        # Array of 26 pointers initialized to None for each letter 'a'-'z'
        self.children = [None] * 26
        # Store the full word at the terminal node to easily keep track of valid words
        self.end = end

class Trie:
    def __init__(self):
        # Initialize the root node of the Trie with an empty word marker
        self.root = TrieNode('')

    def insert(self, word):
        curr = self.root
        for ch in word:
            # Map character 'a'-'z' to index 0-25
            idx = ord(ch) - ord('a')
            # Create a new Trie node if the child node doesn't exist
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        # Mark the end node of this path with the complete word
        curr.end = word

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Build the Trie structure using all input words
        trie = Trie()
        for w in words:
            trie.insert(w)

        result = ""

        # Perform DFS to find the longest word built one character at a time
        def dfs(root):
            nonlocal result
            
            # Iterate through child nodes in alphabetical order ('a' through 'z')
            for child in root.children:
                # Crucial Condition:
                # We only traverse further if 'child' exists AND 'child.end' is non-empty.
                # This guarantees that every prefix forming the current path is a valid word.
                if child and child.end:
                    # Update result if we find a strictly longer valid word.
                    # Lexicographical order is naturally preserved because children 
                    # are evaluated from index 0 ('a') to 25 ('z').
                    if len(child.end) > len(result):
                        result = child.end
                    
                    # Recursively traverse deeper down this branch
                    dfs(child)

        # Start DFS traversal from the Trie root
        dfs(trie.root)
        
        return result