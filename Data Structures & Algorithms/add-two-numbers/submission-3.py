# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carryover = False
        while l1 or l2:
            value = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carryover
            tail.next = ListNode(value % 10)
            if value / 10 >= 1:
                carryover = True
            else:
                carryover = False
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            tail = tail.next
        
        if carryover:
            tail.next = ListNode(1)

        return dummy.next

