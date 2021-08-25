sayilar = [4,6,9,10,35,57,89,125,244]

# 1 - sayilar listesini while ile ekrana yazdırın.
i=0
while i<len(sayilar):
    print(sayilar[i])
    i +=1


# 2 - Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki 
# tüm tek sayıları ekrana yazdırın.
ilkSayi=int(input('İlk sayınızı giriniz:'))
sonSayı= int(input('Son sayınızı giriniz:'))
sıra=0
while ilkSayi<=sonSayı:
    
    if ilkSayi %2==1:
        sıra+=1
        print(f'{sıra}. tek sayı : {ilkSayi} ')
    else:
        pass
    ilkSayi+=1    

# 3 - 1-100 arasındaki sayıları azalan şekilde yazdırın.
i=100
while i>=1:
    print(i)
    i-=1


# 4 - kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
sayi1= int(input('sayi 1 :'))
sayi2= int(input('sayi 2 :'))
sayi3= int(input('sayi 3 :'))
sayi4= int(input('sayi 4 :'))
sayi5= int(input('sayi 5 :'))
_liste=[sayi1,sayi2,sayi3,sayi4,sayi5]
_liste.sort()
i=0
while i<len(_liste):
    print(_liste[i])
    i+=1
