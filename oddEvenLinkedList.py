class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        odd=head
        even=head.next
        evenHead=even
        while odd.next and even.next:
            odd.next=odd.next.next
            odd=odd.next
            
            even.next=even.next.next
            even=even.next
        odd.next=evenHead
        return head