class Solution {
public:
    /* Pair is not hashable so convert to string for adding into hashset. */
    string pair2str(pair<int, int> pair) {
        return to_string(pair.first) + ',' + to_string(pair.second);
    }

    /* Approach: Hashset, Complexity: O(n), O(n) */
    bool isPathCrossing(string path) {
        /* Hashset to store already visited positions. */
        unordered_set<string> visited;
        /* Store current position in as pair of coordinates i.e. (x, y) */
        pair<int, int> pos;
        pair<int, int> move;
        unordered_map<char, pair<int, int>> moves;

        /* Map change in position (dx, dy) associated with moves. */
        moves['N'] = {0, -1};
        moves['S'] = {0, 1};
        moves['W'] = {-1, 0};
        moves['E'] = {1, 0};

        /* Start off at (0, 0) */
        pos.first = pos.second = 0;
        /* Record initial position in hashset. */
        visited.insert(pair2str(pos));

        /* Traverse the path. */
        for (int i = 0; i < path.length(); ++i) {
            /* Lookup movement (dx, dy) associated with direction. */
            move = moves[path[i]];
            /* Calculate new position. */
            pos.first += move.first;
            pos.second += move.second;

            /* Return true if current position was visited before. */
            if (visited.find(pair2str(pos)) != visited.end())
                return true;
            /* Record current position in hashset. */
            visited.insert(pair2str(pos));
        }

        /* Return false if no position is repeated. */
        return false;
    }
};
