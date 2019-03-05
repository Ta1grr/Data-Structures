"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class Linked_lists:
    def _init_(self, node=None):
        self.head = node
        self.tail = node
        self.length = 0

    #Remove nodes from head
    def remove_from_head(self):
        # return None if there is no head (i.e. the list is empty)
        if not self.head:
            return None
        # if head has no next, then we have a single element in our list
        if not self.head.get_next():
            # get a reference to the head
            head = self.head
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None
            self.length -= 1
            # return the value
            return head.get_value()
        else:
            # otherwise we have more than one element in our list
            value = self.head.get_value()
            # set the head reference to the current head's next node in the list
            self.head = self.head.get_next()
            self.length -= 1
        return value

        #Adding new nodes as tail
    def add_to_tail(self, value):
        # 1. Allocates node
        # 2. Put in the data
        new_node = ListNode(value)

        # 3. This new node is going to be the last node,
        # so make next of it as None
        new_node.next = None

        # 4. If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            value.prev = None
            self.head = value
            return

        # 5. Else traverse till the last node
        last = self.head
        while(last.next is not None):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

        # 7. Make last node as previous of new node
        new_node.prev = last

        return


class Queue:
    def __init__(self):
        self.size = 0
    # what data structure should we
    # use to store queue elements?
        self.storage = Linked_lists()

    def enqueue(self, item):
        self.size += 1
        self.storage.add_to_tail(item)
    
    def dequeue(self):
        self.size -= 1
        self.storage.remove_from_head()

    def len(self):
        return (self.size)


test = Queue()

test.enqueue(5)
test.enqueue(6)

test.len