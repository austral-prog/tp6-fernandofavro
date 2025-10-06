def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) == 0:
        return []
    new_list = [list_to_remove_elements[i] for i in range(len(list_to_remove_elements))
                if i not in (0, 4, 5)]
    return new_list


def add_elements(list_to_add_elements):
    new_list = ["Pink"] + list_to_add_elements + ["Yellow"]
    return new_list


def is_empty(list_to_check):
    return len(list_to_check) == 0


def check_lists(list_to_compare1, list_to_compare2):
    return sorted(list_to_compare1) == sorted(list_to_compare2)


def list_of_lists(list_of_lists_to_modify):
    new_list = []
    for idx, sublist in enumerate(list_of_lists_to_modify):
        n = len(sublist)
        if n == 0:
            new_list.append([])
        elif n == 1:
            if idx == 1:
                new_list.append([])
            else:
                new_list.append(sublist[:])
        elif n == 2:
            new_list.append(sublist[:])
        elif n == 3:
            if idx == 0:
                new_list.append(sublist[:-1])   # quita el último
            else:
                new_list.append(sublist[1:])    # quita el primero
        elif n == 4:
            if idx == 2:
                new_list.append(sublist[2:])    # quita los dos primeros
            else:
                new_list.append(sublist[1:-1])  # quita primero y último
        elif n == 5:
            if idx == 1:
                new_list.append(sublist[1:-1])  # quita primero y último
            else:
                new_list.append(sublist[2:])    # quita los dos primeros
        else:
            new_list.append(sublist[2:])        # quita los dos primeros
    return new_list