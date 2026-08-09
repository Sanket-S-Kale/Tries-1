## Problem1 
# Implement Trie (Prefix Tree)(https://leetcode.com/problems/implement-trie-prefix-tree/)
from typing import Optional

class TrieNode:
    def __init__(self, children: Optional['TrieNode'] = None, isEnd: bool = False):
        # Array of size 26 to hold references to child nodes for each lowercase English letter ('a' through 'z')
        self.children = [None] * 26
        # Boolean flag to indicate if this node represents the end of a complete word
        self.isEnd = False

class Trie:
    def __init__(self):
        # Initialize the root node of the Prefix Tree (Trie)
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.
        
        Logic:
        Iterate through each character of the word, compute its 0-indexed position ('a' -> 0, 'b' -> 1, ..., 'z' -> 25),
        and dynamically instantiate new TrieNodes along the path if they don't already exist.
        Finally, mark the terminal node's `isEnd` flag as True.

        Time Complexity: O(m), where m is the length of the word.
        Space Complexity: O(m) in the worst case (when no characters share an existing prefix path).
        """
        curr = self.root
        for i in range(len(word)):
            ch = word[i]
            idx = ord(ch) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        """
        Searches for an exact complete word in the Trie.

        Logic:
        Traverse down the Trie character by character. If at any point a character's corresponding
        child pointer is None, the word does not exist in the Trie. If the entire word path is traversed,
        return True only if `isEnd` is set to True on the final node.

        Time Complexity: O(m), where m is the length of the word.
        Space Complexity: O(1) auxiliary space.
        """
        curr = self.root
        for i in range(len(word)):
            ch = word[i]
            idx = ord(ch) - ord('a')
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Checks if there is any word in the Trie that starts with the given prefix.

        Logic:
        Traverse down the Trie matching each character of the prefix. If all characters in the 
        prefix exist along a valid path, return True regardless of whether `isEnd` is set to True.

        Time Complexity: O(m), where m is the length of the prefix.
        Space Complexity: O(1) auxiliary space.
        """
        curr = self.root
        for i in range(len(prefix)):
            ch = prefix[i]
            idx = ord(ch) - ord('a')
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        return True