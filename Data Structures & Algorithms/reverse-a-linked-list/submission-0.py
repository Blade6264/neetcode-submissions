# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 0 -> 1 -> 2 -> 3
# 3 => 2 => 1 => 0
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr != None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        head = prev
        return head