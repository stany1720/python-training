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

# a = input("Cat este variabila a?")
# b = input("Cat este variabila b?")
# c = input("Cat este variabila c?")

# if a < b and a < c:
#     print(a)
# elif b < a and b < c:
#     print(b)
# elif c < a and c < b:
#     print(c)

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

# found_vowels = [char for char in text if char in vowels]

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

# if text[0::] == text[:: -1]:
#     print("The first and last leets are the same!")
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

# for x in range(1, n):
#     if n % x == 0:
#         print(x)
# print(n)

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

# if capital and lower and digit:
#     print("This looks like a decent password...")
# else:
#     print("Let's try something elese for an input....")

# Exercitii pentru oameni supraincalziti (31-33):
# 31. Fizz Buzz: Primește un număr n și afișează numerele de la 1 la n. Pentru multiplii de 3, afișează "Fizz", pentru multiplii de 5, afișează "Buzz", iar pentru multiplii de ambele, afișează "FizzBuzz".

# n = int(input("Please provide a number! "))


# if n % 3 == 0 and n % 5 == 0:
#     print("FizzBuzz")
# elif n % 5 == 0:
#     print("Buzz")
# elif n % 3 == 0:
#     print("Fizz")
# else:
#     print("Let's try something else! ")


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
