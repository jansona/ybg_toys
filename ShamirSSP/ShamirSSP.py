# -*- coding: utf-8 -*-
from __future__ import print_function
import random
import os
from fractions import Fraction


def Secret2Shadows(secret, least, total):
    vA = []
    aNum = total * (total - 1) / 2 + 10
    start = random.randint(aNum, aNum * 10)
    prime = findBiggerPrime(start)
    Shadows = []
    for i in range(1, total + 1):
        Shadows.append([])
    Shadows.append(prime)
    for i in range(0, least-1):
        vA.append(random.randint(1, least * 10))
    for s in secret:
        lTemp = []
        lTemp = Int2Shadow(int(s), least, total, vA, prime)
        for i in range(0, total):
            Shadows[i].append(lTemp[i])
    return (Shadows, prime)
    # for p in secret:
    
def Int2Shadow(piece, least, total, vA, prime):
    ShadowPiece = []
    # print(vA)
    for i in range(0, total):
        sum = piece
        for j in range(1, least):
            # print(vA[j-1])
            sum += vA[j-1] * (i + 1) ** j
            sum %= prime
        ShadowPiece.append(sum)
    return ShadowPiece

def findBiggerPrime(num):
    temp = num
    flag = True
    while(True):
        for i in range(2, temp):
            if temp % i == 0:
                flag = False
                break
        if flag:
            return temp
        temp += 1
        flag = True


def OutputShadows(ShadowsAndPrime):
    print("The prime is: " + str(ShadowsAndPrime[-1]))
    print("The form of Shadows is like this")
    print("id : shadow")
    i = 1
    for shadow in ShadowsAndPrime[0]:
        if isinstance(shadow, int):
            continue
        sTemp = str(i) + ": "
        for piece in shadow:
            sTemp += str(piece) + " "
        print(sTemp)
        i += 1

def Shadows2Secret(ids, shadows, prime):
    ans = ""
    id = ids
    for i in range(0, len(shadows[0])):
        lTemp = []
        for j in range(0, len(shadows)):
            lTemp.append(shadows[j][i])
        piece = Shadow2Int(id, lTemp, prime)
        # print(piece)
        ans += str(piece)
    return ans

def Shadow2Int(id, shadow, prime):
    sum = 0
    # numeratot = 1
    # denominator = 1
    for i in range(0, len(shadow)):
        temp = shadow[i]
        numeratot = 1
        denominator = 1
        for j in range(0, len(id)): #the length of id[] should be the same as the length of shadow[]
            if j != i:
                numeratot *= (-id[j])
                denominator *= (id[i]-id[j])
        # temp *= Fraction(numeratot, denominator)
        sum += Fraction(temp * numeratot, denominator)
    # sum = int(sum)
    return ((sum.numerator%prime)/sum.denominator)

def InputShadow(aline):
    id = ""
    shadow = []
    i = 0
    while(i < len(aline)):
        if aline[i].isdigit():
            id += str(aline[i])
            i += 1
        else:
            break
    i += 1
    noDigit = True
    temp = ""
    while(i < len(aline)):
        if aline[i].isdigit():
            temp += aline[i]
            noDigit = False
        elif noDigit:
            pass
        else:
            shadow.append(int(temp))
            temp = ""
            noDigit = True
        i += 1
    if len(temp) != 0:
        shadow.append(int(temp))
    return (int(id), shadow)
    

def Decompose():
    secret = str(input("Please tell me your secret:\t"))
    least = int(input("The least keys to rebuild the secret:\t"))
    total = int(input("How many keys you want to share(this number must be bigger than the last one):\t"))
    ShadowsAndPrime = Secret2Shadows(secret, least, total)
    OutputShadows(ShadowsAndPrime)


# print(ShadowsAndPrime[0])

# id = [5,3,1]
# # i = input()
# # while(i != 0):
# #     id.append(i)
# shadow = []
# for i in range(0, len(id)):
#     shadow.append(ShadowsAndPrime[0][id[i] - 1])
# # ans = Shadow2Int(id, shadow, ShadowsAndPrime[-1])
# # print(ans)
# print(Shadows2Secret(id, shadow, ShadowsAndPrime[-1]))
# # for i in range(0, 5):
# #     l.append([])
# # print(l)


def Rebuild():
    ids = []
    id = 0
    shadows = []
    print("Prime:", end='\t')
    prime = int(input())
    least = int(input("How many shadows you gonna input:\t"))
    for i in range(0, least):
        print("Please:", end='\t')
        try:
            aline = input()
            print(aline)
        except Exception as err:
            print(err)
            os.system('pause')
        OneShadow = InputShadow(aline)
        ids.append(OneShadow[0])
        shadows.append(OneShadow[-1])
    # try:
    ans = Shadows2Secret(ids, shadows, prime)
    # except Exception as err:
    # print(err)
    os.system('pause')
    print(str(int(float(ans))))

def ShadowsInit():
    print("Easter egg HAHAHAHAH,")
    print("WARNING DANGEROUS")
    secret = str(input("Please tell me your secret:\t"))
    least = int(input("The least keys to rebuild the secret:\t"))
    total = int(input("How many keys you want to share(this number must be bigger than the last one):\t"))
    ShadowsAndPrime = Secret2Shadows(secret, least, total)
    f = open(".\\ShadowsFile.txt", 'w')
    f.write("Prime:\t" + str(ShadowsAndPrime[-1]))
    f.write("\n")
    for i in range(1, len(ShadowsAndPrime[0])):
        shadow = str(i) + ": "
        for piece in ShadowsAndPrime[0][i - 1]:
            shadow += str(piece) + " "
        f.write(shadow)
        f.write("\n")

    f.close()


control = "d"
while(True):
    # print("我给你讲，你要是Secret分解为Shadows按 d ,")
    # print("要是Shadows重组为Secret按 r ，")
    # print("要是推出随便按吧 .")
    print("""Press 1 to decompose the secret into shadows, 
press 2 to rebuild the secret from shadows 
and press anything else if you wanna quit.""")
    try:
        control = int(input())
    except:
        print("except a digital input but got a str")
        os.system('pause')
        os.system('exit')
    if control == 1 or control == "D":
        Decompose()
    elif control == 2 or control == "R":
        Rebuild()
    elif control == 747343973:
        ShadowsInit()
    else:
        print("Fuck you")
        break

