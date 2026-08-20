# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, second = head, head
        for i in range(n):
            second = second.next
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while second:
            prev = first
            first = first.next
            second = second.next
        if prev is not None:
            prev.next = prev.next.next
        else:
            return None
        return dummy.next