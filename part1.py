"""
SCI 33 Project 1
Part1: file reading and data types
"""


def read_calls(file: open) -> {(str, str): int}:
    """
    Reads calls from file, returns a dict of {(caller, callee): count}
    :param file: open file object
    :return: dict of {(caller, callee): count}
    """
    result = {}
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            tup_lst = line.strip("\n").split(":")
            tup_lst = [i.strip() for i in tup_lst]
            for i in range(1, len(tup_lst)):
                if (tup_lst[0], tup_lst[i]) in result:
                    result[(tup_lst[0], tup_lst[i])] += 1
                else:
                    result[(tup_lst[0], tup_lst[i])] = 1
    return result


def call1to2(calls: {(str, str): int}) -> {str: {str: int}}:
    """
    :param calls: dict of {(caller, callee): count}
    :return: dict of {caller: {callee: count}}
    """
    result = {}
    for key, value in calls.items():
        if key[0] in result:
            if key[1] in result[key[0]]:
                result[key[0]][key[1]] += value
            else:
                result[key[0]][key[1]] = value
        else:
            result[key[0]] = {key[1]: value}
    return result


def main() -> None:
    """
    Main function
    :return: None
    """
    file_name = "calls.txt"

    r_01 = read_calls(file_name)
    print(r_01)
    r_02 = call1to2(r_01)
    print(r_02)


if __name__ == "__main__":
    main()
