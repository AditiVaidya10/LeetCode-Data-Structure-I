class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == 99999:
                return True
            else:
                head.val = 99999
                head = head.next
        return False
