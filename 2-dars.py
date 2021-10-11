

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
    
buyurtmalar = []
ishora = True
while ishora:

    mahsulot = input("Mahsulot nomi kiriting : ")
    if mahsulot == 'Exit':
        ishora = False
    buyurtmalar.append(mahsulot)
print("\n Quyidagi buyurtmalar qanul qilindi")
for buyurtma in buyurtmalar:
    
    print(buyurtma)