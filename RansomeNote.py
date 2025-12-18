#https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        freq = Counter(magazine)
        for ch in ransomNote:
            if freq[ch] == 0:
                return False
            freq[ch] -=1
        return True
ransom = Solution()
print(ransom.canConstruct("aa", "aab"))

# using fixed size
class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str):
        freq = [0] * 26
        for ch in magazine:
            freq[ord(ch)-ord('a')] +=1
        for ch in ransomNote:
            idx = ord(ch)-ord('a')
            if freq[idx] == 0:
                return False
            freq[idx] -=1
        return True

ransom1 = Solution1()
print(ransom1.canConstruct("aa", "aab"))

# using dictionary
class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str):
        freq = {}
        for ch in magazine:
            freq[ch] = freq.get(ch,0) + 1
        for ch in ransomNote:
            if freq.get(ch,0) == 0:
                return False
            freq[ch] -=1
        return True
ransom2 = Solution2()
print(ransom2.canConstruct("aa","aab"))
