class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            diff = head.next
            while diff and head.val == diff.val:
                diff = diff.next
            head.next = diff
            self.deleteDuplicates(head.next)
        return head
