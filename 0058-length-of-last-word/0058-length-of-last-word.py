class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1,-1,-1):
            if not s[i].isspace():
                ans +=1
            else:
                if ans != 0:
                    break
        return ans


        