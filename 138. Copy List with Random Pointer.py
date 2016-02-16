# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    # def copyRandomList(self, head):
    #     """
    #     :type head: RandomListNode
    #     :rtype: RandomListNode
    #     """
    #     if head == None:
    #         return head
    #     hashmap = {}
    #     newHead = RandomListNode(head.label)
    #     hashmap[head] = newHead 
    #     pre = newHead
    #     nextNode = head.next
    #     while nextNode:
    #         newNode = RandomListNode(nextNode.label)
    #         hashmap[nextNode] = newNode
    #         pre.next = newNode
    #         pre = newNode
    #         nextNode = nextNode.next
    #     node = head 
    #     copyNode = newHead
    #     while node:
    #         copyNode.random = hashmap[node.random]
    #         node = node.next 
    #         copyNode = copyNode.next
    #     return newHead
		def copyRandomList(self, head):
			nodeDict = dict()
			dummy = RandomListNode(0)
			pointer, newHead = head, dummy
			while pointer:
				newNode = RandomListNode(pointer.label)
				nodeDict[pointer] = newHead.next = newNode
				newHead, pointer = newHead.next, pointer.next 
			pointer, newHead = head, dummy.next 
			while pointer:
				if pointer.random:
					newHead.random = nodeDict[pointer.random]
				pointer, newHead = pointer.next, newHead.next 
			return dummy.next

		def copyRandomList(self, head):
			current = head 
			# add a new duplicate node after each original node
			while current:
				copied = RandomListNode(current.label)
				copied.next = current.next 
				current.next = copied
				current = copied.next 

			# update random node in copied list
			current = head 
			while current:
				if current.random:
					current.next.random = current.random.next 
				current = current.next.next 

			# Split copied list from combined one 
			dummy = RandomListNode(0)
			copied_current, current = dummy, head 
			while current:
				copied_current.next = current.next 
				current.next = current.next.next 
				copied_current, current = copied_current.next, current.next 
			return dummy.next 

