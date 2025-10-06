def remove_elements(list_to_remove_elements):
    """Remove the 0th, 4th and 5th elements from the list."""
    if len(list_to_remove_elements) == 0:
        return []

    new_list = [list_to_remove_elements[i] for i in range(len(list_to_remove_elements))
                if i not in (0, 4, 5)]
    return new_list


def add_elements(list_to_add_elements):
    """Add 'Pink' at the start and 'Yellow' at the end."""
    new_list = ["Pink"] + list_to_add_elements + ["Yellow"]
    return new_list


def is_empty(list_to_check):
    """Return True if the list is empty, otherwise False."""
    return len(list_to_check) == 0


def check_lists(list_to_compare1, list_to_compare2):
    """
    Return True if all elements in list_to_compare1 are also in list_to_compare2
    (regardless of order), and if both have the same length.
    """
    return sorted(list_to_compare1) == sorted(list_to_compare2)


def list_of_lists(list_of_lists_to_modify):
    """Modify each inner list based on its length."""
    new_outer_list = []
    for inner in list_of_lists_to_modify:
        n = len(inner)
        if n >= 5:
            new_outer_list.append(inner[1:-1])
        elif n >= 3:
            new_outer_list.append(inner[1:])
        else:
            new_outer_list.append(inner[:])
    return new_outer_list
