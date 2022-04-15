#define m 1000000007;
class Solution {
public:
    int dp[100001];
    int solve(string &s, int idx, int k) {
        if(idx==s.size()) return 1;
        if(dp[idx]!=-1) return dp[idx];
        if(s[idx]=='0') return 0;
        long long val = 0;
        int ans = 0;
        for(int j=idx; j<s.size(); ++j) {
            val = val*10 + s[j]-'0';
            if(val>k) break;
            ans += solve(s,j+1,k);
            ans %= m;
        }
        return dp[idx] = ans;
    }
    int numberOfArrays(string s, int k) {
        for(int i=0; i<s.size(); ++i) dp[i] = -1;
        return solve(s,0,k);
    }
 };
