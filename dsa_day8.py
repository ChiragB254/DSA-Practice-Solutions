class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)
        low = 0
        high = n-1
        self.count  = 1

        def sort(arr,high,low):

            if high >= low:
                mid = low + (high-low) // 2
                

                if len(arr[low:mid-1])> 1 and arr[mid-1] >= arr[mid-2]:
                    self.count  +=1
                    return sort(arr = arr[:mid-1], low = low, high = mid-1)
                # else:
                #     self.count+=1
                
                if len(arr[mid:high])>1 and arr[mid] <= arr[mid+1]:
                    self.count  +=1
                    return sort(arr = arr[mid:], high = high, low = mid)
                # else:
                #     self.count+=1
        sort(arr,high = high, low = low)    
        return self.count
            





# class Solution:
#     def maxChunksToSorted(self, arr: List[int]) -> int:
#         max_seen = 0  # Initialize the maximum value seen so far
#         chunks = 0  # Initialize the count of chunks
        
#         for i, num in enumerate(arr):
#             max_seen = max(max_seen, num)  # Update the maximum value seen so far
#             if i == max_seen:  # If the current index equals the maximum value seen so far
#                 chunks += 1  # Increment the count of chunks
        
#         return chunks
