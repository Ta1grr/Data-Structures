"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    """Our doubly-linked list class. It holds references to
    the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 0

    #Adding new nodes as head
    def add_to_head(self, value):
        # check if a head already exists
        if not self.head:
            # if not, create a new node and set it as both head and tail
            new_node = ListNode(value, None)
            self.head = new_node
            self.tail = new_node
        else:
            # wrap the input value in a node
            # set this node's next pointer to point to current head
            new_node = ListNode(value, self.head)
            # make sure the head pointer points to the new head
            self.head = new_node
            self.length += 1

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

    # a handy length getter so we can call the len() method on our linked list
    def __len__(self):
        return self.length

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

    def remove_from_tail(self):
        pass

    def move_to_front(self, node):
        pass

    def move_to_end(self, node):
        pass

    def delete(self, node):
        pass

    def get_max(self):
        pass
