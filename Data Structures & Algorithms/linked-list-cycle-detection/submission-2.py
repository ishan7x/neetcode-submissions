# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        if not head or not head.next:
            return False
        fast = head.next.next
        while fast and fast.next:
            print("Fast and slow", fast.val,slow.val)
            if fast == slow:
                break
            slow = slow.next
            fast = fast.next.next
        return slow==fast

        