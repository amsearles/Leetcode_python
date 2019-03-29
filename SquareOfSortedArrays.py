#Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

# first solution, terrible. I have to keep in mind the most simplest and efficient solution and not overthink
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        B = []
        for x in range(len(A)):
            B.append(A[x]**2)
        
        return sorted(B)
        
#second solution, time complexity is O(NlogN)
class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)
