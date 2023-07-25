
from typing import List


def main():
    """Test selection sort with two lists."""

    nums1 = [3, 1, 4, 1, 5, 9]
    nums2 = []



def selection_sort(data: List[int], start_idx=0) -> None:
    """Sort a list using the selection sort algorithm."""

    # Base case: if there are no remaining data points to sort, return.
    if start_idx == len(data) - 1:
        return

    # Initiate tracker variables.
    lowest_val = data[start_idx]
    lowest_idx = start_idx

    # Scan each data point to find the smallest value.
    for index, value in enumerate(data[start_idx:]):
        if value < lowest_val:
            lowest_val = value
            lowest_idx = index

    # Compare first data point with lowest data point.
    if lowest_idx != start_idx:
        # Swap values if necessary.
        data[start_idx], data[lowest_idx] = data[lowest_idx], data[start_idx]

    # Sort again starting from the next position.
    selection_sort(data, start_idx + 1)


if __name__ == "__main__":
    main()
