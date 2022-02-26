class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        ans = 0.0
        nums = []
        l1 = len(nums1)
        l2 = len(nums2)
        length = len(nums1) + len(nums2)
        i, j = 0, 0
        while i<l1 and j<l2:
            if nums1[i]<=nums2[j]:
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j += 1
        while i<l1:
            nums.append(nums1[i])
            i += 1
        while j<l2:
            nums.append(nums2[j])
            j += 1
        mid = (int)(length/2)
        if (length & 1):
            ans = nums[mid]            
        else:
            ans = (nums[mid-1] + nums[mid])/2.0            
        return ans
        
if __name__ == "__main__":
    tmp1 = input()
    tmp2 = input()
    nums1, nums2 = [], []
    val = 0
    for i in range(1, len(tmp1)-1):
        if tmp1[i]==",":
            nums1.append(val)
            val = 0
        else:
            val = val*10 + int(tmp1[i])
    nums1.append(val)
    val = 0
    for i in range(1, len(tmp2)-1):
        if tmp2[i]==",":
            nums2.append(val)
            val = 0
        else:
            val = val*10 + int(tmp2[i])
    nums2.append(val)
    obj = Solution()
    ans = obj.findMedianSortedArrays(nums1, nums2)
    print(ans)