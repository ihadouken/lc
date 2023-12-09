class Solution:
    # Approach: Priority Queue (minheap), Complexity: O(nlogm), O(m)
    # where, m -> number of servers, n -> number of tasks.
    # Note: Popping from and appending to a heap of size m costs logm.
    #       Both operations are done n times each on both heaps.

    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # Initialize time to 0 and current task to index 0.
        cur_task = time = 0
        res = []
        # Busy queue is empty as all servers are ready at t=0.
        busy_pq = []

        # Construct a priority queue to efficiently select server with min weight.
        ready_pq = [(srv_w, srv_i) for srv_i, srv_w in enumerate(servers)]
        heapq.heapify(ready_pq)

        # Continue until all tasks are processed.
        while cur_task < len(tasks):
            # Move servers from busy to ready queue when they complete a task.
            # To release servers immediately at release time, this is the first
            # to do in the loop. Busy queue is also implemented via minheap so
            # that ones who finish first get evicted first and get back to work.
            while busy_pq and busy_pq[0][0] <= time:
                _, srv_w, srv_i = heapq.heappop(busy_pq)
                heapq.heappush(ready_pq, (srv_w, srv_i))

            # If no server is available, fast forward time to release time of
            # first server in busy queue.
            if not ready_pq:
                time = busy_pq[0][0]
            else:
                # Select the minimum weight server from the available servers.
                srv_w, srv_i = heapq.heappop(ready_pq)

                # Add server to the busy queue with its respective release time.
                free_time = time + tasks[cur_task]
                heapq.heappush(busy_pq, (free_time, srv_w, srv_i))

                # Record index of the server who got assigned the task.
                res.append(srv_i)
                # Move on to the next task.
                cur_task += 1

                # Increment time if time and index of current task were same at
                # the starting of the iteration.
                if cur_task > time:
                    time += 1

        # res[i] is the index of server assigned the ith task.
        return res
