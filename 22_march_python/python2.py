#1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

i = 0
fibonacci = [1 , 1]
while (len(fibonacci) != 20):
       value = fibonacci[i] + fibonacci[i + 1]
       fibonacci.append(value)
       i += 1
for items in fibonacci:
       print(items)

#2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

sayi=int(input("Sayı giriniz :"))
x=0
i=1
while i<sayi:
    if (sayi%i==0):
        x=x+i
    i+=1

if (x==sayi):
    print("Mükemmel sayıdır.")
else:

    print("Mükemmel sayı değildir. ")

#3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

number = int(input("Sayı giriniz: "))
number2 = int(input("Sayı giriniz: "))

def isprime(number):
    i = 2
    if number == 2:
        return True
    while i < number:
        if (number % i == 0):
            return False
        i+=1
    return True

def lcm(number, number2): #ekok
    number_array = []
    x = 1
    i = 2
    while number > 1 or number2 > 1:
        while isprime(i) and (number % i == 0 or number2 % i == 0):
            if number % i == 0 and number2 % i == 0:
                number = number / i
                number2 = number2 / i
            elif number % i == 0:
                number = number / i
            elif number2 % i == 0:
                number2 = number2 / i
            number_array.append(i)
        i += 1
    for i in number_array:
        x *= i
    return x

def gcd(number, number2):  #ebob
    number_array = []
    x = 1
    i = 2
    while number > 1 or number2 > 1:
        while isprime(i) and (number % i == 0 or number2 % i == 0):
            if number % i == 0 and number2 % i == 0:
                number_array.append(i)
                number = number // i
                number2 = number2 // i
            elif number % i == 0:
                number = number // i
            elif number2 % i == 0:
                number2 = number2 // i
        i += 1
    for i in number_array:
        x *= i
    return x

print("ebob:" + str(gcd(number, number2)))
print("ekok:" + str(lcm(number, number2)))



#diğer seçenek

def ebob_bulma(sayi1 , sayi2):
    i = 1
    ebob = 1
    while (i <= sayi1 and i <= sayi2):
        if not sayi1 % i and not sayi2 % i :
            ebob = i
        i += 1

    return ebob

def ekok_bulma(sayi1, sayi2):
    return sayi1 * sayi2 / ebob_bulma(sayi1,sayi2)

sayi1 = int(input("sayi1: "))
sayi2 = int(input("sayi2: "))

print("Ebob: ",ebob_bulma(sayi1,sayi2))
print("Ekok: ",ekok_bulma(sayi1,sayi2))



#4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

number = int(input("Bir sayı giriniz: "))
def isprime(number):
    i = 2
    if number == 2:
        return True
    while i < number:
        if (number % i == 0):
            return False
        i+=1
    return True

if isprime(number): 

    print("Sayınız asaldır")
else:
    print("Sayınız asal değildir")

#5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 

number = int(input("Sayı giriniz: "))

def prime_list(number):
    number_array = []
    i = 2
    while number >= 2:
        while isprime(i) and number % i == 0:
            number_array.append(i)
            number = number / i
        i+=1
    return number_array

dizi = prime_list(number)
for i in dizi : 
    print(i)