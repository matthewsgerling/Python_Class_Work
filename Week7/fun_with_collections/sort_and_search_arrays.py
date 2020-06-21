def sortArray(array):
    array.sort()
    return print('Array sorted', array)


def searchArray(array, item):
    if item in array:
        return print('Item Found')
    else:
        return print('-1')


if __name__ == '__main__':
    pass
