import re 
class Solution:
    def isMatch(self, s, p):
        return re.match(p+"$", s)!=None
        
if __name__ == "__main__":
    ob = Solution()
    s = input()
    s = s[1:len(s)-1]
    p = input()
    p = p[1:len(p)-1]
    print(ob.isMatch(s, p))