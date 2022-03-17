# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.val = 0
        self.head = None
    def createList(self, val):
        self.head = ListNode(val[0], None)
        for i in val[1:]:
            self.head = ListNode(i, self.head)
        return self.head
class Solution:
    def addTwoNumbers(self, l1, l2):
        ans = []
        val, rem = 0, 0
        while l1!=None or l2!=None:
            if l1!=None and l2!=None:
                val = l1.val + l2.val + rem
                if val > 9:
                    rem = int(val/10)
                    val = val % 10
                else: rem = 0
                ans.append(val)
                l1 = l1.next
                l2 = l2.next
            elif l1!=None:
                val = l1.val + rem
                if val > 9:
                    rem = int(val/10)
                    val = val % 10
                else: rem = 0                    
                ans.append(val)
                l1 = l1.next                
            else:
                val = l2.val + rem
                if val > 9:
                    rem = int(val/10)
                    val = val % 10
                else: rem = 0
                ans.append(val)
                l2 = l2.next         
        if rem > 0: ans.append(rem)
        ans1 = LinkedList()
        result = ans1.createList(ans[::-1])
        return result
