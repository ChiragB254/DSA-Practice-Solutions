class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product = nums[0]
        current_product = nums[0]
        min_product = nums[0]

        for index in range(1,len(nums)):
            temp = max(max(nums[index], nums[index] * max_product),nums[index] * min_product)
            min_product = min(min(nums[index], nums[index] * max_product), nums[index] * min_product)
            max_product = temp
            current_product = max(current_product,max_product)
        return current_product
