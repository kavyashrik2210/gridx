# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. Check if there are at least k nodes left
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
        
        # 2. Reverse the first k nodes
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # 3. head is now the tail of the reversed group
        # Connect it to the result of the next group
        head.next = self.reverseKGroup(curr, k)
        
        # prev is the new head of this reversed segment
        return prev
