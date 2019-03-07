class Heap:
    def __init__(self):
        self.storage = []

        # -- Notes --
        # Max Heap: A[PARENT(i) ] ≥ A[i]
        # Min Heap: A[PARENT(i) ] ≤ A[i]

    # Inserting a new value to the end of the list and then bubble upward through the list accordingly to max heap
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
        self._bubble_up(len(self.storage) - 1)
        self.storage[0], self.storage[len(self.storage) - 1] = self.storage[len(self.storage) - 1], self.storage[0]
        Max = self.storage.pop()
        self._sift_down(0)
        return Max

        # -- Notes --
        #  Delete will swap the root node with the last node of the array, delete the last value and start sift stuff down 

    # Getting the largest number
    def get_max(self):
        # self._bubble_up(len(self.storage) - 1)
        return self.storage[0]

        # Alternative way to get max value
        # max_value = self.storage[0]
        # for i in range(len(self.storage)):
        #     if self.storage[i] > max_value:
        #         max_value = self.storage[i]
        # return max_value

    # * `get_size` returns the number of elements stored in the heap.
    def get_size(self):
        if not self.storage:
            return 0
        else:
            return len(self.storage)



    # Child Element bigger than the Parent (Insert)
    def _bubble_up(self, index):
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
        # Formula to access certain index
        left_child = (index * 2) + 1
        right_child = (index * 2) + 2
        # Base case to break out of the loop.
        if left_child >= len(self.storage) or left_child is None:
            return
        elif right_child >= len(self.storage) or right_child is None:
            return

        # if the left child is larger or equal than to the right child
        if self.storage[left_child] >= self.storage[right_child]:
            # If the left child is greater than the index, swap.
            if self.storage[left_child] > self.storage[index]:
                self.storage[left_child], self.storage[index] = self.storage[index], self.storage[left_child]
                return self._sift_down(left_child)
                
        # if the right child is greater than or equal to the left child 
        if self.storage[right_child] >= self.storage[left_child]:
            # If the right child is greater than index, swap
            if self.storage[right_child] >= self.storage[index]:
                self.storage[right_child], self.storage[index] = self.storage[index], self.storage[right_child]
                return self._sift_down(right_child)
        

        # Parent will compare with Child and swap if Parent is smaller
        
        # -- Notes --
        # To be sift down after inserting number
        # Swap parent with the largest child

        # 1. If element has no children, stop
        # 2. is element less than max child, swap



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