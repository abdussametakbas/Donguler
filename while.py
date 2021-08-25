


# for => collection(liste)
# 1 - 100 => koşul => while

i=1

while i<=10:
    if i%2==1:
        print(f'tek sayı: {i}')
    else:
        pass    
    i+=1

username= ''
while not username:         #username'in içi boşsa false kabul eder, not diyerek false halini kabul edip, kullanıcıdan veri gelene kadar tekrarlıyosun.
    username= input('kullanıcı adınız:')
    print('kullanıcı adını girsene!!!!')
print(f'{username} hoşgeldin')    
    


