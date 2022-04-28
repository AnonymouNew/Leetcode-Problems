# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==1:
            return head
        curr = head
        n = 0
        while curr:
            curr = curr.next
            n += 1
        curr = head
        tmp = ListNode(-1)
        tmp.next = head
        tail = tmp
        while n-k>=0:
            for _ in range(k-1):
                nxt = curr.next
                curr.next = curr.next.next
                nxt.next = tail.next
                tail.next = nxt
            tail, curr = curr, curr.next
            n -= k
        return tmp.next
            
