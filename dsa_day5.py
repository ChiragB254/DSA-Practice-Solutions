class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums = sorted(nums)
        nby2 = len(nums)//2
        return nums[nby2]

# Day 5 code


