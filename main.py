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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        curr = head
        newList_1 = []
        newList_2 = []
        
        while curr is not None:
            newList_1.append(curr.val)
            curr = curr.next
            
        newList_2 = newList_1[::-1]
        
        if newList_2 == newList_1:
            return True
        else:
            return False

# ===============

