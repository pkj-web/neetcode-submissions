# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next


        # seperate ll into two havles
        second = slow.next

        prev =None


        slow.next = prev

        # reverse 2nd half

        while second:
            temp = second.next
            second.next = prev

            prev=second
            second = temp

        # i guess we reorder here now
        front = head
        back = prev
        while front and back: 

            tmp1 = front.next
            tmp2 = back.next

            front.next = back
            back.next = tmp1

            front = tmp1
            back = tmp2


        
