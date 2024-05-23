class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1:[ListNode], l2:[ListNode]) ->[ListNode]:
        ll = ListNode()
        head = ll 
        f = []
        s = []
        while l1 : 
            f.append(str(l1.val))
            l1 = l1.next
        while l2 : 
            s.append(str(l2.val))
            l2 = l2.next
        n1 = int("".join(f[::-1]))
        n2 = int("".join(s[::-1]))
        m = n1+n2
        k = list(str(m))[::-1]
        for i in k : 
            new_node = ListNode(int(i))
            head.next = new_node 
            head = head.next
        return ll.next 

        

        
        