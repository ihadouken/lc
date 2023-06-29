class Solution {
    int abs(int num) {
        if (num < 0)
            return num * -1;
        return num;
    }

    public int[] sortedSquares(int[] nums) {
        int i, min, l, r;
        min = 0;
        for (i = 1; i < nums.length; ++i) {
            if (abs(nums[min]) > abs(nums[i]))
                min = i;
        }

        int result[] = new int[nums.length];
        i = 0;
        result[i] = nums[min] * nums[min];
        i++;

        l = min - 1;
        r = min + 1;
        while(l >= 0 || r < nums.length) {
            if (l < 0 || (r < nums.length && (nums[r] * nums[r] < nums[l] * nums[l]))) {
                result[i] = nums[r] * nums[r];
                r++;
            }
            else {
                result[i] = nums[l] * nums[l];
                l--;
            }
            i++;
        }
        return result;
    }
}
