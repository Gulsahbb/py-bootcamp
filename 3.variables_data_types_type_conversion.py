
isim = "Gulsah"
yas = 23
malzeme = ['Elma', 1.49, 'Muz', 1, 'Süt', 2.99, 'Peynir', 4.49]


print(isim)
print(yas)
print(malzeme)
print(type(isim))
print(type(yas))
print(type(malzeme))


print(f'3.Eleman : {malzeme[2]}')
print(f'İlk 3 Eleman : {malzeme[:3]}')
print(f'3.Eleman ve 5.Eleman arasındakiler : {malzeme[2:5]}')
print(f'5.Eleman sonrası : {malzeme[5:]}')


malzeme[3] = "Yumurta"
print(malzeme)


sayi = 15
print(sayi,type(sayi))

sayi +=3.4
print(sayi,type(sayi))

strSayi = "34"
print(strSayi,type(strSayi))

strSayi += "56"
print(strSayi)

strSayi = int(strSayi)
print(strSayi,type(strSayi))