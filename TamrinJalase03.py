# 001
# vazn = int(input("vazn ra vared knid : "))
vazn = 80
# sallHa = int(input("tedad sal ha ra vared knid"))
sallHa = 15
while sallHa >= 0 :
    vazn_mah = vazn * 0.165
    print(vazn,"-->",vazn_mah)
    vazn = vazn + 1 
    sallHa = sallHa - 1
# 001
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
# 002
# name = str(input("eman a retne : "))
name = "emad"
name2 = list(name)
name3 = []
# # 002.5
# i = 1
# for item in name2 :
#     name3.append(name2[-i])
#     i += 1
# name3 = "".join(name3)
# print(name3)
# # 002.5
name = name2[::-1]
name = "".join(name)
print(name)
# 002
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
# 003
number = int(input("enter a number (braie mohasebeie miangin): "))
# miangin = number/2
# print(miangin)
miangine = 0
madeList = [0]
j = 1
while number > 0 :
    madeList.append(j)
    j += 1 
    number = number - 1
for item in madeList:
    miangine = miangine + item
miangine = miangine/(len(madeList))
print(madeList,miangine)
# 003
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
# 004
factoriel = int(input("adade khod ra vared knid (jahate mohasebeie factorial)"))
facktoeNum = factoriel
while factoriel > 1 :
    facktoeNum = facktoeNum * (factoriel-1)
    factoriel = factoriel - 1
    print(facktoeNum)
# 004
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
# 005
lista = []
listae = []
#string = str(input("reshteie khod ra vared knid"))
string = "days2hours24"
for char in string :
    #.isalpha برای تشخیص حروف یا الفابت است
    if char.isalpha():
        lista.append(char)
    #.isdigit برای تشخیص اعداد است
    elif char.isdigit():
        listae.append(char)
print("horof -> ",lista,"adud -> ",listae)
# 005
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
# 006
numberi = 0
numbero = 0
number = int(input("adade khod ra vared knid ( adade fard ghabl * mazarebe 5 ghabl ): "))
orgNumber = number
if number % 2 == 0 :
    number = number - 1
while number > 0 :
    numberi = numberi + number
    number = number - 2
j = (orgNumber//5)
while j > 0 :
    numbero = numbero + (5*j)
    j = j - 1
print(numberi * numbero)
# 006
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
# # 007
# print("(jahate zarb hame dar ham)")
# x1 = int(input("adade 1 ra vared knid : "))
# x2 = int(input("adade 2 ra vared knid : "))
# x3 = int(input("adade 3 ra vared knid : "))
# x4 = int(input("adade 4 ra vared knid : "))
# x5 = int(input("adade 5 ra vared knid : "))
# x6 = int(input("adade 6 ra vared knid : "))
# x7 = int(input("adade 7 ra vared knid : "))
# x8 = int(input("adade 8 ra vared knid : "))
# x9 = int(input("adade 9 ra vared knid : "))
# x10 = int(input("adade 10 ra vared knid : "))
# print(x1*x2*x3*x4*x5*x6*x7*x8*x9*x10)
# # 007
print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
# 007.5
listi = []
# lenn = int(input("che tedad adad morede nazar hast ? : "))
lenn = 10
i = 1
vorodi = 1
print("(jahate zarb hame dar ham)")
while lenn != 0 :
    vorod = int(input("adade khod ra vared knid : "))
    listi.append(vorod)
    vorodi = vorodi *vorod
    lenn = lenn - 1
    i += 1
print(vorodi)
# 007.5