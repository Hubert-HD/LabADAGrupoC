# find_needle implementado en python
# Complejidad: O(m + n)

def isSubstring_in_String(substring, string):
  i = 0
  j = 0
  while j < len(string):
    if substring[i] == string[j]:
      encontrado = True
      while i < len(substring):
        if substring[i] != string[j + i]:
          encontrado = False
          break
        i =  i + 1
      if encontrado:
        return True
      i = 0
    j = j + 1
  return False

print(isSubstring_in_String("rog","programacion"))