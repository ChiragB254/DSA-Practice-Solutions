class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        dicts = {}
        nby3 = len(nums)//3
        lis = []
        for num in nums:
            if num in dicts:
                dicts[num] +=1
            else:
                dicts[num] = 1
        for key, value in dicts.items():
            if value >nby3:
                lis.append(key)
        return(lis)


"""
An Optimal solutin, where we are using collections library and using only one four loop 
"""

from collections import Counter

class Solution2:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # Count the occurrences of each number using Counter
        counts = Counter(nums)
        
        # Calculate the threshold for a majority element
        nby3 = len(nums) // 3
        
        # Filter out elements whose count is greater than n/3
        majority_elements = [num for num, count in counts.items() if count > nby3]
        
        return majority_elements