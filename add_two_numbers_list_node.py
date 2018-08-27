#https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l3 = ListNode(0)
        flag = 0
        iter1 = l1
        iter2 = l2
        iter3 = l3

        while(iter1!=None or iter2!=None or flag!=0):
            val1 = 0
            val2 = 0
            if(iter1 is None):
                iter1 = ListNode(0)
            val1 = iter1.val
            if(iter2 is None):
                iter2 = ListNode(0)
            val2 = iter2.val
            val3 = val1 + val2 + flag
            if(val3>9):
                flag = 1
                val3 %= 10
            else:
                flag = 0
            iter3.val = val3

            if(iter1.next is None and iter2.next is None):
                if(flag==1):
                    iter3.next = ListNode(1)
                return l3
            iter3.next = ListNode(0)
            iter3 = iter3.next
            iter1 = iter1.next
            iter2 = iter2.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
s = Solution()
l3 = s.addTwoNumbers(l1,l2)
iter = l3
while(iter!=None):
    print(iter.val)
    iter = iter.next

