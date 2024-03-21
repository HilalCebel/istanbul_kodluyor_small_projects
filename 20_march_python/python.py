#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

boy = float(input("Boyunuzu giriniz (x.xx): "))
kilo = float(input("Kilonuzu giriniz: "))
sonuc = kilo / (boy*boy)
print("Vücut kitle endeksiniz: " + str(sonuc))


#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

maas = float(input("Maaşınızı giriniz : "))
zamOrani = float(input("Zam oranını(%) giriniz : "))

yeniMaas = maas + (maas * zamOrani/100)
print("Zamlı maaş: " + str(yeniMaas))

#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

sayi1=int(input("birinci sayiyi giriniz"))
sayi2=int(input("ikinci sayiyi giriniz"))
sayi3=int(input("üçüncü sayiyi giriniz"))
if(sayi1>sayi2 and (sayi1>sayi3)):
   print("en büyük sayi =sayi1")
elif(sayi2>sayi1 and (sayi2>sayi3)):
  print("en büyük sayi = sayi2")
else :
 print("en büyük sayi =sayi3")


#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

yariCap=float(input("yaricap"))

pi=3.14

cevre=2*pi*yariCap
alan=pi*(yariCap*yariCap)

print("dairenin alanı="+str(alan))
print("dairenin cevresi="+str(cevre))


#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

number = input("Bir sayı giriniz : " )
reverse = number[::-1]
if number == reverse:
    print("Sayınız palindromdur")
else:
    print("Sayınız palindrom değildir")
