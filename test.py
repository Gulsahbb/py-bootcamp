def toplama(sayi1,sayi2):
    return sayi1 + sayi2

def cikarma(sayi1,sayi2):
    return sayi1 - sayi2

def carpma(sayi1,sayi2):
    return sayi1 * sayi2

def bolme(sayi1,sayi2):
    return sayi1 / sayi2

# sonuc = toplama(4,3)
# sonuc = cikarma(19,3)
# sonuc = carpma(7,234)
# sonuc = bolme(45,6)
# print(sonuc)

sayi1 = int(input('Lütfen 1.sayıyı Giriniz. : '))
sayi2 = int(input('Lütfen 2.sayıyı Giriniz. : '))

print('Toplam : ',toplama(sayi1,sayi2))
print('Fark : ',cikarma(sayi1,sayi2))
print('Çarpım : ',carpma(sayi1,sayi2))
print('Bölüm : ',bolme(sayi1,sayi2))

