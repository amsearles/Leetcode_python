"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
"""

#first brute-forced solution
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        B = []
        for x in range(len(A)):
            if A[x]%2 == 0:
                B.append(A[x])
        
        for x in range(len(A)):
            if A[x]%2 == 1:
                B.append(A[x])
                
        return B
#Common theme among these is everything can be done in a line or two.
#second solution while trying to do it only in the return statement. No need to create an entirely new array for it.
#This solution is only one line but its slower and uses slightly more memory
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
       return ([x for x in A if x%2 == 0] + [x for x in A if x%2 == 1])
