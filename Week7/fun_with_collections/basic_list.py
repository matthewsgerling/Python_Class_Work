def make_list():
    returnList = [0, 0, 0]
    temp = 1
    for i in range(0, 3, 1):
        returnList[temp].index(get_input())
        temp = temp + 1
    return returnList


def get_input():
    listVar = input('Enter a numeric variable')

    while True:
        if listVar is int:
            return listVar
        else:
            print("Not a numeric value")
            listVar = input('Enter a numeric variable')


if __name__ == '__main__':
    pass
