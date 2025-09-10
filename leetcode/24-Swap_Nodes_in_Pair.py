
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            
            first_node = prev.next
           
            second_node = prev.next.next

            
            first_node.next = second_node.next
            second_node.next = first_node
            prev.next = second_node

           
            prev = first_node
        
        return dummy.next
