class Solution{
  public:
    string countAndSay(int n){
      string ans;
      if(n==1) return "1";
      ans = countAndSay(--n);
      string final_ans;
      for(int i=0; i<ans.length(); ++i) {
        char cnt = '1';
        while(ans[i]==ans[i+1]) {
          cnt++; i++;
        }
        final_ans+=cnt;
        final_ans+=ans[i];
      }
      return final_ans;
    }
};
