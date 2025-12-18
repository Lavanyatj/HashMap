#https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True

st = Solution()
print(st.isAnagram("anagram","nagaram"))
