# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        out = l3 = ListNode(None)
        
        while l1 and l2:
            tot = carry + l1.val + l2.val
            carry = 1 if tot >= 10 else 0
            l3.next = ListNode(tot%10)
            l1, l2, l3 = l1.next, l2.next, l3.next
        
        while l1:
            tot = carry + l1.val
            carry = 1 if tot >= 10 else 0
            l3.next = ListNode(tot%10)
            l1, l3 = l1.next, l3.next
            
        while l2:
            tot = carry + l2.val
            carry = 1 if tot >= 10 else 0
            l3.next = ListNode(tot%10)
            l2, l3 = l2.next, l3.next
            
        l3.next = ListNode(carry) if carry else None    
            
        return out.next