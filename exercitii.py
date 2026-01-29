# import click

# Exerciții de vacanță – recapitulare Python (variabile, operatori, stringuri, control flow)
# Perioada: 23 decembrie – 11 ianuarie

# Încălzire (1-10):
# 1. Creează două variabile cu valori numerice și afișează suma lor.

# a = 10
# b = 5

# print(a + b)

# # 2. Afișează produsul a două numere introduse de la tastatură.

# a = input("Cat este variabila a?")
# b = input("Cat este variabila b?")
# print(int(a) * int(b))

# 3. Primește un nume de la tastatură și afișează-l cu litere mari.

# name = input("What's your name? ")

# print(name.upper())

# # 4. Afișează lungimea unui string introdus de la tastatură.

# name = input("What's your name? ")
# print(len(name))

# 5. Verifică dacă un număr este par sau impar.

# a = 10
# b = 5

# if a % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# if b % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# # 6. Primește un text și un caracter, afișează de câte ori apare caracterul în text.

# text = "Cruchyroll"

# print(text.count("l"))

# 7. Afișează ultimul caracter dintr-un string introdus de la tastatură.

# text_1 = input("Input something here please!")

# print(text_1[-1])

# 8. Primește un număr și afișează dacă este pozitiv, negativ sau zero.

# numeber = int(input("Please provide a number!"))

# if numeber > 0:
#     print("Pozitiv")
# elif numeber == 0:
#     print("Zero")
# else:
#     print("Negativ")

# 9. Afișează toate caracterele unui string, câte unul pe linie.

# for letter in text:
#     print(letter)

# 10. Primește două numere și afișează cel mai mare dintre ele.

# if a > b:
#     print(a)
# elif a < b:
#     print(b)

# Exerciții pentru oameni incalziti (11-30):
# 11. Primește trei numere și afișează cel mai mic dintre ele.

# a = int(input("Cat este variabila a?"))
# b = int(input("Cat este variabila b?"))
# c = int(input("Cat este variabila c?"))

# # if a < b and a < c:
# #     print(a)
# # elif b < a and b < c:
# #     print(b)
# # else c < a and c < b:
# #     print(c)

# print(min(a, b, c))

# 12. Primește un text și verifică dacă este palindrom.

# print("Palindome finder: ")


# text_1 = input("Input something here please: ")


# if text_1[::-1] == text_1:
#     print("Palinfrom found!")
#     exit()
# elif text_1[::-1] != text_1:
#     print("Please try another word")

# 13. Primește o parolă și verifică dacă are cel puțin 8 caractere și conține o cifră.

# password = input("Please set a new password...")

# if len(password) >= 8 and any(char.isdigit() for char in password):
#     print("New password has been set! ")
# else:
#     print("Please check the password requirements and try again! ")

# 14. Primește un text și construiește un nou string numai cu vocalele din el.

# text = input("Please enter some text here... ")

# vowels = "aeiouAEIOU"

# found_vowels = "".join([char for char in text if char in vowels])

# print(found_vowels)

# 15. Primește un număr n și afișează toate numerele pare de la 0 la n (inclusiv).

# number = int(input("Please provide a number! "))

# for i in range(0, number + 1, 2):
#     print(i)

# 16. Primește un text și afișează doar literele mici din el.

# text = input("Please enter some text here... ")
# for char in text:
#     if char.islower():
#         print(char)

# 17. Primește două numere și afișează toate numerele între ele (inclusiv), în ordine crescătoare.

# a = int(input("Please provide the first number!"))
# b = int(input("Please provide the second number!"))

# for i in range(a, b+1):
#     print(i)

# 18. Primește un text și afișează fiecare cuvânt pe o linie nouă.

# text = input("Please provide your text here...!")

# for words in text.split():
#     print(words)

# 19. Primește un număr și afișează tabla înmulțirii pentru acel număr (de la 1 la 10).

# number = int(input("Please provide a number"))

# for i in range(1, 11):
#     print(number, "x", i, "=", number * i)

# 20. Primește un text și verifică dacă toate caracterele sunt litere mici.

# text = input("Please input your text here...")

# if text == text.lower():
#     print("All characters are lower case!")
# else:
#     print("There's some upper case letters in there!")

# 21. Primește un text și afișează-l inversat.

# text = input("Please provide your text")

# print(text[::-1])

# 22. Primește o propoziție și numără câte cuvinte conține.

# text = input("Please provide some text here for us to count!")

# print(len(text.split()))

# 23. Primește un text și înlocuiește toate spațiile cu caracterul "_".

# text = input("Please input some text!")

# print(text.replace(" ", "_"))

# 24. Primește un număr și afișează suma cifrelor sale.

# number = int(input("Please provide a number... "))
# list = []

# while number:
#     list.append(number % 10)
#     number = number // 10

# print(sum(list))

# print(number % 10)
# print(number // 10)

# 25. Primește un text și afișează doar caracterele care sunt cifre.

# text = input("Please provide some input.... ")

# note = " "
# for char in text:
#     if char.isdigit():
#         note += char

# print(f"The digits in the string are:  {note}")

# 26. Primește un text și verifică dacă începe și se termină cu aceeași literă.

# text = input("Please provide input....")

# if text[0] == text[-1]:
#     print("The first and last leters are the same!")
# else:
#     print("The first and last letters do not match!")

# 27. Primește un text și afișează toate caracterele distincte din el.

# text = input("Provide some input:... ")

# for char in text:
#     print(char)

# 28. Primește un text și afișează literele care apar de exact două ori.

# text = input("Gimme something to work with here... ")

# for char in set(text):
#     if text.count(char) == 2:
#         print("The duplicate letters are: " + char)

# 29. Primește un număr n și afișează toți divizorii săi.

# n = int(input("Please provide a number! "))

# for x in range(1, n+1):
#     if n % x == 0:
#         print(x)

# 30. Primește un text și verifică dacă are cel puțin o literă mare, una mică și o cifră.

# text = input("Please provide some text for me to check....")

# capital = False
# lower = False
# digit = False

# for char in text:
#     if char.isupper():
#         capital = True
#     if char.islower():
#         lower = True
#     if char.isdigit():
#         digit = True
#     if capital and lower and digit:
#         print("This looks like a decent password...")
#         break
# if not (capital and digit and lower):
#     print("Let's try something elese for an input....")

# Exercitii pentru oameni supraincalziti (31-33):
# 31. Fizz Buzz: Primește un număr n și afișează numerele de la 1 la n. Pentru multiplii de 3, afișează "Fizz", pentru multiplii de 5, afișează "Buzz", iar pentru multiplii de ambele, afișează "FizzBuzz".

# x = int(input("Please provide a number! "))

# for n in range(1, x+1):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 5 == 0:
#         print("Buzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     else:
#         print(n)

# 32. Primește un text și afișează-l cu fiecare cuvânt inversat, dar în aceeași ordine. (Exemplu: "Ana are mere" -> "anA era erem")

# text = input("Please provide some text to screw up...")
# result = ' '.join(word[::-1] for word in text.split())
# print(result)

# 33. Primește un text care contine o insiruire de numere și afișează media lor. (Exemplu: "1,2,3,4,5,10" -> 25/6 = 4.1666)

# text = "1,2,3,4,5,10"
# list1 = list(map(int, text.split(',')))

# multiplyer = len(list1)
# result = sum(list1) / multiplyer

# print(result)

# Spor la exersat și sărbători fericite!


# Trebuie implementat un meniu interactiv in consola care pune la dispozitie utilizatorului urmatoarele optiuni:
# Adunare
# Scadere
# Inmultire
# Impartire
# Iesire din program

# Utilizatorul trebuie sa introduca optiunea, iar apoi:
# Pentru optiunile 1->4, utilizatorul trebuie sa introduca doua numere, iar programul va afisa rezultatul operatiei.
# In cazul in care introduce 5, atunci iesim din program.

# Version 1:

# def adunare():
#     """Docstring for adunare"""
#     a = int(input("Te rog sa intoduci primul numar..."))
#     b = int(input("Te rog sa introduci al doilea numar..."))
#     print("Rezultatul adunarii este: ", a + b)
#     return True


# def scadere():
#     """Docstring for scadere"""
#     a = int(input("Te rog sa intoduci primul numar..."))
#     b = int(input("Te rog sa introduci al doilea numar..."))
#     print("Rezultatul scaderii este: ", a - b)
#     return True


# def inmultire():
#     """Docstring for inmultire"""
#     a = int(input("Te rog sa intoduci primul numar..."))
#     b = int(input("Te rog sa introduci al doilea numar..."))
#     print("Rezultatul inmultirii este: ", a * b)
#     return True


# def impartire():
#     """Docstring for impartire"""
#     a = int(input("Te rog sa intoduci primul numar..."))
#     b = int(input("Te rog sa introduci al doilea numar..."))
#     if a == 0 and b == 0:
#         print("Eroare: Împărțirea la zero nu este permisă!")
#     else:
#         print("Rezultatul impartirii este: ", a / b)
#         return True


# def main():
#     """Docstring for main"""
#     while True:
#         alegere = click.prompt(
#             "1. Adunare \n2. Scadere \n3. Inmultire \n4. Impartire \n5. Iesire din program \nTe rog sa alegi o optiune", type=int)
#         if alegere == 1:
#             adunare()
#         elif alegere == 2:
#             scadere()
#         elif alegere == 3:
#             inmultire()
#         elif alegere == 4:
#             impartire()
#         elif alegere == 5:
#             click.echo("La revedere! ")
#             break
#         else:
#             print(
#                 "Optiunea aceasta nu exista, te rog sa incerci din nou..")


# if __name__ == "__main__":
#     main()


# Version 2 - 1x input, toate operatiile

# def numere():
#     """Preluam input"""
#     a = click.prompt("Te rog sa intoduci primul numar...", type=int)
#     b = click.prompt("Te rog sa introduci al doilea numar...", type=int)
#     return a, b


# a, b = numere()


# def adunare():
#     """Docstring for adunare"""
#     print("Rezultatul adunarii este: ", a + b)
#     return True


# def scadere():
#     """Docstring for scadere"""
#     print("Rezultatul scaderii este: ", a - b)
#     return True


# def inmultire():
#     """Docstring for inmultire"""
#     print("Rezultatul inmultirii este: ", a * b)
#     return True


# def impartire():
#     """Docstring for impartire"""
#     if a == 0 or b == 0:
#         print("Eroare: Împărțirea la zero nu este permisă!")
#     else:
#         print("Rezultatul impartirii este: ", a / b)
#         return True


# def main():
#     """Docstring for main"""
#     while True:
#         alegere = click.prompt(
#             "1. Adunare \n2. Scadere \n3. Inmultire \n4. Impartire \n5. Iesire din program \nTe rog sa alegi o optiune", type=int)
#         if alegere == 1:
#             adunare()
#         elif alegere == 2:
#             scadere()
#         elif alegere == 3:
#             inmultire()
#         elif alegere == 4:
#             impartire()
#         elif alegere == 5:
#             click.echo("La revedere! ")
#             break
#         else:
#             print(
#                 "Optiunea aceasta nu exista, te rog sa incerci din nou..")


# if __name__ == "__main__":
#     main()

# Version 3: GPT

# def get_numbers():
#     """Funcție utilitară pentru a prelua input validat de la utilizator."""
#     a = click.prompt("Primul număr", type=float)
#     b = click.prompt("Al doilea număr", type=float)
#     return a, b


# def execute_operation(operation_name, func):
#     """Execută o operație matematică și afișează rezultatul."""
#     try:
#         a, b = get_numbers()
#         rezultat = func(a, b)
#         click.echo(click.style(
#             f"Rezultatul {operation_name} este: {rezultat}", fg="green", bold=True))
#     except ZeroDivisionError:
#         click.echo(click.style(
#             "Eroare: Împărțirea la zero nu este permisă!", fg="red"))
#     except Exception as e:
#         click.echo(f"A apărut o eroare neașteptată: {e}")


# @click.command()
# def main():
#     """Calculator CLI optimizat folosind Click."""
#     # Definim operațiile într-un dicționar pentru a evita structurile if/elif lungi
#     operations = {
#         1: ("adunării", lambda a, b: a + b),
#         2: ("scăderii", lambda a, b: a - b),
#         3: ("înmulțirii", lambda a, b: a * b),
#         4: ("împărțirii", lambda a, b: a / b)
#     }

#     while True:
#         click.echo("\n--- Meniu Calculator ---")
#         click.echo(
#             "1. Adunare\n2. Scădere\n3. Înmulțire\n4. Împărțire\n5. Ieșire")

#         # click.prompt cu type=click.IntRange asigură că primim doar numere între 1 și 5
#         alegere = click.prompt("Alegeți o opțiune", type=click.IntRange(1, 5))

#         if alegere == 5:
#             click.echo("La revedere!")
#             break

#         # Extragem numele și funcția corespunzătoare din dicționar
#         nume, func = operations[alegere]
#         execute_operation(nume, func)


# if __name__ == "__main__":
#     main()

# 1) Sa se afiseze toate puterile lui 2 aflate intre un interval dat de utilizator.
# Exemplu: 10, 50 -> 16, 32

# a = int(input("First number is... "))
# b = int(input("Second number is..."))
# c = int(input("What is the interval..."))

# for i in range(a, b, c):
#     if (i % 2 == 0):
#         print(i)


# 3) Creează o listă cu 7 numere întregi, apoi afișează suma și media elementelor fara a utiliza functiile sum() si avg().
# Exemplu: [1,2,3,4,5,6,7] -> suma=28, media=4.0

# list = [1, 2, 3, 4, 5, 6, 7]

# a = list[0]
# b = list[1]
# c = list[2]
# d = list[3]
# e = list[4]
# f = list[5]
# g = list[6]

# suma = a + b + c + d + e + f + g
# media = (a + b + c + d + e + f + g) / 7

# print(suma)
# print(media)

# 4) Primește o listă de la tastatură (elemente separate prin spațiu) și afișează lista inversată.
# Exemplu: input: 1 2 3 4 5 -> output: [5,4,3,2,1]

# a = []
# n = int(input("Enter the number of elements: "))
# for i in range(n):
#     element = input(f"Enter element {i+1}: ")
#     a.append(element)

# a.sort(reverse=True)
# print(a)


# 5) Afișează toate elementele de pe poziții impare dintr-o listă dată.
# Exemplu: [10,20,30,40,50,60] -> 20,40,60

# list1 = [10, 20, 30, 40, 50, 60]
# list2 = list1[1::2]

# print(list2)

# 6) Înlocuiește toate aparițiile unui element dat cu altă valoare într-o listă.
# Exemplu: [1,2,3,2,4], inlocuieste 2 cu 5 -> [1,5,3,5,4]

# a = [1, 2, 3, 2, 4]

# userinput = input('please choose a number from 1-4: ')
# x = int(input("What's the new number? "))
# a = [num if num != int(userinput) else x for num in a]
# print(a)


# 7) Afișează elementul maxim și minim dintr-o listă fără a folosi funcțiile max/min.
# Exemplu: [3,1,4,1,5,9,2] -> max=9, min=1

# list1 = [3, 1, 4, 1, 5, 9, 2]
# list1.sort()
# print("Max is: ", list1[-1])
# print("Min is: ", list1[0])

# max = list1[0]
# min = list1[0]

# for i in list1:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i

# 8) Elimină toate elementele pare dintr-o listă de numere.
# Exemplu: [1,2,3,4,5,6] -> [1,3,5]

# list1 = [1, 2, 3, 4, 5, 6]

# for i in list1:
#     if i % 2 == 0:
#         list1.remove(i)

# print(list1)

# 9) Primește o listă de stringuri și construiește o nouă listă cu stringurile care conțin litera 'a'.
# Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'masina']

# mylist = ['ana', 'mere', 'casa', 'masina']
# mylist2 = []

# for word in mylist:
#     if "a" in word:
#         mylist2.append(word)

# print(mylist2)

# 10) Verifică dacă o listă este palindrom (se citește la fel de la stânga la dreapta și invers).
# # Exemplu: [1,2,3,2,1] -> True, [1,2,3,4] -> False

# a = [1, 2, 3, 2, 1]
# b = [1, 2, 3, 4]

# if a == list(reversed(a)):
#     print("List is a palindrome. ")

# else:
#     print("List is not a plaindrom. ")

# if b == list(reversed(b)):
#     print("List is a palindrome. ")

# else:
#     print("List is not a plaindrom. ")

# 11) Interclasează două liste de aceeași lungime într-o singură listă.
# # Exemplu: [1,2], [3,4] => [1,3,2,4]

# a = [1, 2]
# b = [3, 4]

# print(a + b)

# 12) Creează o listă de liste [index, valoare] pentru fiecare element dintr-o listă dată.
# # Exemplu: [10,20,30] -> [[0,10],[1,20],[2,30]]

# a = [10, 20, 30]

# for index, value in enumerate(a):
#     print(f"{index} -> {value}")

# 13) Primește o listă de numere și elimină toate elementele care apar de mai mult de o dată (păstrează doar elementele unice).
# Fara a folosi set().
# # Exemplu: [1,2,2,3,4,4,5] -> [1,3,5]

# a = [1, 2, 2, 3, 4, 4, 5]

# rezultat = [i for i in a if a.count(i) == 1]

# print(rezultat)

# 14) Primește o listă de numere și grupează elementele în două liste: una cu numere negative, alta cu numere pozitive și zero.
# # Exemplu: [10,-1,2,-3,0,4,-5] -> negative: [-1,-3,-5], pozitive_si_zero: [10,2,0,4]

# a = []
# n = int(input("Enter the number of elements: "))

# for i in range(n):
#     element = int(input(f"Enter element {i+1}: "))
#     a.append(element)

# pozitive = []
# negative = []

# for element in a:
#     if element >= 0:
#         pozitive.append(element)
#     elif element < 0:
#         negative.append(element)

# print("Numerele pozitive sunt: ", pozitive)
# print("Numerele negative sunt: ", negative)


# 15) Primește o listă de stringuri și sorteaz-o crescător după numărul de vocale din fiecare string.
# Fara a folosi functia sort() sau sorted().
# # Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'mere', 'masina']

# ??????????????????????

# list1 = ['ana', 'mere', 'casa', 'masina', 'urs']


# def numar_vocale(s):
#     vocale = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vocale:
#             count += 1
#     return count


# print(list1)


# 16) Primește o listă de liste (matrice) și calculează suma elementelor de pe diagonala principală (doar dacă matricea este pătratică).
# # Exemplu: [[1,2,3],[4,5,6],[7,8,9]] -> 15 (1+5+9)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# if len(matrix[0]) == len(matrix[1]) == len(matrix[2]):
#     print(matrix[0][0] + matrix[1][1] + matrix[2][2])

# 17) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel], [10.2, 7.5, 3.4]]. Sa se extraga numele "Ionut" si sa se afiseze.

# lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]

# print(lista[1][1])

# 18) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel], [10.2, 7.5, 3.4]]. Sa se extraga litera "r" din numele "Marcel" si sa se afiseze.

# lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]

# print(lista[1][2][-4])

# 19) Sa se numere de cate ori apare un element intr-o lista incluzand si listele imbricate.
# # Exemplu: [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]] si elementul 1 -> apare de 4 ori

# lista = [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]]


# def count(l):
#     total = 0
#     for x in l:
#         if isinstance(x, list):
#             total += count(x)
#         elif x == 1:
#             total += 1
#     return total


# rezultat = count(lista)
# print(f"Elementul 1 apare in lista de  ", rezultat, "ori.")

# SAU

# lista_elemente = [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]]
# element = 1

# count = 0
# index = 0
# while index < len(lista_elemente):
#     if isinstance(lista_elemente[index], list):
#         lista_elemente.extend(lista_elemente[index])
#     else:
#         if lista_elemente[index] == element:
#             count += 1

#     index += 1

# 20) Scrieti un program care sa genereze un numar aleator intre 1 si 100. Utilizatorul trebuie sa
# ghiceasca numarul, iar programul sa ii ofere indicatii daca numarul introdus este mai mare sau mai mic decat cel generat.
# Programul se termina cand utilizatorul ghiceste numarul corect sau daca introduce cuvantul exit. La final se afiseaza numarul de incercari facute.

# import random

# def cere_numar():
#     """Cere input de la utilizator și îl returnează."""
#     return input("Introdu un număr (sau 'exit' pentru a ieși): ")


# def main():
#     """Docstring main"""
#     numar_aleator = random.randint(1, 100)

#     while True:
#         raspuns = cere_numar()
#         if raspuns.upper() == "EXIT":
#             print("Joc încheiat.")
#             break

#         try:
#             incercare = int(raspuns)
#         except ValueError:
#             print("Te rog introdu un număr valid sau 'exit'.")
#             continue

#         if incercare > numar_aleator:
#             print("Numărul tău este prea mare!")
#         elif incercare < numar_aleator:
#             print("Numărul pe care îl cauți este mai mare.")
#         else:
#             print(f"Felicitări! Ai ghicit numărul {numar_aleator}!")
#             break


# # SAU

# import random
# numar_ales = random.randint(1,100)
# print(numar_ales)
# nr_g = ''
# count = 1
# flag = True
# while flag :
#     nr_g = (input("Ghiceste numar : "))
#     if numar_ales == nr_g :
#         print ("ai gasit numarul")
#         flag = False
#     elif int(nr_g) > numar_ales :
#         print("Numarul ghicit e mai mare ")
#         count += 1
#     else :
#         print("Numarul ghicit e mai mic ")
#         count += 1
#     if nr_g == "exit" :
#         flag = False # break
# print("Ti-a luat "+str(count)+" incercari sa ghicesti")

# Pentru generarea numarului aleator:
# import random
# numar_aleator = random.randint(1, 100)

# 21) Sa se scrie un program primeste date in urmatorul format: "Nume: Ionescu Prenume: Ion" pana cand se introduce
# caracterul #. Programul trebuie sa stocheze toate datele citite, iar la final sa le afiseze in ordine alfabetica
# in functie de numele de familie.

# lista = []
# sublista = []

# while True:
#     data = input("Introdu un nume: ")
#     if data == "#":
#         print("iesire")
#         break
#     else:
#         sublista.append(data)
#         data = input("Introdu un prenume: ")
#         sublista.append(data)
#         lista.append(sublista)
#         # treci pe indexul urmator in lista
#         sublista = []  # resetare sublista pentru urmatorul nume prenume

# lista.sort()
# print("Lista sortata este : ", lista)

# sau CHAT GPT

# persoane = []
# for _ in range(1000):   # număr suficient de mare
#     linie = input("Introdu datele: ")
#     if linie == "#":
#         break
#     parti = linie.split()
#     nume = parti[0]
#     prenume = parti[1]
#     persoane.append([nume, prenume])
# # sortare alfabetică după numele de familie
# persoane.sort(key=lambda x: x[0])
# # afișare
# for p in persoane:
#     print(f"Nume: {p[0]} Prenume: {p[1]}")

# SAU

# date_intrare = []
# while True:
#     date = input(
#         "Introduceti datele in formatul 'Nume: Ionescu Prenume: Ion' sau '#' pentru a termina: ")
#     if date == "#":
#         break
#     date_intrare.append(date)
# date_intrare.sort()
# print("Datele in ordine alfabetica dupa numele de familie:")
# for date in date_intrare:
#     print(date)

# Folositi list comprehension pentru a rezolva urmatoarele exercitii:
# 1) Creeaza o lista cu patratele numerelor de la 0 la 9. Ex: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# list = []

# for x in range(0, 10):
#     list.append(x*x)

# SAU

# list = [x**2 for x in range(10)]

# print(list)

# 2) Creeaza o lista cu toate numerele pare divizibile cu 3 dintre 1 si 50 inclusiv. Ex: [6, 12, 18, 24, 30, 36, 42, 48]

# list1 = []

# for x in range(1, 51):
#     if (x % 2 == 0 and x % 3 == 0):
#         list1.append(x)

# SAU

# list1 = [x for x in range(50) if x % 3 == 0 and x % 2 == 0]

# print(list1)

# 3) Dintr-o lista cu cuvinte creeaza o lista cu lungimile fiecarui cuvant. Ex: ['ana', 'maria', 'ion', 'marioara', '1468912'] -> [3, 5, 3, 8, 7]

# lista = ['ana', 'maria', 'ion', 'marioara', '1468912']

# lista2 = [len(x) for x in lista]
# print(lista2)

# 4) Dintr-o lista cu numere de la 1 la 50, creeaza o lista cu patratele numerelor care sunt divizibile cu 4 si cu 6. Ex: [144, 576, 1296, 2304]

# lista = [x**2 for x in range(1, 50) if x % 4 == 0 and x % 6 == 0]
# print(lista)

# 5) Creeaza o lista cu toate vocalele dintr-un text dat. Ex: 'Aceasta este o propozitie de test.' -> ['A', 'e', 'a', 'a', 'e', 'o', 'o', 'i', 'i', 'e', 'e']

# vocale = "aeiouAEIOU"
# text = 'Aceasta este o propozitie de test.'
# lista = [x for x in text if x in vocale]
# print(lista)

# Folositi any pentru rezolvarea urmatoarelor exercitii:
# 1) Verifica daca intr-o lista de numere exista cel putin un numar par. Ex: [1, 3, 5, 7, 8] -> True

# lista = [1, 3, 5, 7, 8]

# a = any(x for x in lista if x % 2 == 0)
# print(a)

# 2) Verifica daca intr-o lista de cuvinte exista cel putin un cuvant care sa contina litera 'z'. Ex: ['ana', 'maria', 'ioana', 'zebra'] -> True

# lista = ['ana', 'maria', 'ioana', 'zebra']

# a = any("z" in char for char in lista)
# print(a)

# 3) Verifica daca intr-o lista de numere exista cel putin un numar negativ. Ex: [4, 5, -1, 3, 0] -> True

# lista = [4, 5, -1, 3, 0]

# b = any(x for x in lista if x < 0)
# print(b)


# 4) Verifica daca intr-o lista de stringuri exista cel putin un string care sa fie gol. Ex: ['ana', '', 'maria'] -> True

# lista = ['ana', '', 'maria']

# atribuire de spatiu, nu verificare de valoare.
# c = any(x == "" for x in lista)
# print(c)

# SAU

# c = any(not i for i in lista)
# print(c)

# 5) Verifica daca intr-o lista de caractere exista cel putin o vocala mare (A, E, I, O, U). Ex: ['a', 'b', 'C', 'D', 'E'] -> True

# lista = ['a', 'b', 'C', 'D', 'E']
# vowels = "aeiouAEIOU"

# d = any(x for x in lista if x in vowels and x.upper())
# print(d)

# sau - PAUL

# vowels = "AEIOU"
# d = any(x for x in lista if x in vowels)

# print(d)


# Exercitii pentru tuples:
# 1) Creează un tuplu care conține numele a trei fructe și afișează-le pe ecran.
#     Exemplu: ('măr', 'banană', 'cireașă') -> măr, banană, cireașă

# tup = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
# tup2 = ('nectarina', 'pruna')

# f1, f2, f3, f4, f5 = tup
# print(f1, f2, f3, f4, f5)

# Se da tuplul: fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi').

# 2) Afișează al doilea și al patrulea fruct din tuplu.

# print(tup[1:4:2])

# 3) Afișează tuplul inversat.

# print(tup[::-1])

# 4) Verifică dacă 'kiwi' este în tuplu și afișează un mesaj corespunzător.

# a = any(x == "kiwi" for x in tup)
# print(a)

# 5) Creează un tuplu nou care conține doar fructele de la pozițiile(index) pare din tuplul original.

# tup1 = tup[1::2]
# print(tup1)

# 6) Afișează lungimea fiecarui element din tuplu.

# list1 = []
# for element in tup:
#     list1.append(len(element))
# print(list1)

# 7) Concatenează tuplul cu un alt tuplu care conține alte două fructe și afișează rezultatul.

# print(tuple(list(tup) + list(tup2)))

# 8) Adauga un fruct nou 'ananas' in tuplu.

# l1 = list(tup2)
# l1.append('ananas')

# print(tuple(list(tup) + list(l1)))

# 9) Se da tuplul: ('măr', 'banană', 'cireașă'). Faceti unpacking pentru a extrage fiecare element in variabile separate
#    si afisati-le.

# f1, f2, f3, f4, f5 = tup
# print(f1, f2, f3, f4, f5)

# Exerciții pentru seturi:
# 1) Creează un set care conține numele a cinci culori și afișează-le pe ecran.

# set1 = {'rosu', 'galben', 'albastru', 'alb', 'negru'}
# print(set1)

# 2) Adaugă o culoare nouă în setul de mai sus și afișează setul actualizat.

# set1.add("verde")
# print(set1)

# 3) Elimină o culoare din set și afișează setul actualizat.

# set1.remove("alb")
# print(set1)

# 4) Verifică dacă o anumită culoare (de exemplu, 'albastru') este în set și afișează un mesaj corespunzător.

# if "albastru" in set1:
#     print("albastru" in set1)
# else:
#     print("Fals")

# 5) Creează un alt set cu alte trei culori și afișează elementele comune din cele două seturi.

# set2 = {'rosu', 'galben', 'albastru', 'violet', 'portocaliu'}

# print(set1.intersection(set2))

# 6) Afișează toate culorile din primul set care nu sunt în al doilea set.

# print(set1.difference(set2))

# 7) Se da lista: [1, 3, 5, 1, 6, 7, 9, 9, 1, 3, 4, 7, 1, 6, 7, 9, 5, 3, 3, 2, 1, 8, 4]. Eliminati duplicatele din lista,
#    astfel incat fiecare element sa apara o singura data.

# lista = [1, 3, 5, 1, 6, 7, 9, 9, 1, 3, 4, 7, 1, 6, 7, 9, 5, 3, 3, 2, 1, 8, 4]
# print(set(lista))

# exp1 = "((a + b) * (c - d) + e) / f - (g * (h + i))"
# exp2 = "((a + b) * (c - d) + e) / f - )g * (h + i)("

# count = 0

# for i in exp1:
#     if count < 0:
#         break
#     if i == "(":
#         count += 1
#     elif i == ")":
#         count -= 1
# if count == 0:
#     print("Corect")
# else:
#     print("Incorect")

# exp1 = "((a + b) * (c - d) + e) / f - (g * (h + i))"
# exp2 = "((a + b) * (c - d) + e) / f - )g * (h + i)("
# # SAU

# lista = []

# for char in exp2:
#     if char == "(":
#         lista.append(char)
#     elif char == ")":
#         lista.append(char)

# lista2 = []
# flag = False

# for char in lista:
#     if char == "(":
#         lista2.append(char)
#     elif char == ")":
#         if len(lista2) > 0:
#             lista2.pop()
#         elif len(lista2) == 0:
#             print("Incorrect")
#             flag = True
#             break

# if len(lista2) != 0:
#     print("Ai prea multe paranteze deschise! ")
# elif flag is False:
#     print("Corect!")
# stack = []

# # append() function to push element in the stack
# stack.append('a')
# stack.append('b')
# stack.append('c')

# print('Initial stack')
# print(stack)
# # pop() function to pop element from stack in LIFO order
# print('\nElements popped from stack:')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print('\nStack after elements are popped:')
# print(stack)

# # uncommenting print(stack.pop()) will cause an IndexError as the stack is now empty

# 1) Creeaza un dictionar care sa contina numele si varsta a 5 persoane.


import statistics  # pentru ex. 5

d1 = {'Adrian': 70, 'Doina': 67, 'Maria': 98, 'Mihai': 38, 'Madalina': 37}

# 2) Afiseaza varsta unei persoane specifificate de utilizator.

# persoana = input("Vartsa carei persoane vrei sa o afli? ")

# print(d1[persoana])

# 3) Afiseaza cea mai mare si cea mai mica varsta din dictionar.

# print(max(list(d1.values())))
# print(min(list(d1.values())))

# 4) Adauga 3 noi persoane in dictionar.

d1.update({'Alexandru': 18, 'Claudia': 25, 'Ioana': 32})
# print(d1)

# 5) Afiseaza varsta medie a persoanelor din dictionar.

print(statistics.mean(d1.values()))

# 6) Sterge o persoana specificata de utilizator din dictionar.

# victima = input('Specify the person that should dissappear... ')
# d1.pop(victima)
# print(d1)

# 7) Afiseaza toate persoanele cu varsta peste o valoare specificata de utilizator.

# varsta_min = int(input("What's the minimum legal age? "))

# for keys, values in d1.items(): #items() iterates over (key, value) tuples!
#     if values >= varsta_min:
#         print(keys, values)

# 8) Afiseaza toate persoanele din dictionar in urmatorul format: "Nume: <nume_persoana>, Varsta: <varsta_persoana>".

# for keys, values in d1.items():
#     print('Nume:', keys, ",", 'Varsta:', values)

# 9) Verifica daca o persoana specificata de utilizator exista in dictionar.

# search = input('Ca cautam azi in dictionar? ')
# print(d1.get(search))

# 10) Actualizeaza varsta unei persoane specificate de utilizator.

# older = input('Who is older now? ')
# old = (input('How old are they? '))

# d1[older] = old
# print(d1)

# 11) Afiseaza numarul total de persoane din dictionar.

# print(len(list(d1.values())))

# 12) Creeaza o lista cu toate numele persoanelor din dictionar si afiseaza-le.

# lista = []

# for keys in d1:
#     lista.append(keys)

# print(lista)

# 13) Creeaza un nou dictionar care sa contina doar persoanele cu varsta peste 18 ani.

d1.update({'Catalina': 10, 'Serban': 5, 'Razvan': 2, 'Alina': 32, 'Ion': 109})
# print(d1)
# d2 = {k: v for k, v in d1.items() if v >= 18}
# print(d2)

# 14) Creeaza o lista care contine toate varstele din dictionar, fara duplicate, si afiseaz-o.

# print(list(set(d1.values())))

# 15) Afiseaza persoana cu cea mai apropiata varsta de o valoare specificata de utilizator.

# varsta = int(input('Ce varsta cautam? '))
# cheia = None
# dif_min = 999

# for k, v in d1.items():
#     dif_actuala = abs(v - varsta)
#     if dif_actuala < dif_min:
#         dif_min = dif_actuala
#         cheia = k
# print(cheia)

# 16) Afiseaza toate persoanele grupate dupa decadele varstei (0-9, 10-19, 20-29, etc.).

# for k, v in d1.items():
#     if v in range(0, 9):
#         print('Persoanele cu varsta cuprinsa intre 0 si 9 ani sunt: ', k)
#     elif v in range(10, 19):
#         print('Persoanele cu varsta cuprinsa intre 10 si 19 ani sunt: ', k)
#     elif v in range(20, 29):
#         print('Persoanele cu varsta cuprinsa intre 20 si 29 ani sunt: ', k)
#     elif v in range(30, 39):
#         print('Persoanele cu varsta cuprinsa intre 30 si 39 ani sunt: ', k)
#     elif v in range(40, 49):
#         print('Persoanele cu varsta cuprinsa intre 40 si 49 ani sunt: ', k)
#     elif v in range(50, 59):
#         print('Persoanele cu varsta cuprinsa intre 50 si 59 ani sunt: ', k)
#     elif v in range(60, 69):
#         print('Persoanele cu varsta cuprinsa intre 60 si 69 ani sunt: ', k)
#     elif v in range(70, 79):
#         print('Persoanele cu varsta cuprinsa intre 70 si 79 ani sunt: ', k)
#     elif v in range(80, 89):
#         print('Persoanele cu varsta cuprinsa intre 80 si 89 ani sunt: ', k)
#     elif v in range(90, 99):
#         print('Persoanele cu varsta cuprinsa intre 90 si 99 ani sunt: ', k)
#     else:
#         print('Astia bantuie....', k)

# 17) Afiseaza persoanele sortate alfabetic dupa nume. (Utilizati functia sorted pentru a rezolva acest exercitiu).

# print(sorted(list(d1)))

# 18) Afiseaza persoanele sortate dupa varsta, de la cea mai mica la cea mai mare. (Utilizati functia sorted pentru a rezolva acest exercitiu).
#    (Folositi functia sorted() si pentru cheia de sortare (key) accesati valorile dictionarului).

# print(sorted(list(d1.values())))

# 19) Se da urmatorul text: "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani".
#     Creeaza un dictionar care sa contina numele persoanelor ca si chei si varstele ca si valori.
text = 'Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani'

d2 = {item.split(" are ")[0]: int(item.split(" are ")[
    1].replace(" ani", "")) for item in text.split(", ")}
print(d2)

# 20) Se da urmatorul text: "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani".
#     Creeaza un dictionar care sa stocheze frecventa literelor din text si afiseaza-l. Exemplu: {'a': 7, 'n': 3, ... }.

text = 'Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani'

d3 = {char: text.count(char) for char in text if char.isalpha()}
print(d3)
