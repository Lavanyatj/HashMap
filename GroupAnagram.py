#https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagram(self, strs: List[str])-> List[str]:
        groupanagram_map = defaultdict(list)
        for words in strs:
            sorted_word = "".join(sorted(words))
            groupanagram_map[sorted_word].append(words)
        return list(groupanagram_map.values())

s = Solution()
print(s.groupAnagram(["eat","tea","tan","ate","nat","bat"]))
