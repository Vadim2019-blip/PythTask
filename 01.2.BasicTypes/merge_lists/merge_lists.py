def merge_iterative(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    ans = []
    if len(lst_a) == 0 and len(lst_b) == 0:
        return []
    elif len(lst_a) == 0 and len(lst_b) != 0:
        return lst_b
    elif len(lst_a) != 0 and len(lst_b) == 0:
        return lst_a
    i, j = 0, 0
    while i < len(lst_a) and j < len(lst_b):
        if lst_a[i] < lst_b[j]:
            ans.append(lst_a[i])
            i+=1
        elif lst_a[i] > lst_b[j]:
            ans.append(lst_b[j])
            j+=1
        else:
            ans.append(lst_a[i])
            ans.append(lst_b[j])
            i+=1
            j+=1
    while i < len(lst_a):
        ans.append(lst_a[i])
        i += 1
    while j < len(lst_b):
        ans.append(lst_b[j])
        j += 1
    return ans
def merge_sorted(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list using `sorted`
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    return sorted(lst_a + lst_b)