def writeToFile(info):
    try:
        f = open('student_info', 'w')
        f.writelines(info)
        f.close()
    finally:
        return print('File wrote')


def getStudentInfo(sName):
    goAgain = True
    score: str
    finalScores: tuple

    inputName = input("Please enter the students name.")

    if sName == inputName:
        while goAgain is True:
            score = input("Enter a test Score")
            finalScores = (score, " ")
            goAgain = input('Would you like to enter more? y/n')
            if goAgain is 'y':
                goAgain = True
            else:
                goAgain = False
                writeToFile(finalScores)


def readFile():
    f = open('student_info', 'r')
    print(f.read())


if __name__ == '__main__':
    getStudentInfo('Matt')
    readFile()
    print('press any key to end')
