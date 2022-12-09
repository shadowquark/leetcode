from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            head = tail = list1
            list1 = list1.next
        else:
            head = tail = list2
            list2 = list2.next
        while list1 or list2:
            if list1:
                temp1 = list1.val
            else:
                temp1 = 101
            if list2:
                temp2 = list2.val
            else:
                temp2 = 101
            if temp1 <= temp2:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        return head
        
fin = open("oo.xx", "r")
fout = open("xx.oo", "w")

in1 = [int(x) for x in fin.readline().split(',')] 
in2 = [int(x) for x in fin.readline().split(',')] 
list1, list2 = ListNode(), ListNode()
tail1, tail2 = list1, list2
for x in in1:
    tail1.next = ListNode(x) 
    tail1 = tail1.next
for x in in2:
    tail2.next = ListNode(x) 
    tail2 = tail2.next
list1, list2 = list1.next, list2.next
out = Solution().mergeTwoLists(list1, list2)
while out:
    print(out.val)
    fout.write(str(out.val))
    out = out.next

