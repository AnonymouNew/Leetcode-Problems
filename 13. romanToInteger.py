class Solution:
    def romanToInt(self, s: str) -> int:
        di = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'D': 500, 'M': 1000, 'C': 100} 
        ans = di[s[-1]]
        l = len(s)
        for i in range(l-2, -1, -1):
            if di[s[i]] < di[s[i+1]]: ans -= di[s[i]]
            else: ans += di[s[i]]
        return ans
