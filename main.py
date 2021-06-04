# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        currA = headA
        currB = headB
        listA = set()
        
        while currA is not None:
            listA.add(currA)
            currA = currA.next
            
        while currB is not None:
            if currB in listA:
                return currB
            currB = currB.next
        
        return None

# ===============

