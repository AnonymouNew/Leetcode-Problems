class Solution {
public:
    string convert(string s, int r) {
        int n = s.size();
        if(r==1 || r>=n)
            return s;
        string ans = "";
        for(int i=0;i<n;i+=2*(r-1))
            ans += s[i];
        for(int i=1;i<r-1;i++) {
            int b = r-1,x = i;
            while(x<n) {
                ans += s[x];
                if(b==r-1)
                    x += 2*(b-i), b = 0;
                else
                    x += 2*(i-b), b = r-1;
            }
        }
        for(int i=r-1;i<n;i+=2*(r-1))
            ans += s[i];
        return ans;
    }
};
