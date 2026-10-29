class Solution(object):
    def isPerfectSquare(self, num):
        if num == 1:
            return True
        si = 1
        ei = num-1
        while si <= ei:
            if si == ei and si*si == num:
                return True
            mid = si + (ei-si)//2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                ei = mid-1
            else:
                si = mid+1
        
        return False