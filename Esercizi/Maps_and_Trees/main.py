from count_leafs_leftchild import *
from count_descendants import *


def main():
    T = TreeMap()
    
    T[10] = 'N' #         (10: N)           
    T[5]  = 'a' #      /         \         
    T[15] = 't' #   (5: a)       (15: t)   
    T[4]  = 'a' #   /    \         /    \  
    T[6]  = 'l' # (4: a)  (6: l)  (14: e)    
    T[14] = 'e'

    map_to_string = ""
    for p in T.breadthfirst():
        print(f"{p.key()}: {p.value()}")
        map_to_string += str(p.value()) 
    
    print(map_to_string + "\n")
    
    # start = T.find_position(6)
    # end = T.find_position(10)
    # print(f"\n# valori tra {start.key()} e {end.key()}: {count_range(T, start, end)}")
    
    # cmn_anc = common_ancestor(T, start, end)
    # print(f"\nAntenato comune più basso tra ({start.key()}: {start.value()}) e ({end.key()}: {end.value()}) è ({cmn_anc.key()}: {cmn_anc.value()})")

    descA = count_descendantsA(T)
    print("Tonio: " + repr(descA))

    print("Foglie figlie sinistre: " + repr(count_leafs_leftchild(T)))
    
    
if __name__ == "__main__":
    main()
