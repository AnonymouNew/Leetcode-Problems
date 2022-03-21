# Using regex
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip() ; s = re.findall('(^[\+\-0]*\d+)\D*', s)
        try:
            ans = int(''.join(s))
            return -2**31 if ans < -2**31 else 2**31-1 if ans > 2**31-1 else ans
        except: return 0
