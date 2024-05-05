"""
Dos palabras son anagramas cuando uno de ellos alterando sus letras se obtiene la otra
palabra, esto sin importar si existen
EJEMPLO: ROMA - AMOR - MAOR
"""

def sonAnagramas(cad1, cad2):
    list1 = list(cad1)
    list2 = list(cad2)

    list1.sort()
    list2.sort()
    return list1 == list2

Anagramas = sonAnagramas("aladds", "dsdala")

print(Anagramas)