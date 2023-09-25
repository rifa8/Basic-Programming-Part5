def remove_duplicates(array):
    non_duplikat = 1
    for i in range(1, len(array)):
        if array[i] != array[non_duplikat - 1]:
            array[non_duplikat] = array[i]
            non_duplikat += 1
    return non_duplikat

if __name__ == '__main__':
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) # 4
    print(remove_duplicates([2, 3, 4, 5, 6, 9, 9])) # 6
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([1, 2, 3, 11, 11])) # 4
