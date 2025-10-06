def remove_elements(list_to_remove_elements):
    """Remove the 0th, 4th and 5th elements from the list."""
    # Si la lista tiene menos de 1 elemento, simplemente devolvemos la misma
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
    Return True if all elements in list_to_compare1 are also in list_to_compare2
    (regardless of order), and if both have the same length.
    """
    # Solo será True si tienen los mismos elementos, sin importar el orden
    return sorted(list_to_compare1) == sorted(list_to_compare2)


def list_of_lists(list_of_lists_to_modify):
    new_list = []
    for sublist in list_of_lists_to_modify:
        n = len(sublist)
        if n <= 2:
            new_list.append(sublist[:])
        elif n == 3:
            new_list.append(sublist[:-1])      # quita el último
        elif 4 <= n <= 5:
            new_list.append(sublist[1:-1])     # quita el primero y el último
        else:
            new_list.append(sublist[2:])       # quita los dos primeros
    return new_list