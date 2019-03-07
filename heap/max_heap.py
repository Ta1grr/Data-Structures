class Heap:
    def __init__(self):
        self.storage = []

        # -- Notes --
        # Max Heap: A[PARENT(i) ] ≥ A[i]
        # Min Heap: A[PARENT(i) ] ≤ A[i]

    # Inserting a new value to the end of the list and then sift through the list accordingly to max heap
    def insert(self, value):
        self.storage.append(value)
        return self._bubble_up(len(self.storage) - 1)

        # -- Notes --
        # A[A.length] = v
        # i = A.length-1
        # while (i > 1 && A[parent(i)] < A[i])
        # swap(A[i], A[parent(i)])

    """   * `delete` removes and returns the 'topmost' value from the heap; 
        this method needs to ensure that the heap property is maintained after 
        the top most element has been removed. """
    def delete(self):
        pass

        # -- Notes --
        #  Delete will swap the root node with the last node of the array, delete the last value and start sift stuff down 

    # Getting the largest number
    def get_max(self):
        max_value = self.storage[0]
        for i in range(len(self.storage)):
            if self.storage[i] > max_value:
                max_value = self.storage[i]
        return max_value

    # * `get_size` returns the number of elements stored in the heap.
    def get_size(self):
        print(len(self.storage))



    # Child Element bigger than the Parent (Insert)
    def _bubble_up(self, index):
        # left_child = (index * 2) + 1
        # right_child = (index * 2) + 2
        parent = (index - 1) // 2
        # Base case to break out of recursion 
        if index == 0 or self.storage[parent] > self.storage[index]:
            return
        # If index is greater than parent
        if self.storage[index] > self.storage[parent]:
            # swap index with parent
            self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
            return self._bubble_up(index)

        #if index == 0 or parent > child
        #   return (at the top)

        # -- Notes --
        # To be bubble up after getting max value

        # Compare element at index to its parent
        # 1. If it is greater
        #       Swap with parent
        #       Bubble_up(self, old_parent_index)



    """ # Parent Element is smaller than children (Delete)
        # * `_sift_down` grabs the indices of this element's children and determines which child has a larger value. 
       If the larger child's value is larger than the parent's value, the child element is swapped with the parent."""
    def _sift_down(self, index):
        # if LC greater than length of array or RC greater than length of array
        pass
            

        # -- Notes --
        # To be sift down after inserting number
        # Swap with the largest parent

        # 1. If element has no children, stop
        # 2. is element less than max child, swap


heap = Heap()

heap.insert(1)
heap.insert(2)
heap.insert(3)
heap.insert(4)
heap.insert(5)
heap.insert(6)
heap.insert(7)

print(heap.get_size)


# for (i = A.length/2; i >= 1; i--)
#   shiftDown(i)


# -- Formula --
    # LC: (index * 2) + 1
    # RC: (index * 2) + 2
    # P : (index - 1) // 2

# -- Readme.md --
# ### Heaps
#   * Should have the methods `insert`, `delete`, `get_max`, `_bubble_up`, and `_sift_down`.
#   * `insert` adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap
#   * `delete` removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed. 
#   * `get_max` returns the maximum value in the heap _in constant time_.
#   * `get_size` returns the number of elements stored in the heap.
#   * `_bubble_up` moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index.
#   * `_sift_down` grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent.