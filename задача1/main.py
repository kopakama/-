# проверить, совпадает ли вторая структура по вложеноости и длинне вложенных массивов с первой
def same_structure_as(original, other):
    # если вложенность 0, следовательно обе структуры равны
    if type(original) in (str, int) and type(other) in (str, int):
        return True

    # если типы структур разные, то они не равны
    elif type(original) != type(other):
        return False

    # если длины массивов, что снаружи разные, то то они не равны
    elif len(original) != len(other):
        return False
    for ori, oth in zip(original, other):  # сравниваем каждый элемент
        # если типы элементов не равны, то массивы разные
        if (type(ori) != type(oth)) and (type(ori) != str and type(oth) != str):
            return False
        # сравниваем элементы, независимо от позиций
        elif type(ori) == type(oth) and isinstance(ori, list):
            if not same_structure_as(ori, oth) or len(ori) != len(oth):
                return False
    return True


print(same_structure_as([1,'[',']'],['[',']',1]))
print(same_structure_as([1, [1, 1]], [[2, 2], 2]))
print(same_structure_as([12, 13, 14], [2, 2, 2]))
print(same_structure_as([], {}))
print(same_structure_as([1, 2], [2, 1]))
