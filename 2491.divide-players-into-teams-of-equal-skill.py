class Solution:
    # Approach: Hashmap, Complexity: O(n), O(n)
    # Tip: Store player in hashmap if it has no valid partner (for now). If found,
    #      consume partner from hashmap and update score. All players and their
    #      partners must sum to sum of weakest and strongest player.

    def dividePlayers(self, skill: List[int]) -> int:
        reqd_sum = min(skill) + max(skill)
        res = 0
        unteamed = {}

        for player in skill:
            partner = reqd_sum - player

            if partner in unteamed:
                res += player * partner
                if unteamed[partner] == 1:
                    unteamed.pop(partner)
                else:
                    unteamed[partner] -= 1
            else:
                unteamed[player] = unteamed.get(player, 0) + 1

        if unteamed:
            return -1
        return res

    # Approach: Sorting + Two Pointer, Complexity: O(nlogn), O(1)
    # Tip: Sort input so that weakest and strongest players align to the left
    #      and right respectively. Use two pointers at extreme ends to and
    #      greedily converge them to create teams of weak and strong players.

    # def dividePlayers(self, skill: List[int]) -> int:
    #     skill.sort()
    #     l, r = 0, len(skill) - 1
    #     res = 0
    #     reqd_sum = skill[l] + skill[r]
    #
    #     while l < r:
    #         if skill[l] + skill[r] != reqd_sum:
    #             return -1
    #
    #         res += skill[l] * skill[r]
    #         l += 1
    #         r -= 1
    #
    #     return res
