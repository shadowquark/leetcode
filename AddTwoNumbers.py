from typing import Optional
import functools as ft
from functools import partial as par
def F(*z):
    z = [*z]
    return [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]
fyx = lambda f, *x: lambda *y: f(*y, *x)
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def toListNumber(x):
        out = []
        while (x):
            out.append(x.val)
            x = x.next
        return out
    def toListNode(x):
        out = ListNode()
        previous = tail = out
        for xx in x:
            tail.val = xx
            tail.next = ListNode() 
            previous = tail
            tail = tail.next
        previous.next = 0
        return out
    def output(x, fout):
        out = ''
        for xx in x:
            out += str(xx) + ','
        fout.write(out[:-1])
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]
                        ) -> Optional[ListNode]:
        base = 0
        head = tail = ListNode()
        while l1 or l2:
            num1 = num2 = 0
            if (l1):
                num1 = l1.val
            if (l2):
                num2 = l2.val
            if num1 + num2 + base < 10:
                tail.val = num1 + num2 + base
                base = 0
            else:
                tail.val = num1 + num2 + base - 10
                base = 1
            if (l1):
                l1 = l1.next
            if (l2):
                l2 = l2.next
            if l1 or l2:
                tail.next = ListNode()
                tail = tail.next
        if (base):
            tail.next = ListNode(1)
        return head

fin = open("oo.xx", "r");
fout = open("xx.oo", "w");

input1 = [int(x) - int('0') for x in fin.readline()[:-1].split(',')]
input2 = [int(x) - int('0') for x in fin.readline()[:-1].split(',')]
input1, input2 = FF([input1, input2], Solution.toListNode)

#F(Solution().addTwoNumbers(input1, input2), Solution.toListNumber, print)
F(Solution().addTwoNumbers(input1, input2),
    Solution.toListNumber, fyx(Solution.output, fout))

