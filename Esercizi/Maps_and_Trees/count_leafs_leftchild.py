from TdP_collections.map.binary_search_tree import TreeMap

def count_leafs_leftchild(T: TreeMap):
    if T.is_empty():
        raise ValueError("Albero vuoto")
    
    count = 0
    for p in T.positions():
        if T.is_leaf(p):
            parent = T.parent(p)
            if T.left(parent) == p:
                count += 1
                
    return count