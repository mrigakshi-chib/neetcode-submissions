# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        l1_true = 0
        exp  = 0
        while (l1):
            l1_true += l1.val * 10 ** exp
            exp += 1
            l1 = l1.next
        l2_true = 0
        exp  = 0
        while (l2):
            l2_true += l2.val * 10 ** exp
            exp += 1
            l2 = l2.next  
        total = str(l1_true + l2_true)
        for num in total[::-1]:
            cur.next = ListNode(int(num))
            cur = cur.next
        

        return dummy.next
        
  
        