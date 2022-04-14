class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, tmp = [], []
        nums.sort()
        def kSum(k, target, start):
            if k!=2:
                for i in range(start, len(nums)-k+1):
                    if i > start and nums[i]==nums[i-1]:
                        continue
                    tmp.append(nums[i])
                    kSum(k-1, target-nums[i], i+1)
                    tmp.pop()
                return
            # executing 2 sum
            l, r = start, len(nums) -1
            while l < r:
                if nums[l] + nums[r] < target: l += 1
                elif nums[l] + nums[r] > target: r -= 1
                else:
                    ans.append(tmp + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                
        kSum(4, target, 0)   
        return ans
