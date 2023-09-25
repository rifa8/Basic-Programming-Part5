def compare(a, b):
    listA = []
    listB = []
    listC = []
    for i in range(len(a)):
        listA.append(a[i])
    for j in range(len(b)):
        listB.append(b[j])
    if len(listA) < len(listB):
        for el in listA:
            if el in listB:
                listC.append(el)
    else:
        for el in listB:
            if el in listA:
                listC.append(el)
    return "".join(listC)

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA
