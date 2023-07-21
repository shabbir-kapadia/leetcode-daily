class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ptr = head
        tmp_next = None
        runner = None
        
        while ptr:
            if ptr.child:
                tmp_next = ptr.next
                ptr.next = ptr.child
                ptr.next.prev = ptr
                ptr.child = None
                
                
                runner = ptr.next
                while runner.next:
                    runner = runner.next
                runner.next = tmp_next
                if runner.next:
                    runner.next.prev = runner
            ptr = ptr.next
            
        return head