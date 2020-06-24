def in_dict(var):
    d = {'a', 'b', 'c', 'd', 'e'}

    if var in d:
        return True
    else:
        return False


def get_test_scores():
    score_dict = dict()
    num_scores = input('How many test Scores?')

    while int(num_scores) != 0:
        score = input('Enter the test score')
        score_dict.update({num_scores: score})
        num_scores = int(num_scores) - 1


def average_score(scores: dict):
    num_len = len(scores)
    average = int()

    while int(num_len) != 0:
        var = scores[num_len]
        average = average + var
        num_len = num_len - 1

    finalAverage = average / len(scores)
    return print('Final Average = ', finalAverage)


if __name__ == '__main__':
    test_dict = {1: 90, 2: 89, 3: 78, 4: 87}
    average_score(test_dict)
