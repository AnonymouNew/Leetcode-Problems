import heapq as hq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        n = len(lists)
        if n == 0:
            return None
        hres = []
        hq.heapify(hres)
        for i in range(n):
            head = lists[i]
            while head:
                hq.heappush(hres, head.val)
                head = head.next
        if len(hres) == 0:
            return None
        head = ListNode()
        temp = head
        while hres:
            temp.val = hq.heappop(hres)
            temp.next = ListNode() if len(hres) > 0 else None
            temp = temp.next
        return head
        
if __name__ == "__main__":
    temp = input()
    inp = []
    ob = Solution()
    val1 = 0
    for i in range(len(temp)-1):
        if temp[i]=="[":
            head = ListNode()
            head1 = ListNode()
            head1 = head
        elif temp[i]==",":
            if temp[i-1]!="]":
                head.next = ListNode(val1)
                head = head.next
            val1 = 0
        elif temp[i]=="]":
            head.next = ListNode(val1)
            inp.append(head1.next)
            val1 = 0
        else:
            val1 = val1*10 + int(temp[i])
    ans = ob.mergeKLists(inp)
    print("[",end="")
    while(ans):
        print(ans.val,end="")
        ans = ans.next
        if(ans):
            print(",",end="")
    print("]",end="")
       
