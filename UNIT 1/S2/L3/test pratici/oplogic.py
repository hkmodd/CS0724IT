# Funzione di conversione da True/False a "vero"/"falso"
def bool_a_string(valore):
    return "vero" if valore else "falso"

# Operatori di confronto
a = 10
b = 20

print("a è minore di b:", bool_a_string(a < b))           # Minore di
print("a è minore o uguale a b:", bool_a_string(a <= b))  # Minore o uguale
print("a è uguale a b:", bool_a_string(a == b))           # Uguale
print("a è maggiore di b:", bool_a_string(a > b))         # Maggiore di
print("a è maggiore o uguale a b:", bool_a_string(a >= b))# Maggiore o uguale
print("a è diverso da b:", bool_a_string(a != b))         # Diverso

# Operatori di identità
lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]

print("lista1 è lista2:", bool_a_string(lista1 is lista2))         # is - Identità dell'oggetto
print("lista1 è lista3:", bool_a_string(lista1 is lista3))         # is - Identità dell'oggetto (False perché sono liste diverse)
print("lista1 non è lista3:", bool_a_string(lista1 is not lista3)) # is not - Negazione identità

# Operatori di appartenenza
testo = "Ciao, mondo"
print("'C' è nel testo:", bool_a_string('C' in testo))             # in - Contenuto
print("'z' non è nel testo:", bool_a_string('z' not in testo))     # not in - Non contenuto

# Operatori logici
condizione1 = True
condizione2 = False

print("condizione1 e condizione2:", bool_a_string(condizione1 and condizione2))  # AND logico
print("condizione1 o condizione2:", bool_a_string(condizione1 or condizione2))    # OR logico
print("non condizione1:", bool_a_string(not condizione1))                         # NOT logico
