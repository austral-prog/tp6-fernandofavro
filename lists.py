def remove_elements(list_to_remove_elements):
    """Remove the 0th, 4th and 5th elements from the list."""
    if len(list_to_remove_elements) == 0:
        return []
    # Creamos una nueva lista excluyendo las posiciones 0, 4 y 5
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
    Return True if both lists contain the same elements (regardless of order).
    """
    return sorted(list_to_compare1) == sorted(list_to_compare2)


def list_of_lists(list_of_lists_to_modify):
    """Modify each inner list based on its length following specific rules."""
    new_list = []
    for sublist in list_of_lists_to_modify:
        n = len(sublist)
        if n == 0:
            new_list.append([])
        elif n == 1:
            new_list.append([])             # elimina el único elemento
        elif n == 2:
            new_list.append(sublist[:])     # deja igual
        elif n == 3:
            new_list.append(sublist[:-1])   # quita el último
        elif 4 <= n <= 5:
            new_list.append(sublist[1:-1])  # quita el primero y el último
        else:
            new_list.append(sublist[2:])    # quita los dos primeros
    return new_list