def len_int_first(_line): #посчитать длину первого числа
    k = 0
    _max = 0
    _line = _line + "*"
    for i in range(len(_line)):
        if _line[i].isdigit():
            k += 1
        else:
            if k > _max:
                _max = k
                return _max
            k = 0


def len_int_max(_line): #посчитать длину максимального числа
    k = 0
    _max = 0
    _line = _line + "*"
    for i in range(len(_line)):
        if _line[i].isdigit():
            k += 1
        else:
            if k > _max:
                _max = k
            k = 0
    return _max

_line = ""
_line = input("Введите строку / Enter the line: ")

print("[0] - Посчитать длину первого найденного числа / Calculate the length of the first found number")
print("[1] - Вывести длину самого длинного числа / Print the length of the longest number")
x = int(input("Введите пункт / select an item: "))
if x == 0:
    print(len_int_first(_line))
else:
    print(len_int_max(_line))
    
input()