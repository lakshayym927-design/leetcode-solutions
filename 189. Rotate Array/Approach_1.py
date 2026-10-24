class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        if(k == 0):
            return nums
        k = k % n
        nums[:] = nums[n-k:n] + nums[0:n-k]
        return nums