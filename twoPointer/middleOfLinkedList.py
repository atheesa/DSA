import math
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
# Fast slow solution

def middle_of_linked_list(head: Node) -> int:
    slow,fast = head,head
    while(fast.next != None):
        slow = slow.next
        if(fast.next.next):
            fast = fast.next.next
        else:
            break
    return slow.val

# Inital Solution

# def middle_of_linked_list(head: Node) -> int:
    
#     lh,rh = head
#     count = 0
    
#     while(rh.next != None):
#         rh = rh.next
#         count += 1
#     math.ceil(count /2)
#     while(count > 0):
#         lh = lh.next
#         count -= 1
#     return lh.val

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None:
        return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)

if __name__ == "__main__":
    head = build_list(iter(input().split()), int)
    res = middle_of_linked_list(head)
    print(res)
