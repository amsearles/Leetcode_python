#Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        B = []
        for x in range(len(A)):
            B.append(A[x]**2)
        
        return sorted(B)
        
