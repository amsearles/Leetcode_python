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
