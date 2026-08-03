# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #given: head of a linked list, an integer n 
        #return: its head after having removed the nth node from the end of the list
        #this is tricky since you don't know the length of a linked without traversing it 
        #the greedy way is to traverse once to get the length, calculate length - n,
        #then traverse again with a counter and once you reach that index node remove it

        length = 0 
        cur = head

        while cur: 
            cur = cur.next
            length += 1
        
        if length - n == 0: 
            return head.next

        prev = head
        for i in range(length - n-1): 
            prev = prev.next
        
        prev.next = prev.next.next

        return head



