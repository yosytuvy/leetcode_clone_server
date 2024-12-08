class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head:ListNode, n) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        arr = [dummy]
        while head:
            arr.append(head)
            head = head.next
        for _ in range(n + 1):
            pre = arr.pop()
        pre.next = pre.next.next
        return dummy.next