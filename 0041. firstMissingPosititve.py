  class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        di = {}
        n = len(nums)
        for i in range(1, n+1):
            di[i] = 0
        for i in range(n):
            if nums[i] > 0 and nums[i] < n+1:
                di[nums[i]] = 1
        for i in range(1, n+1):
            if di[i] == 0:
                return i
        return n+1
      
# Alternative cpp approach
# class Solution {
# public:
#     int firstMissingPositive(vector<int>& nums) {
#         int n = nums.size();
#         for (int i=0; i<n; ++i){
#             while(nums[i] != i+1){
#                 if (nums[i] <= 0 or nums[i] > n or nums[i] == nums[nums[i]-1]) 
#                     break;
#                 swap(nums[i], nums[nums[i]-1]);
#             }
#         }
#         for (int i=0; i<n; ++i){
#             if(nums[i] != i+1)
#                 return i+1;
#         }
#         return n+1;
#     }
# };
