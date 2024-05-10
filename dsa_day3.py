# Day 3

# Description: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.


'''
Time Complexity = O(n)

Explain - We are doing sum of sum of first 2 consecutive elements then we are saving their result in a variable
then we are checking if that sum is greater than the next number if not it will store that number are the current max
and then we check if that number is greater than then the max sum if not that replace it with current sum else max sum will remain same
'''


class Solution:
    def maxSubArray(self,nums: list[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1,len(nums)):
             current_sum = max(nums[i],current_sum+nums[i])
             max_sum = max(max_sum,current_sum)
        return max_sum
		


# Test Case
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(s.maxSubArray([1])) # 1
print(s.maxSubArray([-1])) # -1
print(s.maxSubArray([-2147483647])) # -2147483647
print(s.maxSubArray([5,4,-1,7,8])) # 23
print(s.maxSubArray([-2,1])) # 1
print(s.maxSubArray([-2,-1])) # -1
print(s.maxSubArray([1,2])) # 3
print(s.maxSubArray([1,2,3])) # 6