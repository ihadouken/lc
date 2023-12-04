# Approach: Doubly Linked List + Hashmap, Complexity: O(1) for all operations.

# One node in the linked list for (key and value of) every cache entry.
class Node:
    def __init__(self, val: int, key: int):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

# Use a doubly linked list to maintain recency order of cache entries.
class LinkedList:
    def __init__(self, maxlen):
        self.maxlen = maxlen
        self.len = 0

        self.left = Node(-1, -1)
        self.right = Node(-1, -1)

        self.left.next = self.right
        self.right.prev = self.left

    # Add the given node at the end of list (making it most recent).
    def add(self, node: Node):
        node.prev = self.right.prev
        self.right.prev = node

        node.prev.next = node
        node.next = self.right

        self.len += 1

    # Remove the given node from the list (still accessible via hashmap).
    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

        self.len -= 1


class LRUCache:
    def __init__(self, capacity: int):
        # Hashmap to map key to a linked list node (for O(1) key->value access).
        self.nodemap = {}
        # Linked list to maintain recency order of cache keys (for O(1) LRU removal).
        self.reclist = LinkedList(capacity)

    def get(self, key: int) -> int:
        # If given key is invalid, return -1.
        if key not in self.nodemap:
            return -1

        # Otherwise, find node corresponding to key.
        node = self.nodemap[key]

        # Make accessed key's node most recent in the recency list.
        self.reclist.remove(node)
        self.reclist.add(node)

        # Return value associated with the queried cache key.
        return node.val

    def put(self, key: int, value: int) -> None:
        # If the key exists, update its value.
        if key in self.nodemap:
            node = self.nodemap[key]
            self.reclist.remove(node)
            node.val = value
        # Otherwise, create a new node for the cache key.
        else:
            node = Node(value, key)
            self.nodemap[key] = node

        # Make the newly created/updated node most recent.
        self.reclist.add(node)

        # If cache size has exceeded its limit, remove least recent cache entry
        # i.e. one corresponding to first (head) node in the recency list.
        if self.reclist.len > self.reclist.maxlen:
            least_recent = self.reclist.left.next
            self.reclist.remove(least_recent)
            self.nodemap.pop(least_recent.key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
