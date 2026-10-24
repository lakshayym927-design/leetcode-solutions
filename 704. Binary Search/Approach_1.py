class Solution(object):
    def search(self, nums, target):
        si = 0
        ei = len(nums)-1
        while si <= ei:
            mid = si + (ei - si) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                ei = mid-1
            elif nums[mid] < target:
                si = mid+1

        return -1