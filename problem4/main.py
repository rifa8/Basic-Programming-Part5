def muncul_sekali(angka):
    unique_el = []
    jumlah = {}
    for el in angka:
        if el in jumlah:
            jumlah[el] += 1
        else:
            jumlah[el] = 1
    for el, count in jumlah.items():
        if count == 1:
            unique_el.append(el)
    return [int(el) for el in unique_el]

if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]
