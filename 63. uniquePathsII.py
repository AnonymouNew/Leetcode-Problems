class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows, cols = len(obstacleGrid)+1, len(obstacleGrid[0])+1
        if obstacleGrid[rows-2][cols-2]: return 0
        ans = [[0] * cols for _ in range(rows)]
        ans[rows-2][cols-2] = 1
        for i in range(cols-3, -1, -1):
            if obstacleGrid[rows-2][i]:
                ans[rows-2][i] = 0
                break
            else: ans[rows-2][i] = 1
        for i in range(rows-3, -1, -1):
            for j in range(cols-2, -1, -1):
                if obstacleGrid[i][j]:
                    ans[i][j] = 0
                else:
                    ans[i][j] = ans[i+1][j] + ans[i][j+1]
        return ans[0][0]

if __name__ == "__main__":
    ob = Solution()
    inp = input("obstacleGrid = ")
    inp1, lis, val = [], [], 0
    for i in range(1, len(inp)-1):
        if inp[i]=="[": val = 0
        elif inp[i]=="]":
            lis.append(val)
            inp1.append(lis)
            lis, val = [], 0
        elif inp[i]==",":
            if inp[i-1]!="]":
                lis.append(val)
                val = 0
        else: val = val*10 + int(inp[i])
    print(ob.uniquePathsWithObstacles(inp1))
