urunler = [
    {'name':'iphone 8' ,'price':'4000' },
    {'name':'iphone 8 plus' ,'price':'5000' },
    {'name':'iphone X' ,'price':'6000' },
    {'name':'iphone XR' ,'price':'7000' },
    {'name':'iphone 11' ,'price':'8000' },
    {'name':'samsung S10' ,'price':'6000' }
]

# 1 - Tüm ürün bilgilerini listeleyiniz.
for urun in urunler:
    print(urun)

# 2 - Ürünlerin fiyatları toplamı nedir.
toplam=0
for urun in urunler:
    toplam += int(urun['price'])
print(toplam)


# 3 - ürünlerden fiyatı en fazla 6000 olan ürünleri gösteriniz.
for urun in urunler:
    if int(urun['price'])<=6000:
        print(urun)
    else:
        pass

# 4 - kullanıcıdan alınan anahtar kelimeyi içeren ürünleri bulunuz.
x = input('Ne aramıştınız:')
for urun in urunler:
    if urun['name'].find(x)>-1:
        print(urun)
    else:
        pass
        
