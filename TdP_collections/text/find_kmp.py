# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def find_kmp(T, P):
  """Return the lowest index of T at which substring P begins (or else -1)."""
  n, m = len(T), len(P)            # introduce convenient notations
  if m == 0: return 0              # trivial search for empty string
  fail = compute_kmp_fail(P)       # rely on utility to precompute
  j = 0                            # index into text
  k = 0                            # index into pattern
  while j < n:
    if T[j] == P[k]:               # P[0:1+k] matched thus far
      if k == m - 1:               # match is complete
        return j - m + 1           
      j += 1                       # try to extend match
      k += 1
    elif k > 0:                    
      k = fail[k-1]                # reuse suffix of P[0:k]
    else:
      j += 1
      
  return -1                        # reached end without match

def compute_kmp_fail(P):
  """Utility that computes and returns KMP 'fail' list.
  
  Calcola l'array LPS (Longest Prefix Suffix) per il pattern P.
  """
  m = len(P)
  fail = [0] * m                   # by default, presume overlap of 0 everywhere
  j = 1
  k = 0
  while j < m:                     # compute f(j) during this pass, if nonzero
    if P[j] == P[k]:               # k + 1 characters match thus far
      fail[j] = k + 1
      j += 1
      k += 1
    elif k > 0:                    # k follows a matching prefix
      k = fail[k-1]
    else:                          # no match found starting at j
      j += 1
      
  return fail

'''Fatto da me'''
def find_kmp_all(T, P):
  """Restituisce tutti gli indici di T in cui ha inizio il pattern P (oppure -1 se non presente)."""
  n, m = len(T), len(P)            # introduce convenient notations
  if m == 0: return 0              # trivial search for empty string
  fail = compute_kmp_fail(P)       # rely on utility to precompute
  j = 0                            # index into text
  k = 0                            # index into pattern
  matches = []                     # lista di indici in cui iniziano le occorrenze del pattern nel testo 
  while j < n:
    if T[j] == P[k]:               # P[0:1+k] matched thus far
      if k == m - 1:               # match is complete
        matches.append(j - m + 1)  # memorizza l'indice in cui inizia l'occorrenza
        j += 1                     # passa al carattere del testo successivo
        k = fail[k]                # usa il suffisso che è anche prefisso di tutto il pattern
      else:               
        j += 1                     # try to extend match
        k += 1
    elif k > 0:                    
      k = fail[k-1]                # reuse suffix of P[0:k]
    else:
      j += 1
      
  return matches if matches else -1  # restituisci la lista indici (-1 se vuota)

'''Fatto da me'''
def find_kmp_last(T, P):
  """Restituisce l'ultimo indice di T in cui ha inizio il pattern P (oppure -1 se non presente)."""
  n, m = len(T), len(P)            # introduce convenient notations
  if m == 0: return 0              # trivial search for empty string
  fail = compute_kmp_fail(P)       # calcola la failure function sul pattern
  j = n - 1                        # indice del testo inizia dall'ultima posizione
  k = m - 1                        # index into pattern
  
  while j >= 0:                    # scorre il testo al rovescio
    if T[j] == P[k]:               # P[0:1+k] matched thus far
      if k == 0:                   # match is complete
        return j                   # indice dell'occorrenza
      j -= 1                       # try to extend match
      k -= 1
    elif k < m-1:                    
      k = fail[k]                  
    else:
      j -= 1
      
  return -1                   

