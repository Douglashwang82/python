class UnsortedPriorityQueue(PriorityQueueBase): # base class defines _item
    """A min-oriented priority queue implemented with an unsorted list."""
    
    def _find_min(self):    # nonpublic utility
        """Return Position of item with minimum key."""
        if self.is_empty(): #inherited from base class
            raise Empty('Priority queue is empty')
        small = self._data.first()
        after = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()   # a double Linked list

    
    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        self._data.add_last(self._item(key, value))
        
    def min(self):
        """Return but do not remove (k, v) tuple with minimum key."""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Return and remove min (k,v)"""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)
        
