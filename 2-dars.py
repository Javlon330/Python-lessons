

# while True:
#     kitob = input('Yaxshi korgan kito kiriting :')
#     if kitob == 'stop':
#         break
#     else :
#         print(kitob)
# print("Dastur toxtadi")
# narh = 0
# while True:
#     yosh = input("Yoshingizni kiritng : ")
#     if yosh == 'exit' or yosh == "quit":
#         print("dastur tugadi")
#         break
#     yosh =int(yosh)
#     if yosh < 7 :
#         narh = 2000
#     elif yosh>7 and yosh<18 :
#         narh =3000
#     elif yosh > 18 and yosh <65:
#         narh = 10000
#     else:
#         narh = 0
#     print(f"CHipta narxi {narh} so'm")
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'Exit':
#         break
#     qiymat = float(qiymat)
#     elif qiymat < 0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
    
# buyurtmalar = []
# ishora = True
# while ishora:

#     mahsulot = input("Mahsulot nomi kiriting : ")
#     if mahsulot == 'Exit':
#         ishora = False
#     buyurtmalar.append(mahsulot)
# print("\n Quyidagi buyurtmalar qanul qilindi")
# for buyurtma in buyurtmalar:
    
#     print(buyurtma)
# e_bozor = {}
# while True:
#     marka = input("Telefon nomi : ")
#     narhi = int(input('Telefon narxi : '))
#     e_bozor[marka]=narhi
#     info = input("Yana elemt qoshishni hohlaysizmi ha/yoq : ")
#     if info == 'ha':
#         continue
#     else:
#         break
# for t,n in e_bozor.items():
#     print(f" {t} - {n} so'm ")


# for telefon in buyurtma:
#     if telefon in e_bozor.keys():
#         print(e_bozor[telefon])
#     else : 
# #         print("Bunday mahsulot yoq")
# buyurtmalar = ['iphone x','samsung A50','redmi note8','pocox3 pro','redmi magic']
# mahsulotlar = {
#     'iphone x': 12000,
#     'samsung A50' : 212333,
#     'iphone 13promax' : 13000,
#     'redmi note8' : 700,
#     'redmi magic' : 900
#     }
# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh = mahsulotlar[buyurtma]
#         print(f" {buyurtma.title()} - {narh} so'm ")
#     else:
#         print(f"Bizda bunday {buyurtma} yo'q  ")
# def yilini_hisobla(ism,yosh):
#     """ Yilini hisobla """ 
#     print(f" {ism} {2021 - yosh } yil ")
# ism = input('ismingizni kiriting : ')
# yosh = int(input('yoshingizni kiriting : '))
# yilini_hisobla(ism, yosh)
# def kv_hb(x):
#     """Kvadrat hisoblaydigan funksiya"""
#     x = x**2
#     print(x)
# kv_hb(int(input('son kiriting : ')))
# def juft_toq(x):
#     """  Sonning juft toqligini jisoblaydigan funksiya"""
#     if x%2:
#         print('Toq son')
#     else :
#         print('Juft son')

# y = float(input("Son kiriting : "))
# juft_toq(y)
# def maxx(x,y):
#     if x == y:
#         print("Sonlar teng ")
#     elif x > y:
#         print(x)
#     else :
#         print(y)
# def n_daraja(x,y):
#     n = x**y
#     print(n)

# x,y = map(float,input().split())
# n_daraja(x, y)
# def bol_alomatlari(x):
#     """ Sonlarni bolinish alomatlari """
#     for i in range(2,11):
#         if  not x % i :
#             print(f" {x} - {i} ga qoldiqsiz bolinadi  ")
# bol_alomatlari(float(input(" SOn kiriting : ")))
# def oraliq(min,max,step = 1):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min+=step
#     return sonlar
# print(oraliq(12,43))
# def mijoz_info(ism, familiya, tyil, tjoy, email="", tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {
#         "ism": ism,
#         "familiya": familiya,
#         "tyil": tyil,
#         "yoshi": 2020 - tyil,
#         "tjoy": tjoy,
#         "email": email,
#         "telefon": tel,
#     }
#     return mijoz


# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar = []
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon)) #man shu joyina tushunmadim
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob != "ha":
#         break

# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(
#         f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
#         f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}"
#     )
# def eng_katta(x,y,z):
#     """ Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya """
#     if x > y:
#         if x > z:
#             maxx = x
#         else :
#             maxx = z
#     elif y > z:
#         maxx = y
#     else :
#         maxx = z
#     return maxx
# # def kattasi(x, y, z):
# #     max = x
# #     if y >= max:
# #         max = y
# #     if z >= max:
# #         max = z
# #     return max

# print(eng_katta(12, 24, 1343))
def aylana(r):
    """Aylana radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya"""
    pi = 3.14
    doira = {
        'Radius' : r,
        'Diametr' : 2*r,
        'Perimatr' : 2*pi*r,
        'Yuzi' : pi*r*r
    }
    return doira
print(aylana(float(input("Radiusni kiriting : "))))
