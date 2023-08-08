class Solution {
public:
    /* Approach: Sorting + Two Pointer, Complexity: O(nlogn + mlogm), O(1) */
    /* Tip: Sort both arrays. Use two pointers traversing the two arrays at the
     *      same time. Move the pointer which points at a smaller element and 
     *      then move. Pointer to smaller element is moved as it is still 
     *      possible to find the larger element in other array but it is not 
     *      possible to find the smaller element to the right of a larger
     *      element as the arrays are sorted. When a match is found, keep
     *      moving one of the pointers till it points t oa different value
     *      to avoid duplicates.
     */

    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());

        vector<int> common;
        int i, j;
        i = j = 0;

        while (i < nums1.size() && j < nums2.size()) {
            if (nums1[i] < nums2[j])
                ++i;
            else if (nums1[i] > nums2[j])
                ++j;
            else {
                common.push_back(nums1[i]);
                while (i < nums1.size() && nums1[i] == nums2[j])
                    ++i;
            }
        }
        return common;
    }
};
