class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        t = 100001
        cnt = [0]*t
        freq = [0]*t
        n = len(nums)
        for i in range(n):
            cnt[nums[i]] += 1
            freq[cnt[nums[i]]] += 1
        for i in range(n-1, -1, -1):
            if (freq[cnt[nums[i]]] * cnt[nums[i]]) == i: return i+1
            freq[cnt[nums[i]]] -= 1
            cnt[nums[i]] -= 1
            if (freq[cnt[nums[i-1]]] * cnt[nums[i-1]]) == i: return i+1
        return 1
