
from typing import List


def main():
    """Test selection sort with two lists."""

    nums1 = []
    nums2 = []



def selection_sort(data: List[int], start=0) -> None:
    """Sort a list using the selection sort algorithm."""

    # Base case: if there are no remaining data points to sort, return.
    if start == len(data) - 1:
        return

    # Scan each data point to find the smallest value.
    lowest = data[start]
    for element in data[start:]:
        if element < lowest:
            lowest = i
            lowest_index =

    # Sort again starting from the next position.
    selection_sort(data, start + 1)


if __name__ == "__main__":
    main()
