class Solution(object):
    def searchInsert(self, nums, target):
        si = 0
        ei = len(nums)-1
        while si < ei:
            mid = si + (ei - si) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target :
                si = mid +1
            else :
                ei = mid -1

        if nums[si] < target:
            return si+1
        else:
            return si