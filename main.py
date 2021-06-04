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

from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class HashSet:
    
    def __init__(self):
        self.arr = [None] *1000000
        
    def hashIndex(self, key):
        return hash(key) % len(self.arr)
    
    def add(self, key):
        hashIndex = self.hashIndex(key)
        if self.arr[hashIndex] == None:
            newList = deque()
            newList.append(key)
            self.arr[hashIndex] = newList
        elif key not in self.arr[hashIndex]:
            self.arr[hashIndex].append(key)
            
    def contains(self, key):
        hashIndex = self.hashIndex(key)
        if self.arr[hashIndex] != None:
            return True
        else:
            return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        newHashSet = HashSet()
        
        curr = head
        
        while curr is not None:
            if newHashSet.contains(curr):
                return True
            else:
                newHashSet.add(curr)
                curr = curr.next
            
        return False

# ===============

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        curr = head
        
        if curr is None:
            return curr
        elif curr.val != val:
            curr.next = self.removeElements(curr.next, val)
            return curr
        else:
            curr.next = self.removeElements(curr.next, val)
            return curr.next

# ===============

