"""
Given the head of a linked list, rotate the list to the right by k places.
Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""

from typing import Optional

from Tools.scripts.generate_opcode_h import header

from reverseLinkedList import ListNode


class Solution:
    def rotate_linked_list(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        dummy = head
        while dummy.next:
            dummy = dummy.next
            length += 1

        postion = k % length;
        if postion == 0:
            return head
        current = head

        for _ in range(length - postion - 1):
            current = current.next

        new_head = current.next
        current.next = None
        dummy.next = head

        return new_head

    def build_list(self, vals):
        if not vals: return None
        head = ListNode(vals[0])
        cur = head
        for v in vals[1:]:
            cur.next = ListNode(v)
            cur = cur.next
        return head
if __name__ == '__main__':
    s = Solution()
    head = s.build_list([1,2,3,4,5])
    k = 2
    res = s.rotate_linked_list(head, k)
    print(res)


