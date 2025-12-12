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
from reverseLinkedList import ListNode

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotate_linked_list(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head
        # 1) tính length và tìm tail
        while tail.next:
            tail = tail.next
            length += 1

        # 2) rút gọn k
        k_mod = k % length
        if k_mod == 0:
            return head

        # 3) noi tail -> head tao vong
        tail.next = head
        # 4) tìm new_tail: đi (length - k_mod - 1) bước từ head
        step_to_new_tail = length - k_mod - 1
        new_tail = head
        for _ in range(step_to_new_tail):
            new_tail = new_tail.next

        # 5) xác định new_head và ngắt vòng
        new_head = new_tail.next
        new_tail.next = None

        return new_head

    def build_list(self, vals):
        if not vals: return None
        head = ListNode(vals[0])
        cur = head
        for v in vals[1:]:
            cur.next = ListNode(v)
            cur = cur.next
        return head

    def to_list(self, head):
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res


if __name__ == '__main__':
    s = Solution()
    head = s.build_list([1, 2, 3, 4, 5])
    res = s.rotate_linked_list(head, 2)
    print(s.to_list(res))  # [4,5,1,2,3]

    head = s.build_list([0, 1, 2])
    res = s.rotate_linked_list(head, 4)
    print(s.to_list(res))  # [2,0,1]

