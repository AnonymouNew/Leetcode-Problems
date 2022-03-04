class Initializer:
    def __init__(self, nums=[]):
        self.nums = nums
class Solution:
    def threeSum(self, nums):
        visited = set()
        ans = set()
        l = len(nums)
        if l<3: return ans
        for i in range(l):
            for j in range(i+1,l):
                third = 0-nums[i]-nums[j]
                if third in visited:
                    arr = sorted([nums[i], nums[j], third])
                    ans.add((arr[0],arr[1],arr[2]))
            visited.add(nums[i])
        return ans
        
if __name__=="__main__":
    ob = Solution()
    inp = Initializer()
    val = input("nums = ")
    val = val[1:len(val)-1]
    val += ","
    print(val)
    cnt,t = 0,""
    while cnt<len(val):
        if val[cnt]==",":
            inp.nums.append(int(t))
            t=""
        else:
            t+=val[cnt]
        cnt+=1
    print(inp.nums)
    print(ob.threeSum(inp.nums))