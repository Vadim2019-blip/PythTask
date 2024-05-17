import enum


class Status(enum.Enum):
    TEMPORARY = 1
    PERMANENT = 2


def extract_alphabet(graph: dict[str, set[str]]) -> list[str]:
    """
    Extract alphabet from graph
    :param graph: graph with partial order
    :return: alphabet
    """
    incoming_edges = {v: set() for v in graph}
    for vertices in graph.values():
        for v in vertices:
            incoming_edges[v].add(v)

    status = {v: Status.TEMPORARY for v in graph}
    result = []

    def visit(vertex):
        if status[vertex] == Status.PERMANENT:
            return
        if status[vertex] == Status.TEMPORARY:
            status[vertex] = Status.TEMPORARY
            for neighbor in graph[vertex]:
                visit(neighbor)
            status[vertex] = Status.PERMANENT
            result.append(vertex)

    for vertex in graph:
        visit(vertex)
    return result[::-1]


def build_graph(words: list[str]) -> dict[str, set[str]]:
    """
    Build graph from ordered words. Graph should contain all letters from words
    :param words: ordered words
    :return: graph
    """
    graph = {}

    for word1, word2 in zip(words, words[1:]):
        for char1, char2 in zip(word1, word2):
            if char1 != char2:
                if char1 not in graph:
                    graph[char1] = set()
                graph[char1].add(char2)
                break  # Прерываем цикл на первой различающейся букве

    all_chars = set("".join(words))
    for char in all_chars:
        if char not in graph:
            graph[char] = set()

    return graph

#########################
# Don't change this code
#########################

def get_alphabet(
        words: list[str]
        ) -> list[str]:
    """
    Extract alphabet from sorted words
    :param words: sorted words
    :return: alphabet
    """
    graph = build_graph(words)
    return extract_alphabet(graph)

#########################
