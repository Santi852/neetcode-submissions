# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new = []
        head1 = list1
        head2 = list2
        while head1:
            if head1.value >= head2.value:
                new.append(head1)
                head1.next
            else: 
                new.append(head2)
                head2.next

