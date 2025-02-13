

def deleteRange(T, start, stop):
    if not T.is_empty():
        # Se la mappa non è vuota
        T.validate(start)  # Potresti avere posizioni di Tree e non di TreeMap
        T.validate(stop)

        # Se start è None, prendi la posizione più piccola
        if start is None:
            start = T.first()
        else:
            p = T.find_position(start.key())  # Trova la posizione di start
            if p.key() < start.key():
                # Se la posizione trovata è più piccola di start, prendi il successore
                p = T.after(p)

        # Ciclo per eliminare elementi nel range
        while p is not None and (p.key() < stop.key() or stop is None):
            old = p  # Salva la posizione corrente
            p = T.after(p)  # Aggiorna p al successore da esaminare
            T.delete(old)  # Cancella la posizione salvata
