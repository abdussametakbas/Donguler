isim='Samet Akbaş'

for harf in isim:
    if harf=='m':     #continue o an geleni es geçip devam eder.
        continue
    print(harf)

for harf in isim:
    if harf=='m':     # m yi gördüğü an bırakır onu da  yazmaz
        break
    print(harf)    



# soru = 1-100 arası çift sayıların toplamı?
toplam=0
i=0
while i<=100:
    i+=1
    if i%2==1:
        continue
    toplam+=i
print(toplam)

