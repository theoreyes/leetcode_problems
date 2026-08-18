# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Node to keep track of head
        dummy = ListNode()

        # Tail of output list
        tail = dummy

        # Iterators for both lists
        node1 = list1
        node2 = list2

        while (node1 and node2):
            if node1.val <= node2.val:
                tail.next = node1
                node1 = node1.next
            else:
                tail.next = node2
                node2 = node2.next
            tail = tail.next
        
        tail.next = node2 if node2 else node1

        return dummy.next
