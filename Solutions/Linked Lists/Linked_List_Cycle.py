class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head == None: return False
        
        seen = dict()
        i = 0
        curr = head
        
        while(curr.next != None):
            if curr not in seen:
                seen[curr] = True
                curr = curr.next
            else:
                return True
        return False
    
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None: return None
        
        seen = dict()
        curr = head
        
        seen[curr] = 0
        
        while (curr != None):
            if curr.next in seen:
                return curr.next
            else:
                curr = curr.next
                seen[curr] = True
        return None