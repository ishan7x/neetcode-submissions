# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummyHead = cur = ListNode()
        cur1 = l1
        cur2 = l2
        while(cur1 or cur2 or carry):
            res = carry
            if cur1:
                res+=cur1.val
                cur1 = cur1.next
            if cur2:
                res+=cur2.val
                cur2 = cur2.next
            cur.next = ListNode(res % 10)
            cur = cur.next
            carry = res//10
        return dummyHead.next
            
        