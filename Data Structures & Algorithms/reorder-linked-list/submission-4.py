# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # use slow and fast pointers to get the middle use the fast=head.next trick for this

        slow = head

        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        '''
        head = [2,4,6,8], slow = 2->4, fast = 2->6->8
        '''

        second = slow.next # second = 6
        prev = None
        slow.next = prev # 2->4->None, now this is a sucessfuly split of the 2 halves

        while second: # reverse the second half being 6->8
            
            temp = second.next  # 8
            second.next = prev # 6-> None the pre-defined prev above
            prev = second # None->6
            second = temp # 6->8



        # 2->4           6<-8
        first = head # 2
        second = prev # second 8

        while second:
            tmp1 = first.next #4
            tmp2 = second.next # 6
            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2









