def sortArray(array):
    array.sort()
    return print('Array sorted', array)


def searchArray(array, item):
    for i in range(len(array)):

        if str(array[i]) == str(item):
            return print('Item Found', i)

    return print('-1')


if __name__ == '__main__':
    pass
