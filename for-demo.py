sayilar = [1,5,15,35,57,72,2,18]

# 1 - sayılar listesindeki her bir elemanı yazdırın.
for i in sayilar:
    print(i)

# 2 - sayılar listesindeki hangi sayılar 5'in katıdır?
for i in sayilar:
    if i % 5 ==0:
        print(i)
    else:
        pass    

# 3 - sayılar listesinde sayıların toplamı kaçtır ?
toplam=0
for i in sayilar:
    toplam +=i

print(toplam)    

# 4 - sayılar listesindeki çift sayıların karesini alınız.
for i in sayilar:
    if i%2==0:
        print(f"{i}'nin karesi : {i**2}")
    else:
        pass    


urunler = ['iphone 8','iphone X','iphone XR','samsung S10']

# 5 - urunler listesindeki tüm ürünlerin 2. karakterlerini ekrana yazdırın.
for i in urunler:
    print(i[1])

# 6 - urunler listesi içinde iphone geçen kaç ürün vardır? (index(bulunca 0 değeri verir, bulamayıca hata),
                                                           #find(bulunca 0-bulamayınca -1 değeri verir) )
toplamSayi=0
for i in urunler:
    if i.find('iphone')>-1:
        toplamSayi +=1
    else:
        pass     
print(toplamSayi)
