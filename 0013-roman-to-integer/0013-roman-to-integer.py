class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        num = 0
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)-1,-1,-1):
            if dic[s[i]] >= num:
                num = dic[s[i]]
                ans += dic[s[i]]
            else:
                ans -= dic[s[i]]
        return ans
            


        