class SortedPriorityQueue(PriorityQueueBase): # base class defines _item
    """A min-oriented priority queue implemeneted with a sorted list."""
    
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()
        
    def __len__(self):
        """Return the nuber of items in the P."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        newest = self._item(key, value) # make new item instance
        walk = self._data.last()    # walk backward looking for smaller key
        while walk is not NOne and newest < walk.element():
            walk = self._data.before(walk)
        i
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        """Return but do not remove (k, v) tuple with minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Return and remove the min tuple."""
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
        