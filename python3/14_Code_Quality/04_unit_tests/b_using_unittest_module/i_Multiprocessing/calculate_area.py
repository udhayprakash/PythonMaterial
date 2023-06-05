import multiprocessing
from typing import List


def calculate_area(length: int, width: int) -> int:
    return length * width


def calculate_area_parallel(lengths: List[int], widths: List[int]):
    if len(lengths) != len(widths):
        raise ValueError("Give Equal numbe of values for both lengths & widths")

    with multiprocessing.Pool(processes=2) as pool:
        areas = pool.starmap(calculate_area, zip(lengths, widths))
    return areas


if __name__ == "__main__":
    res = calculate_area_parallel([1, 2, 3], [4, 5, 6])
    print(res)

    try:
        res = calculate_area_parallel([1, 2, 3], [4, 5])
    except ValueError as ex:
        print(ex)
