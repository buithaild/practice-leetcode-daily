from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None

        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp
        return node

#Tao 1 linked list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


if __name__ == "__main__":
    solution = Solution()

    # Tạo danh sách liên kết từ [1, 2, 3, 4, 5]
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Original List:")
    print(head)

    # Đảo ngược danh sách liên kết
    reversed_head = solution.reverseList(head)
    print("Reversed List:")
    print(reversed_head)