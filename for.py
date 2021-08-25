sayilar=[1,2,3,6,8,9]
for i in sayilar:
    print(i)

for i in sayilar:
    print("Merhaba")    


isimler= ["Ali","Deniz", "Ahmet"]
for isim in isimler:
    print(isim)


isim="Samet"
for a in isim:
    print(1)


_tuple= [(1,2),(3,4),(8,9)]
for a,b in _tuple:
    print(a,b)


_dict={"k1":1,"k2":2,"k3":3}
for x in _dict:
    print(x)           #sadece key bilgisini alır.

for x in _dict:
    print(_dict[x])   #value bilgisini alır

for x in _dict.values():     #daha kullanışlı value bilgisini alır.
    print(x) 

print(111111)
for x in _dict.items(): #Key ve Value bilgisini parantez içinde alır
    print(x)    

for key,value in _dict.items():
    print(key,value)            #parantezsiz key value bilgisini verir
