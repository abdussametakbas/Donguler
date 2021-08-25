# kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız
#   ürün sayısını kullanıcıya sorun
#   dictionary listesi yapısı (urunAdi, fiyat) şeklinde olsun
#   ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin
urunler=[]
i=1
iSon=int(input('Kaç tane ürün eklemek istersiniz: '))

while i<=iSon:
    urunAdi=input(f'{i}. ürünün ismini giriniz: ')
    fiyat= input(f'{i}. ürünün fiyatını giriniz: ')
    urunler.append({
        'urunAdi':urunAdi,
        'fiyat':fiyat
    })
    i+=1
sayac=0
while sayac<iSon:
    print(urunler[sayac])
    sayac+=1     



