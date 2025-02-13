from TdP_collections.map.binary_search_tree import TreeMap

def count_range(T: TreeMap, start: TreeMap.Position, stop: TreeMap.Position):
    """given two positions in the MapTree, return the number 
    of Position p such that start.key() < p.key() < stop.key().
    """
    if T.is_empty():
        return None
    
    T._validate(start)
    T._validate(stop)
    
    if start is None:
        start = T.first()
    
    p = T.find_position(start.key())
    if p.key() <= start.key():
        p = T.after(p)
    
    count = 0
    while p is not None and (stop is None or p.key() < stop.key()):
        count += 1
        p = T.after(p)
    
    return count