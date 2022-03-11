class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        if len_s < 2:
            return s
        def findSubstring(s, start, end):
            while start>=0 and end<len(s) and s[start]==s[end]:
                start-=1
                end+=1
            return s[start+1:end]
        ans = ""
        for i in range(len_s):
            first = findSubstring(s, i, i)
            second = findSubstring(s, i, i+1)
            longestPalin = first if len(first) > len(second) else second
            if len(longestPalin) > len(ans):
                ans = longestPalin
        return ans
