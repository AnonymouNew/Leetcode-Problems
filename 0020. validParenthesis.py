class Solution:
    def isValid(self, s):
        while "{}" in s or "[]" in s or "()" in s:
            s = s.replace("{}", "").replace("[]", "").replace("()", "")
        if s=="": return True
        return False

if __name__=="__main__":
    ob = Solution()
    s = input("s = ")
    s = s[1:len(s)-1]
    print(ob.isValid(s))
