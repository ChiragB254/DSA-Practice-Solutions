# # Partial Success

# class Solution:
#     def nextGreaterElement(self, n: int) -> int:
#         if len(str(n)) < 2:
#             return -1
#         if len(str(n)) == 2:  
#             if int(str(n)[0]) >= int(str(n)[1]):
#                 return -1
#         i = 0
#         j = len(str(n)) - 1
#         list_1 = ['0'] * (j+1)

#         while i < j:
#             if int(str(n)[i]) < int(str(n)[j]):
#                 list_1[i] = str(n)[j]
#                 list_1[j] = str(n)[i]
#                 i += 1
#                 j -= 1
#             else:
#                 list_1[i] = str(n)[i]
#                 list_1[j] = str(n)[j]
#                 i += 1
#                 j -= 1 

#         if int(''.join(list_1)) >= 2**31:
#             return -1
#         if n > int(''.join(list_1)):
#             return -1
#         else:
#             return int(''.join(list_1))
        

'''
https://algo.monster/liteproblems/556

'''

class Solution:
    def nextGreaterElement(self, num: int) -> int:
        # Convert the number to a list of characters for easy manipulation
        char_list = list(str(num))
        length = len(char_list)
      
        # Start from the second last element and move backward to find the first element which is smaller than its next element
        i = length - 2
        while i >= 0 and char_list[i] >= char_list[i + 1]:
            i -= 1
          
        # If we can't find such an element, it means the number cannot be greater in its permutation
        if i < 0:
            return -1
      
        # Now find an element which is greater than the found element at i
        j = length - 1
        while char_list[i] >= char_list[j]:
            j -= 1
      
        # Swap these two elements
        char_list[i], char_list[j] = char_list[j], char_list[i]
      
        # Reverse the sublist after the index i to get the next greater element in terms of permutation
        char_list[i + 1 :] = char_list[i + 1:][::-1]
      
        # Convert the char list back to an integer
        next_greater = int(''.join(char_list))
      
        # If the next greater number is bigger than the largest 32-bit integer, return -1
        return next_greater if next_greater <= 2**31 - 1 else -1