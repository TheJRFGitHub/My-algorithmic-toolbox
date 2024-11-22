# First solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        linkedListToArray = []

        
        self.traverseLinkedList(head, linkedListToArray)

        
        return linkedListToArray == linkedListToArray[::-1]

    def traverseLinkedList(self, node: Optional[ListNode], linkedListToArray: list):
        if node is None:  
            return

       
        linkedListToArray.append(node.val)

        
        self.traverseLinkedList(node.next, linkedListToArray)
