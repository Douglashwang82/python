class PriorityQueueBase:
    """Abstract base class for a priority queue."""
    
    class _item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            """Compare items base on their keys"""
            return self._key < other._key
    
    def is_empty(self):
        """Return True if queue is empty."""
        return len(self) == 0
        
