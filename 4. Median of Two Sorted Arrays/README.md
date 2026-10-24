# 4. Median of Two Sorted Arrays

### Difficulty: Hard

## Description
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 
Example 1:


Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


Example 2:


Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


 
Constraints:


	nums1.length == m
	nums2.length == n
	0 <= m <= 1000
	0 <= n <= 1000
	1 <= m + n <= 2000
	-106 <= nums1[i], nums2[i] <= 106

## Submission Details
- **Status**: Accepted
- **Runtime**: 5
- **Memory**: 12636000
- **Language**: python

## Code
```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        length = len(merged)
        if length % 2 == 0:
            return float((merged[length/2] + merged[(length/2)-1])) / 2
        else:
            return merged[length//2]
```
