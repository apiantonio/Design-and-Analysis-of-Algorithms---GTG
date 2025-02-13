from TdP_collections.map.binary_search_tree import TreeMap

def _num_descendants_p(T: TreeMap, p): 
    if p is None:
        p = T.root()

    count = 0
    for c in T.children(p):
        count += 1 + _num_descendants_p(T, c) 

    return count

def count_descendantsA(T: TreeMap, p: TreeMap.Position = None):
    descendants = {} # Inizializzazione della struttura dati

    if p is None:
        p = T.root()

    for p in T.positions():
        descendants[p.key()] = _num_descendants_p(T, p)  # Salvataggio del numero di discendenti

    return descendants

def count_descendantsB(T, p=None, h=0):
    if(p is None):
        p = T.root()
    if (T.is_empty()) or (T.is_leaf(p) and h==0):  # significa che gli hai passato già una foglia, il numero di discendenti quindi è 0
        return 0
    elif T.is_leaf(p) and h!=0:
        return 1  # Conta anche la foglia stessa
    elif h == 0:
        return sum(count_descendantsB(T, c, 1) for c in T.children(p))

    return 1 + sum(count_descendantsB(T, c, 1) for c in T.children(p))