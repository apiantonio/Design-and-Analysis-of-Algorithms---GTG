# Implementazione di una Hash Map con double hashing
# implementata per esercizio

from .hash_map_base import HashMapBase

class DoubleHashMap(HashMapBase):
  """Hash map implementata con double hashing per risolvere le collisioni"""
  _AVAIL = object()       # sentinal marks locations of previous deletions

  def __init__(self, cap=11, p=109345121, q=7):
    if q <= cap:
      raise ValueError("q deve essere minore della dimensione della mappa!") 
    super().__init__(cap, p)
    
  def _secondary_hash_function(self, k):
      return self.q - (k % self.q)
              
  def _is_available(self, j):
    """Return True if index j is available in table."""
    return self._table[j] is None or self._table[j] is DoubleHashMap._AVAIL
      
  def _find_slot(self, j, k):
    """Cerca la chiave k a partire dal bucket di indice j.

    Returns:
      (success, index) tupla, descritta come segue: 
      Se è stata trovata una corrispondenza, success è True e index indica la sua posizione. 
      Se non è stata trovata alcuna corrispondenza, success è False e index indica il primo slot disponibile.
    """
    firstAvail = None
    s = self._secondary_hash_function(k)
    c = 0 # numero di bucket controllati

    while True:
      if self._table[j] is None or self._table[j] is DoubleHashMap._AVAIL:
        if firstAvail is None:
          firstAvail = j  # mark this as first avail
        if self._table[j] is None:
          return (False, firstAvail) # search has failed
      elif k == self._table[j]._key:
        return (True, j)  # found a match
      c += 1
      j = (j + c * s) % len(self._table) # keep looking (cyclically) con double hashing

  def _bucket_getitem(self, j, k):
    found, s = self._find_slot(j, k)
    if not found:
      raise KeyError('Key Error: ' + repr(k))        # no match found
    return self._table[s]._value

  def _bucket_setitem(self, j, k, v):
    found, s = self._find_slot(j, k)
    if not found:
      self._table[s] = self._Item(k,v)               # insert new item
      self._n += 1                                   # size has increased
    else:
      self._table[s]._value = v                      # overwrite existing

  def _bucket_delitem(self, j, k):
    found, s = self._find_slot(j, k)
    if not found:
      raise KeyError('Key Error: ' + repr(k))        # no match found
    self._table[s] = DoubleHashMap()._AVAIL             # mark as vacated

  def __iter__(self):
    for j in range(len(self._table)):                # scan entire table
      if not self._is_available(j):
        yield self._table[j]._key
