#Giriş
print()                         # satır sonu karakterinden oluşan boş satır.   
print("Merhaba")                # ekrana yazdır.
print("T","Ç","Ç","Böl","M","Üs")
print(2 + 3, 2 * 3, 2 - 2, 5 / 1, 20 % 7, 5 ** 3)
print(5.5 * 2)
print(5.5 * 2.5)
print(5,5 * 2,5)                # sonuçLAR?
print(22 / 7)
sonuc = 22/7 ; print(sonuc)  
sonuc = int(sonuc) ; print(sonuc)
print(type(sonuc))              # sonuç değişkeninin tipini yaz.
ad="şenol" ; print("Merhaba", ad)
print(type(ad))                 # ad değişkeninin tipini yaz
print({'pardus', ad, 'Pardus', sonuc,'pardus'})
print(sonuc + 2)
sonuc += 5 ; print(sonuc) ; sonuc -= sonuc ; print(sonuc)
print(ad, ad == 'şenol')  ; print(ad, ad == 'senol')
print(sonuc, sonuc >= sonuc <= sonuc + 1 )   
soy = "ALD" ; Ad = "Senol" ; adsoy = Ad + " " + soy ; print(adsoy, ad)  # case-sensitive (ad, Ad)
print(adsoy * 3) ; print(adsoy[0] + adsoy[1:3] + " " * 10 + "A" * 5 )   # ş en " " AAAAA
print(ad[:3], ad[-1],ad[-3], ad[:-2], ad[::-1])
x, y = 500, 300 ; x, y = y, x ; print(x, y); x = y = z = ad[:3] ; print(x, y, z)
print(); print('\n') ; print('')      # satır sonu karakterinden oluşan boş satır; 1 char ; zero       
dizi = ["pardus", "debian", "ubuntu", "redhat"] ; print(" / ". join(dizi))
# 1ad = "senol" ; 4 = "Snl" ; is="senol" ; not = 60 ; vize-notu = 55   # Illegal variable names:
import os ; print(os)
#print('Merhaba, ' + os.getlogin())





