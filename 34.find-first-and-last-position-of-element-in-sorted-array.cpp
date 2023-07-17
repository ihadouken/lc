class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        /* Initialize result with Defaults. */
        vector<int> ret = {-1, -1};

        /* Handle empty input. */
        if (nums.size() == 0)
            return ret;

        int l, r, mid;
        l = 0;
        r = nums.size() - 1;

        /* Minimum three elements in the search space to continue searching. */
        while (l + 1 < r) {
            /* Minimize i such that nums[i] = target. */
            mid = l + (r - l) / 2;
            if (nums[mid] >= target)
                r = mid;
            else
                l = mid;
        }

        /* If we have just two elements in the input and they both equal target,
         * nums[l] will be the first occurence of target. Otherwise nums[r] = target
         * and the first occurence and nums[l] < target. */
        if (nums[l] == target)
            ret[0] = l;
        else if (nums[r] == target)
            ret[0] = r;

        l = 0;
        r = nums.size() - 1;
        while (l + 1 < r) {
            /* Maximize i such that nums[i] = target. */
            mid = l + (r - l) / 2;
            if (nums[mid] <= target)
                l = mid;
            else
                r = mid;
        }

        /* If we have just two elements in the input and they both equal target,
         * nums[r] will be the last occurence of target. Otherwise nums[l] = target
         * and the first occurence and nums[r] > target. */
        if (nums[r] == target)
            ret[1] = r;
        else if (nums[l] == target)
            ret[1] = l;

        return ret;
    }
};
