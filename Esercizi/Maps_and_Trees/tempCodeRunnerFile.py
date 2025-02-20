  avl = AVLTreeMapBF()

  # Inseriamo dei nodi
  elements = [30, 20, 40, 10, 25, 35, 50, 5, 15, 45, 60]
  print("Inserimento elementi:", elements)
  
  for elem in elements:
    avl[elem] = str(elem)  # Inseriamo una coppia (chiave, valore)