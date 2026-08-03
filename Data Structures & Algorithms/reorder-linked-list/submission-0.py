# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #given: the head of a singly linked-list
        #return: the same link list mutated to the general case
        #on each turn, make the current node's next pointer point to the last node in the list, and then from there
        #make that node point to the previous next, and continue this cycle
        #the difficulty is how to just have access to the last node of the list since you'd have to traverse first
        #you can only iterate through once and have to change pointers as you go along
        #each time first store the current node and the current node's value, then change the current node's next pointer to the previous node's stored next pointer 
        #you should use a stack to do this 

        if not head: 
            return

        stack = []

        beginning = head
        while head: 
            stack.append(head)
            head = head.next 

        n = len(stack)

        head = beginning
        count = 0 
        while count < n - 1: 
            if count % 2 != 0: 
                head.next = new_next
                head = head.next
                count += 1
            else: 
                new_next = head.next
                head.next = stack.pop()
                head = head.next
                count += 1

        head.next = None

        