# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        # Step 1: Find the middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Split the list
        secondHead = slow.next
        slow.next = None

        # Step 3: Reverse the second half
        prev = None
        cur = secondHead

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        secondHead = prev

        # Step 4: Merge two halves
        dummy = ListNode()
        node = dummy

        while head and secondHead:
            node.next = head
            head = head.next
            node = node.next

            node.next = secondHead
            secondHead = secondHead.next
            node = node.next

        node.next = head
