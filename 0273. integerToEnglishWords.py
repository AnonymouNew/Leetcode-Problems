class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0: return "Zero"
        di = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 
              7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 
              30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy",
              80: "Eighty", 90: "Ninety", 100: "One Hundred", 200: "Two Hundred",
              300: "Three Hundred", 400: "Four Hundred", 500: "Five Hundred", 
              600: "Six Hundred", 700: "Seven Hundred", 800: "Eight Hundred", 
              900: "Nine Hundred", 1000: "One Thousand", 1000000: "One Million", 1000000000:                 "One Billion"}
        ans = ""
        tmp, cnt, numList = num, 0, []
        tmp = str(num)
        cnt = len(tmp) - 1
        numList = [int(i) for i in tmp]
        # for digit in numList:
        #     val = digit * int(pow(10, cnt))
        val = num
        if val in di.keys():
            return di[val]
        if val > 1000000000:
            tmp = int(val / 1000000000)
            ans += self.numberToWords(tmp)
            ans += " Billion "
            if (val % 1000000000 > 0):
                ans += self.numberToWords(val % 1000000000)
        elif val > 1000000:
            tmp = int(val / 1000000)
            ans += self.numberToWords(tmp)
            ans += " Million "
            if (val % 1000000) > 0:
                ans += self.numberToWords(val % 1000000)
        elif val > 1000:
            tmp = int(val / 1000)
            ans += self.numberToWords(tmp)
            ans += " Thousand "      
            if (val % 1000) > 0:
                ans += self.numberToWords(val % 1000)
        else:
            if val > 99:
                tmp = int(val / 100)
                ans += di[tmp]
                ans += " Hundred "
                if (val % 100) > 0:
                    ans += self.numberToWords(val%100)
            elif val > 10 and val < 20:
                ans += di[val]
            elif val > 9:
                tmp = val - (val % 10)
                ans += di[tmp] + " "
                if val % 10 > 0:
                    ans += di[val % 10]
            else:
                ans += di[val]
            # cnt -= 1
        if ans[-1]==" ": return ans[:-1]
        return ans
