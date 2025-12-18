#https://leetcode.com/problems/two-sum/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement],i]
            seen[num] = i
s = Solution()
print(s.twoSum([2,7,11,15],9))