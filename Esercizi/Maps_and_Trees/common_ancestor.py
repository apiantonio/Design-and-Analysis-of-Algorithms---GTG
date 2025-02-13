from TdP_collections.map.binary_search_tree import TreeMap

def common_ancestor(T: TreeMap, p1: TreeMap.Position, p2: TreeMap.Position):
    """
    Returns the lowest common ancestor of the two nodes

    Args:
        T (TreeMap): 
        p1 (TreeMap.Position): 
        p2 (TreeMap.Position): 
        
    Raises:
        ValueError: if the positions p1 or p2 are not a Position of TreeMap  

    Returns:
        TreeMap.Position: the lowest common ancestor of p1 and p2 
    """
    
    T._validate(p1)
    T._validate(p2)
    
    if not T.is_empty():   # SE il BST è non vuoto
        
        p = T.find_position(p1.key())  # verifico che p1 sia nel BST O(h)
        if p.key() != p1.key():
            raise ValueError('P1 is not a Position of BST')
        
        p = T.find_position(p2.key())  # verifico che p2 sia nel BST
        if p.key() != p2.key():
            raise ValueError('P2 is not a Position of BST')

        d1 = T.depth(p1)  # salvo in una variabile la profondità p1 O(h)
        d2 = T.depth(p2)  # faccio lo stesso con p2   O(h)
        
        diff = abs(d1 - d2)  # calcolo la differenza tra le profondità di p1 e p2
        
        lowp, upperp = (p1, p2) if d1 >= d2 else (p2, p1)   # Distingue la position più in basso e quella più in alto
        
        # porto le position allo stesso livello
        for _ in range(diff):   # caso peggiore h*O(1)
            lowp = T.parent(lowp)    # fuori dal for le due position avranno la stessa profondità
        
        while lowp != upperp:   # il while finchè non risultano uguali  O(h) # HO DOVUTO SOTITUIRE is not con != perché parent() crea nuove istanze di Position, ciò causa che il confronto con 'is' è sempre negativo
            lowp = T.parent(lowp)      
            upperp = T.parent(upperp)
        
        # Complessivamente O(h)    
        return lowp

