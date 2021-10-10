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
python_il = {
    'int': 'butun son tipi', 
    'float': 'onlik sonlar',
    'for':'sikl operatori',
    'if_else' : 'shart opertorlari',
    'list' : "royhat",
    'dictionary' : "lugat",
    'len' : 'royxat uzunliki',
    'sort' : "tartiblaydi"
    }
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