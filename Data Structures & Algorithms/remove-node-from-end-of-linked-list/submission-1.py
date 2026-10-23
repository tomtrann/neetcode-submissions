# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur: 
            count += 1
            cur = cur.next 
        
        if count == n:
            return head.next

        cur = head
        
        for i in range(count - n - 1):
            cur = cur.next
        
        temp = cur.next.next
        cur.next = temp
        return head