/* finds a triplet whose sum is closest to a given target number in the given array */

#include <stdlib.h>

int closest_triplet_sum(int* arr, int len, int target);
int closest_duet_sum(int* arr, int len, int target);
unsigned int abs_val(int val);
int cmpfunc (const void * a, const void * b);

int threeSumClosest(int* nums, int numsSize, int target){
    int closest, sum, p1, p2, two_sum;
    closest = nums[0] + nums[1] + nums[2];

    qsort(nums, numsSize, sizeof(int), cmpfunc);

    for (int i = 0; i < numsSize - 2; ++i) {
        p1 = i + 1;
        p2 = numsSize - 1;

        while (p1 < p2) {
            two_sum = nums[p1] + nums[p2];
            sum = two_sum + nums[i];

            if (two_sum == target - nums[i])
                return sum;
            else if (two_sum > target - nums[i])
                p2--;
            else
                p1++;

            if (abs_val(target-sum) < abs_val(target-closest))
                closest = sum;
        }
    }
    return closest;
}

unsigned int abs_val(int val) {
    if (val < 0)
        return val * -1;
    else
        return val;
}

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}
