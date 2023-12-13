# Definition for singly-linked list.
# class ListNode:
    # def __init__(self, val=0, next=None):
    #     self.val = val
    #     self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        result.head = None
        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            self.appendNode(result, sum % 10)

            carry = 0
            if sum >= 10:
                carry = 1

            l1 = l1.next
            l2 = l2.next

            if l1 == None and l2 != None:
                l1 = ListNode(0)
            if l2 == None and l1 != None:
                l2 = ListNode(0)
        
        if carry != 0:
            self.appendNode(result, carry)
        
        return result

    def appendNode(self, list, val):
        newNode = ListNode(val)
        if list.head is None:
            list.val = val
            list.next = None
            list.head = newNode
            return

        while list.next:
            list = list.next
        list.next = newNode
