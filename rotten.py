armen_results = [
    +3, -2, -3, +3, +1, -3, +3, -2, +3, -3,
    +3, +3, +2, +0, +1, +3, +2, -2, +3, +0,
    -3, +0, -3, -3, -3, -3, -2, +2, +3, -3,
    +3, +2, -3, +3, +0, +3, +2, -1, +3, +2,
    +3, +2, 0, +2
]

ranges = {
    "io": [
        [-132, -13, 1], [-13, -2, 2], [-2, 10, 3], [10, 22, 4], [22, 33, 5], [33, 45, 6], [45, 57, 7], [57, 69, 8],
        [69, 80, 9], [80, 132, 10]
    ],
    "in": [
        [-36, -7, 1], [-7, -3, 2], [-3, 1, 3], [1, 5, 4], [5, 8, 5], [8, 12, 6], [12, 16, 7], [16, 20, 8],
        [20, 24, 9], [24, 36, 10]
    ],
    "id": [
        [-36, -10, 1], [-10, -6, 2], [-6, -2, 3], [-2, 2, 4], [2, 6, 5], [6, 10, 6], [10, 15, 7], [15, 19, 8],
        [19, 23, 9], [23, 36, 10]
    ],
    "ip": [
        [-30, -11, 1], [-11, -7, 2], [-7, -4, 3], [-4, 0, 4], [0, 4, 5], [4, 7, 6], [7, 11, 7], [11, 14, 8],
        [14, 18, 9], [18, 30, 10]
    ],
    "is": [
        [-30, -4, 1],
        [-4, 0, 2],
        [0, 4, 3],
        [4, 8, 4],
        [8, 12, 5],
        [12, 16, 6],
        [16, 20, 7],
        [20, 24, 8],
        [24, 28, 9],
        [28, 30, 10]
    ],
    "im": [
        [-12, -6, 1],
        [-6, -4, 2],
        [-4, -2, 3],
        [-2, 0, 4],
        [0, 2, 5],
        [2, 5, 6],
        [5, 7, 7],
        [7, 9, 8],
        [9, 11, 9],
        [11, 12, 10]
    ],
    "iz": [
        [-12, -3, 1],
        [-3, -1, 2],
        [-1, 1, 3],
        [1, 3, 4],
        [3, 4, 5],
        [4, 5, 6],
        [5, 7, 7],
        [7, 9, 8],
        [9, 11, 9],
        [11, 12, 10]
    ]
}

pluses = {
    "io": [2, 4, 11, 12, 13, 15, 16, 17, 19, 20, 22, 25, 27, 29, 31, 32, 34, 36, 37, 39, 42, 44],
    "id": [12, 15, 27, 32, 36, 37],
    "in": [2, 4, 20, 31, 42, 44],
    "is": [2, 16, 20, 32, 37],
    "ip": [19, 22, 25, 31, 42],
    "im": [4, 27],
    "iz": [13, 34]
}

minuses = {
    "io": [1, 3, 5, 6, 7, 8, 9, 10, 14, 18, 21, 23, 24, 26, 28, 30, 33, 35, 38, 40, 41, 43],
    "id": [1, 5, 6, 14, 26, 43],
    "in": [7, 24, 33, 36, 40, 41],
    "is": [7, 14, 26, 28, 41],
    "ip": [1, 9, 10, 24, 30],
    "im": [6, 38],
    "iz": [3, 23]
}


def collect_answers():
    results = []
    index = 1

    with open('questions.txt', 'r') as file:
        questions = file.read().split("\n")

    for question in questions:
        print("{}/{} {}".format(index, len(questions), question))
        answer = input()

        try:
            answer = int(answer)
        except ValueError:
            answer = 0

        while answer < -3 or answer > 3:
            print("\t [X] Только от -3 до 3 включительно")
            answer = int(input())

        results.append(answer)
        index += 1

    return results


def calc_sten(score, range):
    for val in range:
        if val[0] <= score < val[1]:
            return val[2]


def calc_scale(plus, minus, results):
    buf = 0

    k = 1
    for answer in results:
        if k in plus:
            buf += answer

        if k in minus:
            buf += -answer

        k += 1
    return buf


user_results = collect_answers()
print("Collecting...\n")

for stage in ["io", "id", "in", "is", "ip", "im", "iz"]:
    score = calc_scale(pluses[stage], minuses[stage], user_results)
    sten = calc_sten(score, ranges[stage])

    print("{} stage, score = {}, sten = {}".format(stage, score, sten))
