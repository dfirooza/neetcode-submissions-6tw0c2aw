# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #given: the beginning of a linked list 
        #return: whether there is a cycle in the linked list 
        #solution: keep a seen set, iterate through the linked list with the next pointer, and if the next pointer 
        #points to a number in the seen list return True 
        #if it points to null return False 
        #the list is not unique must consider that 

        slow, fast = head, head 

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                return True
        return False
