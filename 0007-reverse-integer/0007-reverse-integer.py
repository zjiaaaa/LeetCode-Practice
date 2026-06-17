class Solution:
    def reverse(self, x: int) -> int:
        num = -1 if x < 0 else 1
        ans = 0
        if num == -1:
            x *= -1
        while x != 0:
            k = x % 10             
            ans = ans * 10 + k
            x = x // 10
        if ans < (-2)**31 or ans > (2**31)-1:
            return 0
        return ans * num