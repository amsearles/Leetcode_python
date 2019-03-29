"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.
"""


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        result = [None] * len(A) #creating empty list with same length as A
        result[::2] = (x for x in A if x%2 == 0) #for every even index, add an even integer
        result[1::2] = (x for x in A if x%2 == 1) #for every odd index, add an odd integer
        return result
