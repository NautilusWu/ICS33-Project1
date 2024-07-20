"""
SCI 33 Project 1
Part2: comprehension
"""


def question1(n: dict) -> dict:
    """
    Given a dictionary n where the values are unique, create a new dictionary
    where the keys become values and the values become keys.
    :param n: dict where the values are unique
    :return: dict where the key and values are exchanged
    """
    result = {v: k for k, v in n.items()}
    return result

def question2(n: dict) -> dict:
    """
    Given a dictionary n, create a new dictionary where each value from the
    original dictionary becomes a key in the new dictionary and its value
    is a list of keys from the original dictionary that had the same value.
    :param n: dict original dictionary
    :return: dict new dictionary with list of keys
    """
    result = {v: [key for key, val in n.items() if val == v] for v in n.values()}
    return result
def question3(m: dict, n: dict) -> dict:
    """
    Given two dictionaries m and n, merge them into a new dictionary. Where
    keys in m and n that match, sum their values, assuming all values are
    numeric.
    :param m: dict first dictionary
    :param n: dict second dictionary
    :return: dict new dictionary with merged values
    """
    result = {k: m.get(k, 0) + n.get(k, 0) for k in m.keys() | n.keys()}
    return result


def question4(n: list) -> list:
    """
    Create a list of integers from a nested list structure that appear more
    than once any where in the entire structure.
    :param n: nested list structure
    :return: list of integers that appear more than once
    """
    result = [
        x
        for x in {item for sublist in n for item in sublist}
        if [item for sublist in n for item in sublist].count(x) > 1
    ]
    return result


def main() -> None:
    """
    Main function
    :return: None
    """
    n = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}
    print(question1(n))
    n = {"A": 1, "B": 1, "C": 1, "D": 5, "E": 5, "F": 6}
    print(question2(n))
    m = {"A": 1, "B": 1, "C": 1, "D": 3, "F": 1}
    n = {"A": 3, "B": 1, "D": 4, "E": 5, "F": 6}
    print(question3(m, n))
    n = [[1, 2], [3, 2], [1, 5, 3], [6, 5]]
    print(question4(n))


if __name__ == "__main__":
    main()
