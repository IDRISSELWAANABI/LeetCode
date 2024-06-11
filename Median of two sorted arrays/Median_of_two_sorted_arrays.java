class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int i = 0, j = 0;
        List<Integer> res = new ArrayList<>();

        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] <= nums2[j]) {
                res.add(nums1[i]);
                i++;
            } else {
                res.add(nums2[j]);
                j++;
            }
        }
        while (i < nums1.length) {
            res.add(nums1[i]);
            i++;
        }
        while (j < nums2.length) {
            res.add(nums2[j]);
            j++;
        }

        int len = res.size();
        if (len % 2 != 0) {
            return res.get(len / 2);
        } else {
            return (res.get((len / 2) - 1) + res.get(len / 2)) / 2.0;
        }
    }
}
