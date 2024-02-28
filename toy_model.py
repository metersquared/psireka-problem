import numpy as np


def to_array(num: int, b=10):
    n = np.ceil(np.max(np.log(num) / np.log(b))).astype(int)
    d = np.arange(n)
    return num // b**d % b


def to_integer(array: np.ndarray, b=10):
    num = 0
    for n, digit in enumerate(array):
        num = num + digit * b**n
    return num


def approach(target: int, init: int):
    res = target - init

    if res == 0:
        return init

    x = init

    if res > 0:  # Upshift numbers
        for i in np.arange(10):
            new_x = to_integer(np.append(i, to_array(init)))
            new_res = target - new_x
            if abs(new_res) < abs(res):
                res = new_res
                x = new_x

        for i in np.arange(10):
            new_x = to_integer(np.append(to_array(init), i))
            new_res = target - new_x
            if abs(new_res) < abs(res):
                res = new_res
                x = new_x

    else:  # Downshift numbers
        for i in np.arange(10):
            new_x = to_integer(to_array(init)[0:-1])
            new_res = target - new_x
            if abs(new_res) < abs(res):
                res = new_res
                x = new_x

        for i in np.arange(10):
            new_x = to_integer(to_array(init)[1:])
            new_res = target - new_x
            if abs(new_res) < abs(res):
                res = new_res
                x = new_x

    return x


rng = np.random.default_rng(58)

candidates = 3  # Number of candidate
ideal_dist = [0.24, 0.58, 0.18]  # Number of distribution that we would ideally want
max_vote = 200  # Maximum number of votes that can be given to a candidate

votes = rng.integers(
    max_vote, size=(candidates,)
)  # Generate a randomized distribution of our candidates
total_vote = np.sum(votes)

votes_dist = votes / total_vote  # Distribution of votes
ideal_dist = np.array(ideal_dist / np.sum(ideal_dist))  # Ideal distribution of votes

ideal_num = rng.integers(200)
actual_num = rng.integers(50)

print(ideal_num)
print(actual_num)

array1 = to_array(ideal_num)
array2 = to_array(actual_num)
print(array1)
print(array2)

print(to_integer(array1))
print(to_integer(array2))

print(approach(15, 47))
