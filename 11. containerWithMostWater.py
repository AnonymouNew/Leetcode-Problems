class Initializer:
    def __init__(self, height=[]):
        self.height = height
class Solution:
    def maxArea(self, height):
        area = 0
        l = len(height)
        start, end = 0, l-1
        for i in range(l):
            val = min(height[start], height[end])*(end-start)
            area = max(area, val)
            if(height[start]<height[end]):
                start+=1
            else: end-=1
        return area

if __name__ == "__main__":
    
    s = input()
    i, n = 0, len(s)
    s = s[1:n-1]
    s += ","
    ob = Solution()
    inp = Initializer()
    for word in s.split(","):
        if word.isdigit():
            inp.height.append(int(word))
    print(ob.maxArea(inp.height))