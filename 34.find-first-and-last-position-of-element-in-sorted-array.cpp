class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ret = {-1, -1};
        if(nums.size() == 0) return ret;
        
        int l = 0, r = nums.size() - 1, mid;
        while (l + 1 < r) {
            mid = l + (r - l) / 2;
            if (nums[mid] >= target) {
                r = mid;
            } else {
                l = mid;
            }
        }
        
        if (nums[l] == target) {
            ret[0] = l;
        } else if (nums[r] == target) {
            ret[0] = r;
        }
        
        l = 0;
        r = nums.size() - 1;
        while (l + 1 < r) {
            mid = l + (r - l) / 2;
            if (nums[mid] <= target) {
                l = mid;
            } else {
                r = mid;
            }
        }
        
        if (nums[r] == target) {
            ret[1] = r;
        } else if (nums[l] == target) {
            ret[1] = l;
        }
        
        
        
        return ret;
    }
};
