'''

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

'''
from typing import List

nums = [1, 2, 3,4]


# print(len(set(sorted(nums))))

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if len(set(sorted(nums)))!=len(nums):
            return 'true'
         
        return 'false'
         
    
         


a=Solution()

print(a.hasDuplicate(nums))