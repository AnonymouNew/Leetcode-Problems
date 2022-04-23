class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = defaultdict(list)
        dic1 = defaultdict(list)
        for i, j in edges:
            dic1[j].append(i)
        
        def dfs(node):
            if node in ans:
                return ans[node]
            
            for neighbour in dic1[node]:
                ans[node] += [neighbour] + dfs(neighbour)
            
            ans[node] = list(set(ans[node]))
            
            return ans[node]
        
        for i in range(n):
            dfs(i)
        
        return [sorted(ans[i]) for i in range(n)]
