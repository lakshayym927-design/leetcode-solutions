# 367. Valid Perfect Square

### Difficulty: Easy

## Description
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

 
Example 1:


Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.


Example 2:


Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.


 
Constraints:


	1 <= num <= 231 - 1

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 12048000
- **Language**: python

## Code
```python
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
```
