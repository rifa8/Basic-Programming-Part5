def pair_sum(arr, target):
    el_kiri, el_kanan = 0, len(arr) - 1    
    while el_kiri < el_kanan:
        hasil = arr[el_kiri] + arr[el_kanan]
        if hasil == target:
            return [el_kiri, el_kanan]
        if hasil < target:
            el_kiri += 1
        else:
            el_kanan -= 1
    return None

if __name__ == '__main__':
    print(pair_sum([1, 2, 3, 4, 6], 6)) # [1, 3]
    print(pair_sum([2, 5, 9, 11], 11)) # [0, 2]
    print(pair_sum([1, 3, 5, 7], 12)) # [2, 3]
    print(pair_sum([1, 4, 6, 8], 10)) # [1, 2]
    print(pair_sum([1, 5, 6, 7], 6)) # [0, 1]
