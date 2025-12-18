#https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def wordPattern(self, pattern:str, word:str) -> bool:
        mapPS,mapSP = {},{}
        if (len(pattern) != len(word.split())):
            return False
        for c1, c2 in zip(pattern, word.split()):
            if ((c1 in mapPS and mapPS[c1] != c2) or (c2 in mapSP and mapSP[c2] != c1)):
                return False
            mapPS[c1] = c2
            mapSP[c2] = c1
        return True

s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))
