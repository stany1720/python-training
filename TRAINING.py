# x = 10
# y = input("y: ")
# z = input("z: ")

# x += int(y)

# print(x)

# a = 5
# b = 7
# c = 9

# print(a < b and a < c)
# print(a < b and a < c)

# print("a" in "ana")
# print(6 not in [1, 2, 3])

# a is b
# a is not b


# var_1 = input("Numar 1: ")
# var_2 = input("Numar 2: ")\

# suma = int(var_1) + int(var_2)

# print(suma)
# ################################################################

# text1 = "something is happening"
# lista = ["mama", "tata", "frate", "sora"]

# my_list = text1.split()

# print(text1.split())
# print(text1.split("t"))

# new_sting = " ".join(my_list)

# print(new_sting)

# print(text1.startswith("somet"))
# print(text1.endswith("ing"))

# var = "test 1"

# La functii sau metode, ai nevoie de "()"

# print(var.isalnum())
# print("test".isalpha())
# print("123".isdigit())

# \n - new line
# \t - tab
# \\ - backslash
# \' - '
# \" - "

# a = 10
# b = 12

# if a < b:
#     print("a este mai mic decat b")
# elif b < a:
#     print("a este mai mare decat b")
# else:
#     print("a si b sunt egale")

# my_str = "mama are 10 pere"

# for char in my_str:
#     print(char)
# ==
# for cuvant in my_str.split():
#     lungime = len(cuvant)
#     print(cuvant)
#     print(lungime)

# for char in my_str:
#     if char.isdigit():
#         print(char)

# text = " "
# for char in my_str:
#     if char.isdigit():
#         text += char

# print(f"Cifrele din string sunt: {text}")
# print(f"Cifrele din string sunt: " + text)

# for numar in range(2, 4, 2):
#     print(numar)

# numar = 1
# limita = 5

# while numar <= limita:
#     print(numar)
#     numar += 1

# opresti Bucle:
# break
# continue
# pass

# x = -4
# if x > 0:
#     print("mai mare ca 0")
# else:
#     pass # Nu faci nimic, si mergi mai departe (la compilare verifici daca s-a vazut ramura de program)
# print("ceva....")

# for x in range(1, 10):
#     if x % 2 == 0:
#         print(x)
#     else:
#         continue # flag de debugging / optimizare / daca ceva nu e conform parametrii, treci mai departe


# Să nu se printeze numărul 3
# for i in range(5):
#     if i == 3:
#         continue  # Sări peste iterația curentă și treci la următoarea
#     print(i)

# Rezultat: 0, 1, 2, 4 (numărul 3 lipsește)

# linie 1
# linie 2
# linie 3
# date 1
# date 2
# date 3


# for linie in fisier:
#     if "date 3" in linie:
#         # prelucreaza info
#         break

# while inputul != 0:
#     if inputul == 0:
#         break

# Structuri de date:
# Liste
# list = []
# list()
# fructe = ["banane", "mere", "pere"]
# print(fructe)
# print(fructe[1])
# fructe[0] = "capsuni"
# print(fructe)
# print(fructe[0][0: 4])
# print(fructe[2].upper())

# lista_smechera = [1, 2, 3, "kiwi", "bere",
# ['Mariana', ['Ionela'], ['Marius']]]
# ela
# print(lista_smechera[-1][-2][-3:]) # cate liste in liste ai, atatea paranteze drepte ai, apoi slicing
# print(len(lista_smechera))
# lista_smechera.append(4.6)
# print(lista_smechera)
# lista_smechera.insert(3, 3.5)
# print(lista_smechera)
# lista_smechera.append(3.5)
# print(lista_smechera)
# lista_smechera.remove(3.5)#
# print(lista_smechera)

# while 3.5 in lista_smechera:
#     lista_smechera.remove(3.5)

# print(lista_smechera)
# print(lista_smechera.pop())

# lista1 = [1, 2, 3]
# lista2 = [3, 4, 5]

# lista1.append(lista2)
# print(lista1)
# lista1.extend(lista2)
# print(lista1)

# import random
# exemplu = [5, 7, 3, 1, 9, 4]
# random.shuffle(exemplu)
# exemplu.sort()
# print(exemplu)

# ex_sorted = sorted(exemplu, reverse=True)
# print(exemplu)
# print(ex_sorted)

# for index, valoare in enumerate(lista_smechera):
#     print(f"{index} -> {valoare}")

# print(lista_smechera[-3:])

# all verifica daca toat is True, any verifica daca cel putin unul este True.

# lista1 = [1, 2, 3, 4, 5]
# lista2 = [0, 1, 2, 3, 4]

# print(any(lista1))
# print(any(lista2))
# print(all(lista1))
# print(all(lista2))

# lista = range(1, 11)
# lista_pare = []

# for i in lista:
#     if i % 2 == 0:
#         lista_pare.append(i)
#     else:
#         continue

# print(lista_pare)

# lista = [x ** 2 for x in range(1, 11) if x % 2 == 0]
# X**2 este forma in care vrei elemenetel in lista

# print(lista)

# lista = [3, 5, 7, 15, 21, 72, 56, 99]
# # lista_s = []  # numerele divizibile cu 3 si 5

# # lista_s = [x for x in lista if x % 3 == 0 and x % 5 == 0]
# # print(lista_s)

# x = any(x % 3 == 0 and x % 5 == 0 for x in lista)
# print(x)

# TUPLES - imutabil (ordonata, permite duplicate, indexabila)
# sse defineste cu ()
# Metode uzuale: *count(x) - numar de cate ori apare x in tupla
#               #*index(x) - returneaza indexul primei aparitii a lui x
# Metode utile: tuple(iter) - converteste un iterabil intr-o tupla.
# unpacking - atribuie valori dintr-o tubla in variabile separate
# Ex: a, b, c = (1, 2, 3)
# slicing: Extrage sub tuple
# iterare

# zile = ("Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica")
# print(zile)
# print(zile[3]) #---> Joi
# zile.count("luni") # ----> 1
# print(zile.index("vineri")) # ----> 4
# zile_lucratoare = zile[0:5]

# zile_i = tuple(zi for zi in zile if "i" in zi)
# tuplele trebuiesc castate ca atare,
# dar pot fi rezolvate tot cu list comprehention.
# print(zile_i)

# tuple_numere = (1, 2, 3, 4)
# print(tuple_numere)
# tuple_numere = list(tuple_numere)
# tuple_numere.append(5)
# tuple_numere = tuple(tuple_numere)
# print(tuple_numere)

# ceva = ("Ana", "Ionescu", "25")
# prenume, nume, varsta = ceva
# print(prenume, nume, varsta)
# pt unpack, e nevoie de tot atatea variabile, cate vrei sa scoti din tupla.

# SETURI
# fara o ordine anume, fara duplicate

# Metode:
# add(x)
# remove(x) daca elementul nu exista = Eroare
# discard(x) nu da eroare daca elementul nu exista
# pop(x)

# my_set = {1, 2, 3, 4, 5}
# print(my_set)
# my_set.add("5")
# print(my_set)

# lista_mea = [1,1,2,2,3, 4, 6, 7, 7]

# lista_mea = set(lista_mea)
# lista_mea = list(lista_mea)
# # SAU
# lista_mea = list(set(lista_mea))

# set1 = {1, 2, 3, 4, 5}
# print(set1)
# set2 = {3, 4, 7, 8, 9}
# print(set2)
# set1.update(set2) *adauga doar elemenete unice
# print(set1)

# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 7, 8, 9}
# set3 = {3, 4, 7, 8, 9, 10}

# # doar afisaza elementele impreuna, dar nu modifica seturile.
# print(set1.union(set2))
# print(set1.difference(set2))  # ---> 1, 2, 5
# print(set2.difference(set1))  # ---> 8, 9, 7
# print(set1.intersection(set2))  # ----> 3, 4
# print(set1.issubset(set2))  # ----> False
# print(set2.issubset(set3))  # -----> True
# print(set3.issuperset(set2))  # ------> True
# frozenset -----> il face si imutable
# comprehention merge doar cu {}
# print({x**2 for x in range(10)if x % 2 == 0})

# DICTIONARE: valoare, ordonata, mutable definit prin {} sau dict()
# metode:
# keys()
# values()
# items()
# pop(k)
# popitem()
# update(d)
# clear()

# var = {"Ana": 18, "Maria": 20, "Marian": 45}
# print(type(var))
# print(var["Ana"])
# print(var)
# var["Ana"] = 19
# print(var)
# buletine = [{"Nume": "Ana", "CNP": 123, "Varsta": 18},
#             {"Nume": "Marius", "CNP": 125, "Varsta": 22}]
# for persoana in buletine:
#     if persoana["Nume"] == "Ana" and persoana["CNP"] == 123:
#         persoana["Nume"] = "Rodica"

# bul1 = {"Nume": "Ana", "CNP": 123, "Varsta": 18}

# for key in bul1.keys():
#     print(key)
# print()
# for element in bul1.values():
#     print(element)
# print()
# for key, values in bul1.items():
#     print(key, values)

# print(var.keys())
# keys = list(var.keys())
# print(keys)

# bul1 = {"Nume": "Ana", "CNP": 123, "Varsta": 18}
# bul1["Nume Familie"] = "Ionescu"
# print(bul1)
# bul1.pop("Nume")
# print(bul1)
# print(bul1.popitem())
# print(bul1.get("Nume")) - # nu crapa
# print(bul1["Nume"]) - #crapa programul daca cheia nu exista
# bul1.update({"Nume": "Ana"})
# print(bul1)
# bul1.update([("Nume Familie", "Ionescu"), ("Salar", 150)])
# print(bul1)


# dict_mare = {
#     12345678: {
#         "nume": "popescu",
#         "prenume": "ionut",
#         "varsta": 20,
#         "masina": {
#             "marca": "bmw",
#             "vin": 12345,
#             "tip_c": "benzina"
#         }
#     },
#     12346778: {
#         "nume": "ionescu",
#         "prenume": "george",
#         "varsta": 45,
#         "masina": {
#             "marca": "mercedes",
#             "vin": 35489,
#             "tip_c": "motorina"
#         }
#     }
# }
# print(dict_mare[12345678]["masina"]["tip_c"])
# dict_mare[12345678]["masina"]["tip_c"] = "gpl"
# print(dict_mare.get(12345678).get("masina").update({"tip_c": "electric"}))
# print(dict_mare.get(12345678).get("masina").get("tip_c"))

# import json
# print(json.dumps(dict_mare, indent = 4))

# bul1 = {"Nume": "Ana", "CNP": 123, "Varsta": 18}
# # negasit in caz ca vrei o valoare in caz ca ceva nu exista
# print(bul1.get("masina", "negasit"))
# #setdefault creaza si o cheie si o valoare, cum ca nu are masina.
# bul1.setdefault("masina", "Nu are masina")
# print(bul1)

# d = {}
# print(d)
# d.setdefault("fructe", []).append("mar")
# print(d)
# d.setdefault("fructe", []).append("banana")
# print(d)
# d["fructe"] = ["mar", "banana", "portocala"]

# for fruct in ["mar", "banana", "portocala"]:
#     d.setdefault("fructe", []).append(fruct)

# print(d)

patrate = {x: x**2 for x in range(5)}
print(patrate)
