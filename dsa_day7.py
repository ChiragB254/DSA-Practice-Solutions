# Partial Success

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if len(str(n)) < 2:
            return -1
        if len(str(n)) == 2:  
            if int(str(n)[0]) >= int(str(n)[1]):
                return -1
        i = 0
        j = len(str(n)) - 1
        list_1 = ['0'] * (j+1)

        while i < j:
            if int(str(n)[i]) < int(str(n)[j]):
                list_1[i] = str(n)[j]
                list_1[j] = str(n)[i]
                i += 1
                j -= 1
            else:
                list_1[i] = str(n)[i]
                list_1[j] = str(n)[j]
                i += 1
                j -= 1 

        if int(''.join(list_1)) >= 2**31:
            return -1
        if n > int(''.join(list_1)):
            return -1
        else:
            return int(''.join(list_1))
        
