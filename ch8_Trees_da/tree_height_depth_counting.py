# Tree computing height and depth
def depth(self, p):
    """Return the number of levels separating Position p from the root."""
    if self.is_root(p):
        return 0
    else:
        return 1 + self.depth(self.parent(p))


# bottom up approach. from leaf to root. if p is root return 0, if p is leaf return 1 + f(p.parent)

def _height1(self):
    """Return the height of the tree."""
    return max(self.depth(p)) for p in self.positions() if self.is_leaf(p))

# unefficient for finding a height.

# Optimal choice can be O(n) in worst case.

def _height2(self, p):
    """Return the height of the subtree rooted at Position p."""
    if self.is_leaf(p):
        return 0
    else:
        return 1 + max(self._height2(c) for c in self.children(p))

def height(self, p = None):
    """Return the height of the subtree rooted at Position p.

    If p is None, return the height of the entire tree.
    """
    if p is None:
        p = self.root()
    return self._height1(p)
    