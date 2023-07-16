class NumArray {
public:
    std::vector<int> prefix = {0};

    NumArray(vector<int>& nums) {
        int i, sum;
        sum = 0;

        for (i = 0; i < nums.size(); ++i) {
            sum += nums[i];
            prefix.push_back(sum);
        }
    }

    int sumRange(int left, int right) {
        return prefix[right+1] - prefix[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */
