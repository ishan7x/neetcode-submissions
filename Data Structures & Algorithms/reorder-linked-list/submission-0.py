# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        nodes = []
        while cur:
            nodes.append(cur)
            cur = cur.next
        l, r = 0, len(nodes) - 1
        while l < r:
            nodes[l].next = nodes[r]
            # print(l, r)
            l += 1
            if (l >= r):
                break
            nodes[r].next = nodes[l]
            r -= 1
        nodes[l].next = None
        
        return