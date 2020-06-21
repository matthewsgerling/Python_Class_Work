def average_scores(*args, **kwargs):
    # Use *args for average calculation
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
    # return


if __name__ == '__main__':
    print(average_scores(first_name='Matt', last_name='Gerling', gpa='3.5'))
    print(average_scores(first_name='Chad', last_name='Indigo', gpa='2.0'))
    print(average_scores(first_name='Logan', last_name='North', gpa='3.9'))
