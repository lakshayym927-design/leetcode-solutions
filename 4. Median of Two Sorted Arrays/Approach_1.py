class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        length = len(merged)
        if length % 2 == 0:
            return float((merged[length/2] + merged[(length/2)-1])) / 2
        else:
            return merged[length//2]