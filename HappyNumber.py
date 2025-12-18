#https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isHappy(self, n:int)-> bool:
        seen = set()
        while n !=1:
            if n in seen:
                return False # cycle deducted
            seen.add(n)
            n =sum(map(lambda x : int(x) ** 2, str(n)))
        return True
s = Solution()
print(s.isHappy(19))