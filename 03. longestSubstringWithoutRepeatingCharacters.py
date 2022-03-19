class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, cnt, l = 1, 0, len(s)
        if s=="": return 0
        end = l
        for i in range(end):
            cnt = 1
            tst = dict()
            val = s[i]
            tst[val] = 1
            for j in range(i+1, l):
                if s[j] in tst:
                    break
                else:
                    cnt += 1
                    val = s[j]
                    tst[val] = 1
                    if ans<cnt:
                        ans = cnt
                        end = end-ans+1
        return ans
