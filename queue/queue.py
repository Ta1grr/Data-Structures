from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = DoublyLinkedList(self)

  def enqueue(self, item):
    pass
  
  def dequeue(self):
    pass

  def len(self):
    len(self.storage)
