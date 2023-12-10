# Approach: Tree + Hashmap
# Tip: Maintain a tree containing a path (of chars) corresponding to every word.

class Node:
    # Complexity: O(1)
    def __init__(self):
        # Node can have multiple children stored in this hashmap.
        self.children = {}

class Trie:
    # Complexity: O(1)
    def __init__(self):
        # Initially trie has a dummy node which holds starting char of all words.
        self.root = Node()

    # Complexity: O(word)
    def insert(self, word: str) -> None:
        # Start from the root node.
        cur = self.root

        # Insert a node (if not present) for each char of string such that there
        # exits path in the trie representing the word after the insertion.
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
        # A char is the ending of a word if it has '' as one of its children.
        cur.children[''] = Node()

    # Complexity: O(word)
    def search(self, word: str) -> bool:
        # Start from the root node.
        cur = self.root

        # Try to find a path in the trie representing the word.
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        # Ensure that there exists a word ending after the last char of word.
        return '' in cur.children

    # Complexity: O(prefix)
    # Same as search() except word ending after last char is not required.
    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
