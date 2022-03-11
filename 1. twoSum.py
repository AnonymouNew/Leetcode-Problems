class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()
        for idx, val in enumerate(nums):
            remain = target - val
            if remain in visited:
                return [visited[remain], idx]
            visited[val] = idx
        
