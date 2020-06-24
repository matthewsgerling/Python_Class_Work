def switch_average(var: str):
    scores: dict = {'a': 90, 'b': 80, 'c': 70, 'd': 60}

    if scores['a']:
        return print("Score is 90")
    elif scores['b']:
        return print("Score is 80")
    elif scores['c']:
        return print("Score is 70")
    elif scores['d']:
        return print("Score is 60")
    else:
        return print('Key not Valid')


if __name__ == '__main__':
    switch_average('d')
