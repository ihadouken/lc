class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Use a hashmap to store/lookup subordinates of every manager.
        subs = collections.defaultdict(list)
        for emp, manager in enumerate(manager):
            subs[manager].append(emp)

        def dfs(emp: int) -> int:
            # Initialize reporting time.
            time = 0

            # Select the upper bound of propagation time of all subtrees.
            for sub in subs[emp]:
                time = max(time, dfs(sub))

            # Total time = inform time + propagation time.
            return time + informTime[emp]

        # Initialize DFS on the head of the organization.
        return dfs(headID)
