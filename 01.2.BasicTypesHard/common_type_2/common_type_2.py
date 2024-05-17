import typing as tp


def find_general_type(data):
    types = set(type(elem) for elem in data if elem not in (None, ""))
    if len(types) == 0:
        return str
    if str in types:
        return str
    if float in types:
        return float
    if bool in types:
        return bool
    return int


def convert_to_common_type(data: list[tp.Any]) -> list[tp.Any]:
    """
    Takes list of multiple types' elements and convert each element to common type according to given rules
    :param data: list of multiple types' elements
    :return: list with elements converted to common type
    """
    for i in data:
        if type(i) is list or type(i) is tuple:
            ans = list()
            for element in data:
                if list == type(element):
                    ans += [list(element)]

                elif tuple == type(element):
                    ans += [list(element)]
                elif element is None:
                    ans += [[]]

                elif element == "":
                    ans += [[]]
                else:
                    ans += [[element]]
            return ans

    general = find_general_type(data)
    ans = []
    for element in data:
        if element is None or element == "":
            ans += [general()]
        else:
            ans += [general(element)]
    return ans