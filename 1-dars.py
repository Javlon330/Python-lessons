# foydalanuvchilar = ['anvar','rustam','javlon','bekzod','arslon']
# login = input('Login kiriting :')
# if login.lower() in foydalanuvchilar:
#     print('Login band , yangi login kiriting') 
# else: 
#     print('Xush kelibsiz')
# x = int(input('Butun son kiriting : '))
# for i in range(2,11):
#     if not (x%i):
#         print(f"{x} soni {i} ga qoldiqsiz bolinadi" )
# kop uchraydigan hatoliklar
# # LUG'ATLAR
# otam = { 'ismi' : 'Sabirjon','yoshi' : 57, "t_joyi" : 'Urganch tumani'}
# onam = { 'ismi' : 'Sultonposhha','yoshi' : 56, "t_joyi" : 'Urganch shahri'}
# akam = { 'ismi' : 'Yodgor','yoshi' : 31, "t_joyi" : 'Urganch tumani'}
# print(f"Otamning ismi {otam['ismi']} yoshi {otam['yoshi']} da {otam['t_joyi']}da tugilgan ")
# taomlar = {
#     'otam' : 'osh',
#     'onam' : "manti",
#     'akam' : 'lagmon'
# }
# print(f" otamning sevimli taomi {taomlar['otam']} \n onamning sevimli taomi {taomlar['onam']}")
# python_il = {
#     'int': 'butun son tipi', 
#     'float': 'onlik sonlar',
#     'for':'sikl operatori',
#     'if_else' : 'shart opertorlari',
#     'list' : "royhat",
#     'dictionary' : "lugat",
#     'len' : 'royxat uzunliki',
#     'sort' : "tartiblaydi"
#     }
# soz = input("soz kiriting : " )
# # print(python_il.get(soz,'bunday soz mavjud mas'))
# kalit = python_il.get(soz)
# if kalit == None:
#     print('bunday soz yoq')
# else :
#     print(f"{soz} {kalit} deb tarjima qilinadi")
# for k,q in sorted(python_il.items()):
#     print(f"{k} - {q}")

# countries = {
#     'Fransiya': 'Parij',
#     'Italiya' : 'Rim',
#     'Shetsiya': 'Stokgolm',
#     'Polsha': 'Varshara',
#     'Avstraliya' : 'Vena',
#     'Turkiya' : 'Anqara',
#     'Turkmaniston' : 'Ashxobod'
#     }
# print("Dunyo davlatlari")
# for d in sorted(countries.keys()):
#     print(d.upper())
# print(' \n Davlatlarning poytaxtlari')
# for p in sorted(countries.values()):
# #     print(p.title())
# davlat = input("Davlatni nomini kiriting : ")
# poytaxt = countries.get(davlat)
# if poytaxt == None:
#     print("Bunday davlat haqida ma'lumot yoq")
# else :
#     print(f"{davlat.upper()} ning poytaxti {poytaxt.title()}") 
# menu = {
#     'shashlik':15000,
#     'qatlet':24000,
#     'tabaqa': 45000,
#     'manti' : 12000,
#     'baliq' : 55000,
#     'somsa' : 7000,
#     'barak' : 17000
# }
# taom = []
# print('3 ta taom buyurtma qiling')
# for i in range(3):
#     taom.append( input(f"{i+1} taom : ").lower())
# for zakaz in taom:
#     if zakaz in menu:
#         print(f"{zakaz} {menu[zakaz]} so'm ")
#     else:
        # print(f"Kechirasiz bizda {zakaz} yo'q ")
# shoir1 = {
#     'ismi' : 'Abu Abdulloh Muhammad ibn Ismiol',
#     't_yili' : 810,
#     't_joyi' : 'Buxoro',
#     'y_yili' : 60,
#     'asarlari':{ 'al jome as sahih','al adab al mufrat','at tarix al kabir'}
# }
# shoir2 = {
#     'ismi' : 'Abdulla Qodiriy',
#     't_yili' : 1894,
#     't_joyi' : 'Toshkent',
#     'y_yili' : 44,
#     'asarlari':{ 'al jome as sahih','al adab al mufrat','at tarix al kabir'}
# }
# shoir3 = {
#     'ismi' : 'Erkin Vohidov',
#     't_yili' : 1936,
#     't_joyi' : 'Fargona',
#     'y_yili' : 80,
#     'asarlari':{ 'al jome as sahih','al adab al mufrat','at tarix al kabir'}
# }
# shoir4 = {
#     'ismi' : 'Alisher Navoiy',
#     't_yili' : 1441,
#     't_joyi' : 'Xirot',
#     'y_yili' : 60,
#     'asarlari':{ 'al jome as sahih','al adab al mufrat','at tarix al kabir'}
# }
# allomalar = [shoir1,shoir2,shoir3,shoir4]
# # for alloma in allomalar:
# #     ismi = alloma['ismi']
# #     t_yili = alloma['t_yili']
# #     t_joyi = alloma['t_joyi']
# #     y_yili = alloma['y_yili']
# #     print(f"\n {ismi} {t_yili}-yilda {t_joyi}da tavallud topgan.{y_yili} yil umir korgan   ")
# # for i in range(4):
# #     print(
# #     f"\n {allomalar[i]['ismi']} {allomalar[i]['t_yili']}-yilda {allomalar[i]['t_joyi']}da tavallud topgan.{allomalar[i]['y_yili']} yil umir korgan   ")
# for alloma in allomalar:
#     ismi = alloma['ismi']
#     print(f"\n{ismi}ning mashhur asarlari: ")
#     # asar = alloma['asarlari']
#     for asar in alloma['asarlari']:
#         print(asar)
# dostlar ={
#     'Ali' : ['Terminator','rambo','terminator'],
#     'Vali' : ['sdads','SFDAD','SDSASAJJ'],
#     'Rustam' : ['adsda','sdadas','safs']
# }
# for ism,kinolar in dostlar.items():
#     print(f"{ism}ning sevimli kinolar:")
#     for kino in kinolar:
#         print(kino)

davlatlar = {
    "O'zbekiston" : {
        'Poytaxti' : 'Toshkent',
        'Hududi' : 448978,
        'Aholisi' : 30000000,
        "Pul birligi" : "so'm"
    },
    "Rossiya" : {
        'Poytaxti' : 'Moskva',
        'Hududi' :17980746,
        'Aholisi' : 144000000,
        "Pul birligi" : "rubl"
    },
    "AQSH" : {
        'Poytaxti' : 'Vashington',
        'Hududi' : 92432423,
        'Aholisi' : 327000000,
        "Pul birligi" : "dollor"
    }
}
davlat = input("Davlat nomini kiriting :")
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(
        f" {davlat.upper()}ning poytaxti {info['Poytaxti']} "
        f"\n Hududi : {info['Hududi']} "
        f"\n Aholisi : {info['Aholisi']} "
        f"\n pul birligi : {info['Pul birligi']} "
    )





# for davlat,korsatkichlar in davlatlar.items():
#     poytaxt = korsatkichlar['Poytaxti']
#     hudud = korsatkichlar['Hududi']
#     aholisi = korsatkichlar['Aholisi']
#     pul_birligi = korsatkichlar['Pul birligi']
#     print(
#         f"   {davlat}ning poytaxti {poytaxt} \n"
#         f" Hududi  : {hudud} \n"
#         f" Aholisi : {aholisi} \n "
#         f" pul birligi : {pul_birligi} \n "
    
#     )
