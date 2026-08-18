# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        newHead = ListNode()
        newHead.next = head

        # Computes size of linked list
        sz = 0
        node = head
        while (node):
            node = node.next
            sz += 1

        # Remove the 'mth' node from beginning oflist
        m = sz - n
        
        node = newHead

        for i in range(m):
            node = node.next
        
        node.next = node.next.next

        return newHead.next
