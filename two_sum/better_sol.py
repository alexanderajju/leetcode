from typing import List
nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [pair_idx[target - num],i]
            pair_idx[num] = i
            
        # print(mapper)



a=Solution()
print(a.twoSum(nums=nums,target=target))