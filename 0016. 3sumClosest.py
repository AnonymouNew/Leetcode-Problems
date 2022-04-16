class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")
        for num, val in enumerate(nums):
            low, high = num+1, len(nums)-1
            while low < high:
                sum3 = val + nums[low] + nums[high]
                if abs(target - sum3) < abs(diff):
                    diff = (target - sum3)
                if sum3 < target:
                    low += 1
                else:
                    high -= 1
            if diff == 0: break
        return target - diff
