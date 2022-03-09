class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_l = 500
        cnt=0
        ans = ""
        for i in strs:
            cnt+=1
            min_l = min(min_l,len(i))
        for i in range(min_l):
            chr1 = strs[0][i]
            cnt1=0
            for str in strs:
                if str[i]==chr1:
                    cnt1+=1
                else:
                    break
            if cnt1==cnt:
                ans+=strs[0][i]
            else:
                return ans
        return ans