

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
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'Exit':
        break
    qiymat = float(qiymat)
    elif qiymat<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
    

