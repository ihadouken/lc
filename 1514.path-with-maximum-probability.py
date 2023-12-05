class Solution:
    # Approach: Dijkstra's Algorithm + Heap + Hashmap, Complexity: O(elogv), O(e)
    # Note: Python only supports minheaps but the edge with max probability must
    #       be tracked which normally requires a maxheap. So, negated probs. are
    #       used with minheap which ends up emulating a maxheap as if a > b holds,
    #       -a < -b will also hold.

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Build adjacency list out of list of undirected edges.
        adj = [[] for _ in range(n)]
        for (src, dest), prob in zip(edges, succProb):
            adj[src].append((-prob, dest))
            adj[dest].append((-prob, src))

        # Use heap to keep track of edge with max. probablity.
        heap, max_success = [], {}
        heapq.heappush(heap, (-1, start_node))

        while heap:
            # Select the edge with max. probability.
            prob, cur = heapq.heappop(heap)

            # If a better probability path if found for cur, leave it be.
            if cur in max_success:
                continue
            # Else, store this probability as the best possible for cur.
            max_success[cur] = prob

            # Add all edges outgoing from cur.
            for nei_prob, neighbour in adj[cur]:
                if neighbour not in max_success:
                    heapq.heappush(heap, (-prob*nei_prob, neighbour))

        # If end_node is unreachable from start_node, it wont be in max_success.
        if end_node not in max_success:
            return 0
        # Remember to undo the negated probability when returning.
        return -max_success[end_node]
