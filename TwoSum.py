"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

"""
class Solution(object):
    def twoSum(self, nums, target):
        for idx, val in enumerate(nums):
            for idx2 in range(idx+1, len(nums)):
                val2 = nums[idx2]
                if ((val+val2)==target):
                    return [idx, idx2]
