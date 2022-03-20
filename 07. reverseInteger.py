class Solution:
    def reverse(self, x: int) -> int:
        flag, ans = 0, 0
        if x < 0:
            flag = 1
            x*=-1
        if x > 2**31 - 1: return 0
        str1 = str(x)
        str1 = str1[::-1]
        for i in str1:
            ans = ans*10 + int(i)
        if ans > 2**31 - 1: return 0
        if flag: ans *= -1
        return ans
