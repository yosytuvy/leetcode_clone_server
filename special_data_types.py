class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
def build_linked_list(values):
    """Convert a list to a ListNode."""
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    """Convert a ListNode to a list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result