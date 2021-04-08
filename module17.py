while True:
    try:
        a = list(map(int, input('введите последовательность чисел через пробел:').split()))
        if a != list(map(int, input().split())):
            break
        else:
            raise ValueError
    except ValueError:
        print('Не выполнено условие ввода')
    pass
for i in range(len(a)):
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        x = array[: middle]
        for i in x:
            if i == element:
                x.remove(element)
        index_left = (len(x) - 1)
        y = array[middle:]
        for n in y:
            if n <= element and len(y) > 1:
                y.remove(n)
        f = y[0]
        index_right = array.index(f)
        if index_left < 0:
            print('Это первый элемент списка. Индекс большего числа справа =', index_right)
        elif index_right == len(array) - 1:
            print(f'Индекс меньшего числа слева = {index_left}. Это последний элемент списка')
        else:
            print(f'Индекс меньшего числа слева = {index_left}. Индекс большего числа справа = {index_right}')
        return index_left, index_right
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)
print(a)