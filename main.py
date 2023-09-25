from random import randint
def HeadHands1() -> list:

    '''Данная функия предназначена для создания и обработки массивов,
    при выполнении функции необходимо будет указать:
    n - желаемое количество генерируемых массивов.
    size - максимально возможное значение длины генерируемых массивов.
    number - максимально возможное значение элементов в массивах.'''

    print('Сейчас Вы введете значения, они должны быть натуральными числами.')
    while True:
        try:
            n = int(input('Введите количество массивов: '))
            size = int(input('Введите длину массивов (не может быть меньше количества массивов): '))
            if size <= n:
                raise 'TypeError'
            number = int(input('Введите максимально значение числа в массиве: '))
            break
        except Exception:
            print('Ошибка ввода. Введите значения заново.')

    list_lens = []                               # массив для хранения размеров списков
    result = []                                  # массив для заполнения готового результата

    for i in range(n):                           # заполнение массива размеров
        while True:
            lens = randint(1, size)
            if lens not in list_lens:
                list_lens.append(lens)
                break
            else:
                continue

    for size_massive in list_lens:               # заполнение массива списками
        sp = []
        step = 0
        while step != size_massive:
            sp.append(randint(0, number))
            step += 1
        result.append(sp)

    for i in result[1::2]:                       # сортировка четных элементов списка
        i.sort()

    for i in result[::2]:                        # сортировка не четных элементов списка
        i.sort(reverse= True)

    return result

print(HeadHands1())
