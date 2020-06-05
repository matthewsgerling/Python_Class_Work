def average():
    score1 = input('Please enter your first score:')
    score2 = input('Please enter your second score:')
    score3 = input('Please enter your third score:')
    return (int(score1) + int(score2) + int(score3)) / 3


if __name__ == '__main__':
    fName = input("Please Enter your first name:")
    lName = input("Please Enter your last name:")
    age = input("Please Enter your age:")
    avg = average()

    print(f'{lName}, {fName} age: {age} average grade: {avg:0.2f}')
