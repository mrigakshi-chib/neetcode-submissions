# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #first part
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        second = slow.next
        slow.next = None

        #second part
        
        prev = None
        current = second
        while current:
            current_next = current.next
            current.next = prev
            prev = current
            current = current_next
        
        second = prev

        #third part
        first = head
        while second:
            

            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
            
