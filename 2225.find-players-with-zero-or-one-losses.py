class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Create two arrays to store both types of players.
        not_lost, lost_one = [], []
        # Hashmap to keep track of matches lost by every player.
        losses = {}

        # Iterate over all match results.
        for winner, loser in matches:
            # Make sure winners are initialized with 0 losses.
            if winner not in losses:
                losses[winner] = 0
            # Increment count for loser (or initialize with 1).
            losses[loser] = losses.get(loser, 0) + 1

        # Find lowest and highest (by ID) players that played at least one match.
        first, last = min(losses), max(losses)

        # Iterate over all players that were active.
        for player in range(first, last+1):
            # Ignore players in between that didn't play any matches.
            if player not in losses:
                continue

            # Check if a player matches one of the two criterias.
            if losses[player] == 0:
                not_lost.append(player)
            elif losses[player] == 1:
                lost_one.append(player)

        # Return the two desired lists of players.
        return [not_lost, lost_one]
