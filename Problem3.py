## Problem3
# Replace Words (https://leetcode.com/problems/replace-words/)
"""
===============================================================================
TIME AND SPACE COMPLEXITY ANALYSIS:
===============================================================================
Let:
  - N = number of roots in the dictionary
  - L = maximum length of a root word in the dictionary
  - M = number of words in the sentence
  - K = maximum length of a word in the sentence

1. TIME COMPLEXITY:
   - Building the Trie:
     Inserting N words of max length L into the Trie takes O(N * L) time.
   
   - Processing the Sentence:
     Splitting the sentence takes O(M * K) time.
     Searching each word in the Trie takes at most O(K) steps. For M words,
     searching takes O(M * K) time.
   
   - Overall Time Complexity: O(N * L + M * K)
     This is optimal as every character in the dictionary and sentence is 
     processed at most a constant number of times.

2. SPACE COMPLEXITY:
   - Trie Storage:
     In the worst case, storing all N words of max length L without overlapping
     prefixes requires O(N * L * Σ) space, where Σ = 26 (size of the English alphabet).
   
   - Output / Auxiliary Space:
     Storing the split words array and the result array takes O(M * K) space.
   
   - Overall Space Complexity: O(N * L * 26 + M * K) -> O(N * L + M * K)
===============================================================================
"""

from typing import List

class TrieNode:
    def __init__(self, end: str = None):
        # Array of 26 pointers for lowercase English letters 'a' through 'z'
        self.children = [None] * 26
        # Store the complete root word at the terminal node if this marks the end of a root
        self.end = end

class Trie:
    def __init__(self):
        # Root node of the Trie (represents empty string prefix)
        self.root = TrieNode()

    def insert(self, word: str):
        """Inserts a dictionary root word into the Trie."""
        curr = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            # Create a new Trie node if the child branch does not exist
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        
        # Mark the end of the root word by storing the word itself
        curr.end = word

    def search(self, word: str) -> str:
        """
        Traverses the Trie using characters of `word`.
        Returns the shortest root matching prefix if found; otherwise, returns `word`.
        """
        curr = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            # If path ends in Trie before hitting a valid root end, no prefix match exists
            if not curr.children[idx]:
                return word
            curr = curr.children[idx]
            
            # Since we traverse character-by-character from left to right,
            # the first time we encounter `curr.end != None`, we've found
            # the SHORTEST matching root prefix.
            if curr.end is not None:
                return curr.end
        
        # If the full word was traversed without finding a matching root, return original word
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        
        # Step 1: Build the Trie containing all dictionary roots
        for w in dictionary:
            trie.insert(w)
        
        result = []
        
        # Step 2: Replace each word in sentence with its shortest root prefix (if any)
        for word in sentence.split():
            result.append(trie.search(word))
            
        # Step 3: Reconstruct and return the processed sentence
        return " ".join(result)