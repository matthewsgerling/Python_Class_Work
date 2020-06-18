def measurements(a_list):
    if len(a_list) is 2:
        x = a_list[0]
        y = a_list[1]
    else:
        x = a_list[0]
        y = x

    print('Area is ', area(x, y))
    print('perimeter is ', perimeter(x, y))


def area(x, y):
    return x * y


def perimeter(x, y):
    return x + x + y + y


if __name__ == '__main__':
    pass
