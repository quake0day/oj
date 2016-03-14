

def copy(head):
    nodeDict = {}
    dummy = RandomListNode(0)
    pointer = head 
    newHead = dummy

    while pointer:
        newNode = RandomListNode(pointer.label)
        nodeDict[pointer] = newNode
        newHead.next = newNode 
        newHead = newHead.next 
        pointer = pointer.next 

    pointer, newHead = head, dummy.next 

    while pointer:
        if pointer.random:
            newHead.random = nodeDict[pointer.random]

        pointer, newHead = pointer.next, newHead.next 
    return dummy.next 