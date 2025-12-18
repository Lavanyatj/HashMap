#https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isIsoMorphic(self, s: str, t:str):
        mapst,mapts = {},{}
        for c1,c2 in zip(s, t):
            if ((c1 in mapst and mapst[c1]!=c2) or (c2 in mapts and mapts[c2]!=c1)):
                return False
            mapst[c1] = c2
            mapts[c2] = c1
        return True
s = Solution()
print(s.isIsoMorphic("egg","add"))