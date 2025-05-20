# Theodore Reyes
#
# Explanation: The output linked list is built by iterating through the two
# parameter linked lists and adding their node values together, then creating
# a new node with this value and appending it to the output linked list.
#
# Pretty straight-forward linked list problem!

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nodeOne = l1
        nodeTwo = l2
        headNode = ListNode(0, None)  # dummy node
        curNode = headNode
        carry = 0
        sum = 0
        nodeOneVal = 0
        nodeTwoVal = 0
        while (((nodeOne != None) or (nodeTwo != None)) or carry > 0):
            # Gets value from nodes, handles case that node == None
            nodeOneVal = 0 if nodeOne == None else nodeOne.val
            nodeTwoVal = 0 if nodeTwo == None else nodeTwo.val

            # Calculates sum, updates carry
            sum = nodeOneVal + nodeTwoVal + carry
            if (sum > 9):
                carry = 1
                sum = sum - 10
            else:
                carry = 0
            
            # Appends new node to output list
            tmpNode = ListNode(sum, None)
            curNode.next = tmpNode
            curNode = tmpNode

            # Moves node iterators forward (if safe)
            if (nodeOne != None):
                nodeOne = nodeOne.next
            if (nodeTwo != None):
                nodeTwo = nodeTwo.next
        
        return headNode.next
