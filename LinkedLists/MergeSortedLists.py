#problem Link : https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        tail = ans
        c1 = list1
        c2 = list2
        while c1 and c2:
            if(c1.val < c2.val):
                tail.next = ListNode(c1.val)
                c1 = c1.next
            else:
                tail.next = ListNode(c2.val)
                c2 = c2.next
            tail = tail.next
        if c1:
            tail.next = c1
        if c2:
            tail.next = c2
        return ans.next

        