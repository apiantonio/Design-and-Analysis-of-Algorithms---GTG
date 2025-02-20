from TdP_collections.map.binary_search_tree import TreeMap

class AVLTreeMapBF(TreeMap):
  """Implementazione di un AVL Tree che mantiene il balance factor (bf) invece dell'altezza."""

  class _Node(TreeMap._Node):
    __slots__ = '_bf'
    
    def __init__(self, element, parent=None, left=None, right=None):
      super().__init__(element, parent, left, right)
      self._bf = 0  # inizialmente il bf è 0

  def new_bf(z, y, x):
    """Calcola i nuovi bf dei nodi dopo una restructure se z è squilibrato
   
    restituisce (z_new_bf, y_new_bf, x_new_bf, nh) dove:
    - z_new_bf è il nuovo balance factor di z
    - y_new_bf è il nuovo balance factor di y 
    - x_new_bf è il nuovo balance factor di x
    - nh indica se l'altezza del sottoalbero è aumentata (nh=+1), diminuita (nh=-1) o rimasta invariata (nh=0)
    """
    if -2 < z.bf < 2: # z è bilanciato
      return z.bf, y.bf, x.bf, 0

    if z.bf == -2:
      if y.bf == -1:
        # rotazione singola a destra
        return 0, 0, x.bf, -1
      else: # doppia rotazione sinistra-destra
        if x.bf == -1:
            return 1, 0, 0, -1
        elif x.bf == 0:
            return 0, 0, 0, -1
        elif x.bf == 1:
            return 0, -1, 0, -1
          
    if z.bf == 2:
      # rotazione singola a sinistra
      if y.bf == 1:
          return 0, 0, x.bf, -1
      else: # doppia rotazione destra-sinistra
        if x.bf == -1:
            return 0, 1, 0, -1
        elif x.bf == 0:
            return 0, 0, 0, -1
        elif x.bf == 1:
            return -1, 0, 0, -1

    return z.bf, y.bf, x.bf, 0

  def _is_balanced(self, p):
    """Restituisce True se il nodo p è bilanciato, False altrimenti."""
    return  abs(p._node.bf) < 2 # se il bf è -1, 0 o 1 il nodo è bilanciato

  def _update_bf_insert(self, p, child):
    """Aggiorna il balance factor di p dopo l'inserimento di un nodo figlio.
    
    Se il nuovo figlio è a sinistra incrementa il bf, se a destra lo decrementa
    """
    if self.left(p) is child:
        p._node.bf += 1
    else:
        p._node.bf -= 1

  def _compute_height(self, p):
    """Calcola ricorsivamente l'altezza del sottoalbero radicato in p.
    Serve per il calcolo del balance factor dopo una delete
    """
    if p is None:
      return 0
    return 1 + max(self._compute_height(self.left(p)), self._compute_height(self.right(p)))

  def _update_bf_delete(self, p):
    """Aggiorna il balance factor di p dopo la cancellazione del figlio.
    calcola le nuove altezze dei sottoalberi e calcola il nuovo balance factor
    """
    # Calcola l'altezza dei sottoalberi per calcolare il nuovo balance factor
    left_height = self._compute_height(self.left(p))
    right_height = self._compute_height(self.right(p))
    new_bf = left_height - right_height
    
    p._node.bf = new_bf

  def _tall_child(self, p, favorleft=False):
    """Restituisce il figlio 'più alto' di p in base al bf:
    se bf > 0 il figlio sinistro è più alto
    se bf < 0 il figlio destro più alto
    se bf = 0 p è bilanciato e si segue favorleft
    """
    if p._node.bf > 0:
      return self.left(p)
    elif p._node.bf < 0:
      return self.right(p)
    else: # se pari segui favorleft
      return self.left(p) if favorleft else self.right(p)

  def _rebalance(self, p):
    """Ribalancia l'albero a partire dal nodo p fino alla radice.
    
    utilizza la trinode restructuring _restructure(p) per bilanciare i nodi sbilanciati
    e usa new_bf() per calcolare i nuovi balance factor.
    """
    while p is not None:
      if not self._is_balanced(p): # il nodo non è bilanciato
        z = p # nonno 
        y = self._tall_child(z) # padre
        x = self._tall_child(y) # figlio
        
        z_bf_new, y_bf_new, x_bf_new, nh = self.new_bf(z._node, y._node, x._node)
        z._node.bf = z_bf_new
        y._node.bf = y_bf_new
        x._node.bf = x_bf_new

        if nh != 0:
          p = self._restructure(x) # trinode restructuring
          p = self.parent(p)  
        else: # l'altezza del sottoalbero è rimasta invariata
          p = None # non risaliamo più
      else:
        # Se il nodo è già bilanciato, passiamo semplicemente al suo genitore
        p = self.parent(p)
          
  def _rebalance_insert(self, p):
    """Dopo l'inserimento di p aggiorna i bf e controllo se ci sono nodi che si sono sbilanciati e se servo ribilancio""" 
    parent = self.parent(p)
    self._update_bf_insert(parent, p) #calcola i nuovi bf
    self._rebalance(parent) # ribilancia se serve
   
  def _rebalance_delete(self, p):
    """Dopo la cancellazione di p aggiorna i bf e controllo se ci sono nodi che si sono sbilanciati e se servo ribilancio""" 
    self._update_bf_delete(p) # calcola i nuovi bf
    self._rebalance(p) # ribilancia se serve
