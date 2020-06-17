def scoreInput(name, score=0, invalidmessage='Invalid test score, try again!'):
    while 0 >= int(score) >= 100:
        score = input(invalidmessage)

    return print(name, ': ', score)


if __name__ == '__main__':
    pass
