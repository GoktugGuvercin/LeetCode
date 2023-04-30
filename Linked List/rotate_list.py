### Question 61: Rotate List
### Given the head of a linked list, rotate the list to the right by k places


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def length(self, ptr):
        if ptr.next is None:
            return 1
        else:
            return 1 + self.length(ptr.next)

    def go_until_end(self, ptr1: Optional[ListNode], ptr2: Optional[ListNode]) -> Optional[ListNode]:
        if ptr1.next is None:
            return ptr1, ptr2
        else:
            return self.go_until_end(ptr1.next, ptr1)

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None:
            return head
        
        list_length = self.length(head)
        k = k % list_length if k >= list_length else k
        
        for i in range(k):
            ptr1, ptr2 = head, head
            ptr1, ptr2 = self.go_until_end(ptr1, ptr2)
            ptr1.next = head
            ptr2.next = None
            head = ptr1

        return head
