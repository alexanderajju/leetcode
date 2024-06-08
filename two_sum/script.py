from typing import List
nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,j in enumerate(nums):
            for x,y in enumerate(nums):
                if j+y==target and i!=x:
                    return [i,x]
            

    



a=Solution()
print(a.twoSum(nums=nums,target=target))