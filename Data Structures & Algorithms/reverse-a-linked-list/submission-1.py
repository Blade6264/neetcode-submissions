# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if the list is empty or the list has the size = 1 ->
        # don't have to reverse
        if head == None or head.next == None:
            return head
        
        prev = None
        curr = head
        nxt = head.next
        while curr: # this is a shorthand of curr != None
            curr.next = prev
            prev = curr
            curr = nxt
            if nxt: # this is a shorthand of nxt != None
                nxt = nxt.next
        head = prev
        return head