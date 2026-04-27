"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    ascending = True  # Default order is ascending

    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        order_param = sys.argv[3].lower()
        if order_param == "asc":
            ascending = True
        elif order_param == "desc":
            ascending = False
        else:
            print("The third argument must be 'asc' for ascending or 'desc' for descending order.")
            sys.exit(1)
    else:
        print("You must specify the file as the first argument.")
        print("The second argument indicates if you want to remove duplicates (yes/no).")
        print("The third argument indicates the order: 'asc' or 'desc'.")
        sys.exit(1)

    print(f"Reading words from file {filename}.")
    file_path = os.path.join(".", filename)

    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"The file {filename} does not exist.")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print("Sorted list:")
    print(sort_list(word_list, ascending=ascending))