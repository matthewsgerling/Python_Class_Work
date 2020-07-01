greeting = {
    print("Hello there, Nice to meet you")
}

author = {
    print('Matthew Gerling')
}


def print_dict(var: dict):
    length = len(var)
    i = 0

    while length != 0:
        print(var[i])
        i = i + 1
        length = length - 1


def print_set(var):

    length = len(var)
    i = 0

    while length != 0:
        print(var[i])
        i = i + 1
        length = length - 1

