# Approach 1:  Brute Force
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A=[]):
            if len(A)==2*n:
                if isValid(A): ans.append("".join(A))
            else:
                A.append("(")
                generate(A)
                A.pop()
                A.append(")")
                generate(A)
                A.pop()
        def isValid(A):
            left = 0
            for i in A:
                if i == "(": left += 1
                else: left -= 1
                if left < 0: return False
            return left == 0
        ans=[]
        generate()
        return ans
      
     # Approach 2: Using Backtracking
    class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S)==2*n:
                ans.append("".join(S))
                return 
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans
