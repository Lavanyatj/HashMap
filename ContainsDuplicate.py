#https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def containDuplicate(self, nums: List[int], k):
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i -seen[num] <=k:
                return True
            seen[num] = i
        return False
s = Solution()
print(s.containDuplicate([1,2,3,1],3))