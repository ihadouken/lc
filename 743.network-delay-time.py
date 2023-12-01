import heapq as hq

class Solution:
    # Approach: Graphs + Dijkstra's Algorithm, Complexity: O(elogv), O(e+v)
    # Tip: Visualize the network as a graph. Finding the time taken for signal to
    #      reach every node is same as finding time taken to reach last node as
    #      the signal propagates to all of a node's neighbours simultaneously.

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Convert the edge list into an adjacency list (taking O(e+v) space).
        adj = [[] for _ in range(n+1)]
        for src, dest, weight in times:
            adj[src].append((dest, weight))

        # Use a heap to keep track of the cheapest edge.
        heap = []
        # Hashmap to store lowest costs (as they are found) for nodes.
        costs = {}
        # Zero cost to reach the source node.
        hq.heappush(heap, (0, k))

        # Continue until no edges are left unseen.
        while heap:
            # Process the cheapest unseen edge.
            w1, cur = hq.heappop(heap)

            # If the least cost has already been found for a node, ignore all
            # later found costs as they will always be higher.
            if cur in costs:
                continue

            # As the cheapest edges are being chosen, every chosen edge is best
            # way to reach the node pointed by it.
            costs[cur] = w1

            # Add all outgoing edges from the current node to the heap. Cost borne
            # by an edge = cost(source -> current node) + cost(current -> neighbour)
            # where cost(source -> current node) is has already been computed above.
            for neighbour, w2 in adj[cur]:
                hq.heappush(heap, (w1+w2, neighbour))

        # If a node's cost is uncomputed, it is unreachable from the source.
        if len(costs) < n:
            return -1
        # Return the time taken to reach the last reached node i.e. max cost.
        return max(list(costs.values()))
