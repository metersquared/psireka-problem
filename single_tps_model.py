import numpy as np

# The case where everyone votes in a single voting booth.


def to_array(num: int, b=10):
    """Convert number to array of digits.

    Parameters
    ----------
    num : int
        Number
    b : int, optional
        Base, by default 10

    Returns
    -------
    ndarray
        Array of digits
    """
    n = np.ceil(np.max(np.log(num) / np.log(b))).astype(int)
    d = np.arange(n)
    return num // b**d % b


def to_integer(array: np.ndarray, b=10):
    """Convert array of digits to number.

    Parameters
    ----------
    array : np.ndarray
        Array of digits.
    b : int, optional
        Base, by default 10

    Returns
    -------
    int
        Number
    """
    num = 0
    for n, digit in enumerate(array):
        num = num + digit * b**n
    return num


def optimize(target: int, init: int):
    """Approach a target number with only a single digit append or prepend.

    Parameters
    ----------
    target : int
        Target number
    init : int
        Initial number

    Returns
    -------
    int
        Optimal number
    """

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
max_vote = 10000  # Maximum number of votes that can be given to a candidate

votes = rng.integers(
    max_vote, size=(candidates,)
)  # Generate a randomized distribution of our candidates
total_vote = np.sum(votes)

votes_dist = votes / total_vote  # Distribution of votes
ideal_dist = np.array(ideal_dist / np.sum(ideal_dist))  # Ideal distribution of votes
ideal_votes = np.rint(ideal_dist * total_vote)

manipulated_votes = np.zeros(candidates)

for idx, vote in enumerate(votes):
    manipulated_votes[idx] = optimize(
        ideal_votes[idx], vote
    )  # Find optimal number closest to target

print("Actual vote :", votes)
print("Ideal vote :", ideal_votes)
print("Manipulated vote :", manipulated_votes)

print("Actual vote distribution :", votes_dist)
print("Ideal vote distribution :", ideal_dist)
print("Manipulated vote distribution :", manipulated_votes / sum(manipulated_votes))

# Result is poor ==> Choice of target matters!
