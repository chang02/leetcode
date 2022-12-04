from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = self.getLength(head)
        if length == 0:
            return None
        k = k % length
        if k == 0:
            return head
        
        lastNode = head
        while lastNode.next != None:
            lastNode = lastNode.next
        
        lastNode.next = head
        
        cur = head
        for x in range(length-k-1):
            cur = cur.next
        
        newHead = cur.next
        cur.next = None
        return newHead
            
    
    def getLength(self, head:Optional [ListNode]) -> int:
        len = 0
        cur = head
        while cur is not None:
            len += 1
            cur = cur.next
        return len