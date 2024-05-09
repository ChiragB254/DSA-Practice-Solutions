# Squares of a Sorted Array

"""https://leetcode.com/problems/squares-of-a-sorted-array

***********************************************************
Time Complexity - O(nlog n)
Space Complexity - O(n)
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            ele = nums[i]**2
            nums[i] = ele
        return(sorted(nums))
    

# Main
nums = [-4,-1,0,3,10]
print(Solution().sortedSquares(nums))

nums = [-7,-3,2,3,11]
print(Solution().sortedSquares(nums))
    
