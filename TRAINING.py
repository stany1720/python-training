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

# patrate = {x: x**2 for x in range(5)}
# print(patrate)


# ______________________________________________________________________________________

# str1 = 'ceva'
# str2 = str1

# print(id(str1))
# print(id(str2))
# # id - returneaza adresa de memorie
# str2 = str2 + "incaceva"
# print(id(str1))
# print(id(str2))
# lis1 = [1, 2, 3, 4]
# lis2 = lis1
# print(id(lis1))
# print(id(lis2))
# lis2[0] = 10
# print(id(lis1))
# print(id(lis2))
# print(lis1)
# print(lis2)
# lis1 = [1, 2, 3, 4]
# lis2 = lis1.copy

# print(id(lis1))
# print(id(lis2))
# import copy
# lis1 = [1, 2, [3, 4]]
# lis2 = copy.deepcopy(lis1)
# print(id(lis1))
# print(id(lis2))
# lis2[0] = 20
# lis2[2][0] = 10
# print(lis1)  # [1, 2, [10, 4]]
# print(lis2)  # [20, 2, [10, 4]]
# print(id(lis1[2]))
# print(id(lis2[2]))

# -----------------------------------------------------------------------------------

# Functii: definire
# Functii: apelare

# def func_basic():  # In paranteza se pun parametri
#     print('Salut din functie! ')
#     return 120


# print(func_basic())


# def afisaza_nume(nume, prenume):
#     print(f"Salut {nume} {prenume}!")


# afisaza_nume('Stanislav', 'Mihai')

# default value

# def afisaza_nume(nume='Stanislav', prenume='Mihai'):
#     print(f"Salut {nume} {prenume}!")


# # pentru valori default,
# # MEREU valoarea default este la final si parametrii trebuiesc atribuiti.
# afisaza_nume('Ionescu')

# def operatii(v1, v2):
#     return v1 + v2, v1 - v2, v1 * v2


# x, y, z = operatii(10, 20)
# print(x, y, z)

# VARIABILA_GLOBALA = "Ceva"

# def functie_extra(p1, p2):
#     global var
#     var = p1 + p2
#     print(var)


# functie_extra(100, 200)

# var += var
# print(var)


# Functii recursive: functie care se apeleaza pe ea insasi(necesita coditie de oprire)

# lista = [1, 2, 3, [1, 3, 5], 6, [1, [1, 2], 3]]

# lista_simpla = [1, 2, 3, 4, 5, 1, 7, 1]


# def frecventa_nr(lista_in_care_caut, nr_cautat):
#     counter = 0
#     for nr in lista_in_care_caut:
#         if isinstance(nr, list):
#             counter += frecventa_nr(nr, nr_cautat)
#         elif nr_cautat == nr:
#             counter += 1
#         else:
#             pass
#     return counter


# print(frecventa_nr(lista_simpla, 1))

# functii in functii ca parametru

# def aduna(lista_elemente):
#     suma = 0
#     for element in lista_elemente:
#         suma += element
#     return suma


# def produs(lista_elemente):
#     produsul = 1
#     for elem in lista_elemente:
#         produsul *= elem

#     return produsul


# def suma_liste(func, lista_cu_liste):
#     suma_totala = 0
#     for lista in lista_cu_liste:
#         print(lista)
#         print(func(lista))
#         suma_totala += func(lista)

#     return suma_totala


# lista = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# print("Suma sumelor elemntelor din liste este: ", suma_liste(aduna, lista))
# print("Suma produselor elementelor din liste este: ", suma_liste(produs, lista))

# dictionar = {}
# sorted(dictionar, key=dictionar.get)

# decoratorii = functia "decoreaza" ceva extra ce nu face prima functie pe care nu vrei s-o strici pe prima.

# argumente variabile: oricati parametrii vor veni, vor fi adaugati:

# def suma(p1, p2, *args):
#     print(p1)
#     print(p2)
#     print(args)
#     # s = p1 + p2
#     return sum(args)


# print(suma(10, 7))
# print(suma(10, 11, 12, 13))

# def suma2(p1, p2, **kwargs): #Kwargs necesita 2 stelute 1pt cheie 2pt valoare
#     print(p1)
#     print(p2)
#     print(kwargs)


# suma2(p1=10, p2=20, p3=30, p4=40)

# [DEBUG]

# def logare(*mesaje, **optiuni):
#     nivel = optiuni.get('nivel', 'INFO')
#     separator = optiuni.get('separator', ' ')
#     log_final = separator.join(str(mesaj) for mesaj in mesaje)
#     print(f"[{nivel}]{log_final}")


# action = "start program"
# user = "Anisoara"

# logare(f"Action: {action}", f"User: {user}", nivel="DEBUG", separator=" | ")
# logare("Eroare la conectare", nivel="ERROR")


# Sa se scrie un program care tine evidenta elevilor dintr-o scoala. Programul trebuie sa dispuna de un meniu care ne pune la dispozitie urmatoarele optiuni:
#         a. Adaugare elev
#         b. Afisarea elevilor existenti
#         c. Modificare informatii elev existent
#         d. Stergere elev
#         e. Cautare elev dupa nume si prenume
#         f. Afisare elevi in ordinea mediilor
#         g. Afisare elevi cu media peste 8
#         h. Afisare elevi in ordine alfabetica (dupa nume)

#     Pentru fiecare elev trebuie sa retinem urmatoarele informatii:
#     Nume
#     Prenume
#     Nota romana
#     Nota matematica
#     Nota engleza
#     Media

# Sa se scrie un program care tine evidenta elevilor dintr-o scoala. Programul trebuie sa dispuna de un meniu care ne pune la dispozitie urmatoarele optiuni:
# 		1. Adaugare elev
# 		2. Afisarea elevilor existenti
# 		3. Modificare informatii elev existent
# 		4. Stergere elev
# 		5. Cautare elev dupa nume si prenume
# 		6. Afisare elevi in ordinea mediilor
# 		7. Afisare elevi cu media peste 8
# 		8. Afisare elevi in ordine alfabetica (dupa nume)

# 	Pentru fiecare elev trebuie sa retinem urmatoarele informatii:
#     Nume
#     Prenume
#     Nota romana
#     Nota matematica
#     Nota engleza
#     Media

# Sa se scrie un program care tine evidenta elevilor dintr-o scoala. Programul trebuie sa dispuna de un meniu care ne pune la dispozitie urmatoarele optiuni:
# 		1. Adaugare elev
# 		2. Afisarea elevilor existenti
# 		3. Modificare informatii elev existent
# 		4. Stergere elev
# 		5. Cautare elev dupa nume si prenume
# 		6. Afisare elevi in ordinea mediilor
# 		7. Afisare elevi cu media peste 8
# 		8. Afisare elevi in ordine alfabetica (dupa nume)

# 	Pentru fiecare elev trebuie sa retinem urmatoarele informatii:
#     Nume
#     Prenume
#     Nota romana
#     Nota matematica
#     Nota engleza
#     Media

'''
Exercitii OOP in Python:
A) --- Exercitii - Introducere OOP si Clase
Creeaza o clasa numita "Animal" care are atributele "nume", "varsta" si "specie". Adauga o metoda numita "descriere" care returneaza o descriere a animalului.
Instantiaza doua obiecte ale clasei "Animal" si apeleaza metoda "descriere" pentru fiecare obiect.

Creeaza o clasa numita "Masina" care are atributele "marca", "model" si "an_fabricatie". Adauga o metoda numita "descriere" care returneaza o descriere a masinii.
Instantiaza trei obiecte ale clasei "Masina" si afiseaza informatiile despre fiecare masina.

3.
a) Creeaza o clasa numita "Persoana" care are atributele "nume", "varsta" si "gen".
b) Creeaza o lista de 5 persoane si afiseaza numele si varsta fiecarei persoane din lista.
c) Adauga o metoda numita "introducere" in clasa "Persoana" care returneaza o introducere a persoanei 
    (ex: "Numele meu este X, am Y ani si sunt de gen Z"). Apeleaza aceasta metoda pentru fiecare persoana din lista.
d) Creeaza o metoda numita "este_major" care returneaza True daca persoana are varsta de 18 ani sau mai mult, si False in caz contrar. 
    Apeleaza aceasta metoda pentru fiecare persoana din lista si afiseaza daca fiecare persoana este major sau nu.
e) Creeaza o metoda numita "schimba_gen" care schimba genul persoanei (ex: daca genul este "masculin", il schimba in "feminin" si invers). 
    Apeleaza aceasta metoda pentru fiecare persoana din lista si afiseaza noul gen al fiecarei persoane.
f) Creeaza o metoda numita "adauga_ani" care adauga un numar specificat de ani la varsta persoanei. 
    Apeleaza aceasta metoda pentru fiecare persoana din lista, adaugand un numar aleator de ani si afiseaza noua varsta a fiecarei persoane.
g) Afiseaza o lista cu toate persoanele care sunt majore.
h) Afiseaza o lista cu toate persoanele care au genul "masculin" si au peste 14 ani.
''' 

# class Persoana:
#     def __init__(self, nume, varsta, gen):
#         self.nume = nume
#         self.varsta = varsta
#         self.gen = gen

#     def introducere(self):
#         print(f'Numele meu este {self.nume}, am {self.varsta} ani si sunt de genul {self.gen}')

#     def este_major(self):
#         if self.varsta >= 18:
#             return True
#         return False
    
#     def schimba_gen(self):
#         if self.gen == "M":
#             self.gen = "F"
#         else:
#             self.gen = "M"

# persoane = [Persoana('Andrei', 20, "M"), Persoana('Alexandra', 32, "F"), Persoana('Maria', 16, 'F'), Persoana('Daniel', 31, "M")]


# while len(persoane) < 5:
#     nume = input("Introdu numele: ")
#     varsta = int(input(" Introdu varsta: "))
#     gen = input("Introdu genul: ")

#     persoana = Persoana(nume, varsta, gen)
#     persoane.append(persoana)

# for persoana in persoane:
    # print(f'Persoana {persoana.nume} are varsta {persoana.varsta}')
    # persoana.introducere()
    # print(f"{persoana.nume} - " , persoana.este_major())
    # persoana.schimba_gen()
    # persoana.introducere()


# Encapsulation and Abstraction

# class Elev: 
#     def __init__(self, nume, prenume, nota_romana, nota_mate, nota_engleza):
#         self.nume = nume
#         self.prenume = prenume
#         self.nota_romana = nota_romana 
#         self.nota_mate = nota_mate
#         self.nota_engleza = nota_engleza

# elev1 = Elev("Neamtiu", "Daniel", 8, 9, 10)

# # Protected: informeaza alti programatori sa nu se atinga de variabilele clasei

# class Elev: 
#     def __init__(self, nume, prenume, nota_romana, nota_mate, nota_engleza):
#         self._nume = nume
#         self._prenume = prenume
#         self._nota_romana = nota_romana 
#         self._nota_mate = nota_mate
#         self._nota_engleza = nota_engleza

# # Private: vezi media

# class Elev: 
#     def __init__(self, nume, prenume, nota_romana, nota_mate, nota_engleza, media):
#         self._nume = nume
#         self._prenume = prenume
#         self._nota_romana = nota_romana 
#         self._nota_mate = nota_mate
#         self._nota_engleza = nota_engleza
#         self.__media = media

# Getter/Setter: get x, sext x

# class Elev: 
#     def __init__(self, nume, prenume, nota_romana, nota_mate, nota_engleza, media):
#         self._nume = nume
#         self._prenume = prenume
#         self._nota_romana = nota_romana
#         self._nota_mate = nota_mate
#         self._nota_engleza = nota_engleza
#         self.__media = self._update_media()

#     def get_media(self):
#         return self.__media

#     def get_mate(self):
#         return self._nota_mate

#     def set_mate(self, new_mate):
#         if self._validare_nota(new_mate):
#             self._nota_mate = new_mate
#         else:
#             print("Nota trebuie sa fie intre 1 si 10")

#     def _update_media(self):
#         return round((self._nota_mate + self._nota_romana + self. _nota_engleza) / 3, 2)

#     def _validare_nota(self, new_nota):
#         if 0 < new_nota <= 10:
#             return True
#         else: return False

# elev1 = Elev("Neamtiu", "Daniel", 8, 9, 10, 9)
# print(elev1.get_media())

# class Ghiozdan:
#     def __init__(self, obiecte):
#         self.obiecte = obiecte

#     def __len__(self):
#         return len(self.obiecte)
    
#     def __str__(self):
#         return f"Ghiozdanul are urmatoarele {self.obiecte}"

#     def __repr__(self):
#         return f'Ghiozdan(obiecte = "{self.obiecte}")'

# lista = [1, 2, 3, 4]

# ghiozdan = Ghiozdan(lista)
# print(len(ghiozdan))
# print(ghiozdan)
# lista_ghiozdane = [Ghiozdan(lista), Ghiozdan([7, 8, 9]), Ghiozdan([2, 3, 4])]
# print(lista_ghiozdane)

# class Persoana:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"Persoana (nume = '{self.name}', age = {self.age})"

# persoana1 = Persoana("Alice", 30)
# print(repr(persoana1)) # Persoana(nume = 'Alice', age = 30)

# MOSTENIRE SI POLIMORFISM:
# Mostenire:
# Creezi o clasa de baza si apoi o clasa copil care pe langa standard, are trasaturi in plus. 
# Polimorfism:
# Folosesi clasa initiala din clasa de baza si adaugi trasaturi specifice(animnal vs. caine, pisica(una face miau, altul ham))

# Mostenire sintaxa:

# class Clasa Parinte:
#     cod

# class ClasaCopil(ClasaParinte):
#     cod copil

#  folosind super().__init__() poti prelua innit-ul din clasa parinte

# Exemple: 

# class Persoana:
#     def __init__(self, nume, prenume, varsta):
#         self.nume = nume
#         self.prenume = prenume
#         self.varsta = varsta

#     def prezentare(self):
#         print(f'Salut, ma numesc {self.prenume} {self.nume} si am {self.varsta} ani. ')

# persoana1 = Persoana("Stanislav", "Mihai", 38)
# persoana2 = Persoana("Abesei", "Paul", 31)

# persoana1.prezentare()
# persoana2.prezentare()

# class Elev(Persoana):
#     def __init__(self, nume, prenume, varsta, nota_romana, nota_mate):
#         super().__init__(nume, prenume, varsta)
#         self.nota_romana = nota_romana
#         self.nota_mate = nota_mate

    

# elev1 = Elev("Neamtiu", "Daniel", 15, 10, 10)

# elev1.prezentare()


# class Elev(Persoana):
#     def __init__(self, nume, prenume, varsta, nota_romana, nota_mate):
#         super().__init__(nume, prenume, varsta)
#         self.nota_romana = nota_romana
#         self.nota_mate = nota_mate

#     def afisaza_note(self):
#         print(f'Notele mele sunt la Romana: {self.nota_romana} si la Mate: {self.nota_mate}')

# elev1 = Elev("Neamtiu", "Daniel", 15, 10, 10)

# elev1.prezentare()
# elev1.afisaza_note()

# class Elev(Persoana):
#     def __init__(self, nume, prenume, varsta, nota_romana, nota_mate):
#         super().__init__(nume, prenume, varsta)
#         self.nota_romana = nota_romana
#         self.nota_mate = nota_mate

#     def prezentare(self):
#         super().prezentare() # RETURN NU E OBLIGATORIU
#         print(f'Am urmatoarele note la Romana: {self.nota_romana} si la Mate: {self.nota_mate}')

#     def afisaza_note(self):
#         print(f'Notele mele sunt la Romana: {self.nota_romana} si la Mate: {self.nota_mate}')

#     def calculeaza_media(self):
#         return sum([self.nota_romana, self.nota_mate]) / 2

# elev1 = Elev("Neamtiu", "Daniel", 15, 10, 10)
# elev2 = Elev("Ionescu", "Andrei", 15, 8, 9)

# elev1.prezentare()
# elev1.afisaza_note()
# print(elev1.calculeaza_media())

# lista_oameni = [persoana1, persoana2, elev1]
# for om in lista_oameni:
#     om.prezentare()

# class Profesor(Persoana):
#     def __init__(self, nume, prenume, varsta, materie):
#         super().__init__(nume, prenume, varsta)
#         self._materie = materie

#     def prezentare(self):
#         print(f'Eu sunt profesorul {self.nume}, am varsta de {self.varsta} ani, si predau materia {self.materie}')

#     def get_materie(self):
#         return self._materie

#     def __str__(self):
#         return f'{self.nume} {self.prenume}'

# class ElevLiceu(Elev):
#     def __init__(self, nume, prenume, varsta, nota_romana, nota_mate, diriginte):
#         super().__init__(nume, prenume, varsta, nota_romana, nota_mate)
#         self.diriginte = diriginte

#     def get_diriginte(self):
#         print(f'Dirigintele meu este {self.diriginte}. ')

#     def prezentare(self):
#         return super().prezentare()
    
#     def __str__(self):
#         return f'{self.nume} {self.prenume}' 


# profesor1 = Profesor("Marinescu", "Alexandru", 67, "Spaniola")
# profesor2 = Profesor("Andreescu", "Marin", 45, "Etica")

# elevliceu1 = ElevLiceu("Antonescu", "Maria", 17, 10, 9, profesor1)
# elevliceu2 = ElevLiceu("Parvulescu", "Alexandra", 16, 8, 9, profesor2)

# lista_scoala = [profesor1, profesor2, elev1, elev2, elevliceu1, elevliceu2]

# for persoana in lista_scoala:
#     persoana.prezentare()

# elevliceu1.get_diriginte()

# print(f'Dirigintele lui {elevliceu1} preda {elevliceu1.diriginte.get_materie()}')
# elevliceu1.diriginte.materie = "Germana"
# print(f'Dirigintele lui {elevliceu1} preda {elevliceu1.diriginte.get_materie()}')

# print(profesor1.materie) # Acum se creaza o noua variabila materie, deoarece _materie este protejat

