class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        num_1 = nums[-k:]
        num_2 = nums[:-k]
        nums[:] = num_1+num_2
        return nums

sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
print(sol.rotate(nums, k))

nums_1 = [-1,-100,3,99]
k_1 = 2
print(sol.rotate(nums_1, k_1))

nums_2 = [1,2]
k_2 = 3
print(sol.rotate(nums_2,k_2))