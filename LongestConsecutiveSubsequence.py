#https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def longestConsSeq(self, nums:List[int])-> int:
        nums = set(nums)
        longest = 0
        for x in nums:
            if x-1 not in nums:
                y = x+1
                while y in nums:
                    y +=1
                longest = max(longest, y-x)
        return longest

s = Solution()
print(s.longestConsSeq([100,4,200,1,3,2]))
