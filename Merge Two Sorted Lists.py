class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None: return list2
        if list2 == None: return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
        return list1 if list1.val <= list2.val else list2
