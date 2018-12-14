class Vector(object):
  """Represent a vector in multidimensional space."""

  def __init__(self, d):
    """Create d-dimensional vector of zeros."""
    self._coords = [0] * d
    
  def __len__(self):
    """Return the dimension of the vector."""
    return len(self._coords)
