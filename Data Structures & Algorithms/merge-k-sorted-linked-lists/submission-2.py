# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None

        while len(lists) > 1:
            x = [] # maybe we keep on outside instead

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None


                x.append(self.merge(l1,l2))

            lists = x

        return lists[0]

    

    def merge(self, l1, l2):


        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1 # unsure if .next here
                l1 = l1.next

            else:
                tail.next = l2 # unsure if .next here
                l2 = l2.next
            
            tail=tail.next


        if l1:
            tail.next = l1 # unsure
        else:   
            tail.next = l2 # unsure

        return dummy.next
        