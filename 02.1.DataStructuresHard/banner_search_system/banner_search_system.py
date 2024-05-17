from collections import defaultdict
import heapq
import collections
def normalize(
        text: str
        ) -> str:
    """
    Removes punctuation and digits and convert to lower case
    :param text: text to normalize
    :return: normalized query
    """
    text = text.lower()
    lst1 = list(text)
    ans = []
    for i in lst1:
        if i.isalpha() or i == " ":
            ans.append(i)
        else:
            continue
    return "".join(ans)


def get_words(
        query: str
        ) -> list[str]:
    """
    Split by words and leave only words with letters greater than 3
    :param query: query to split
    :return: filtered and split query by words
    """
    words = normalize(query).split(" ")
    return [x for x in words if len(x) > 3]


def build_index(
        banners: list[str]
        ) -> dict[str, list[int]]:
    """
    Create index from words to banners ids with preserving order and without repetitions
    :param banners: list of banners for indexation
    :return: mapping from word to banners ids
    """
    index = defaultdict(list)
    for i, banner in enumerate(banners):
        words =get_words(banner)  # Разбиваем баннер на слова
        unique_words = list(set(words))  # Удаляем повторяющиеся слова
        for word in unique_words:
            index[word].append(i)  # Добавляем ID баннера в список для данного слова
    return index



def get_banner_indices_by_query(
        query: str,
        index: dict[str, list[int]]
        ) -> list[int]:
    """
    Extract banners indices from index, if all words from query contains in indexed banner
    :param query: query to find banners
    :param index: index to search banners
    :return: list of indices of suitable banners
    """
    words = get_words(query) # Разбиваем запрос на слова
    banner_indices = [index.get(word, []) for word in words]  # Получаем список списков индексов для каждого слова из запроса
    if not all(banner_indices):  # Если хотя бы для одного слова нет индекса, возвращаем пустой список
        return []
    merged_indices = list(heapq.merge(*banner_indices))  # Объединяем списки индексов
    matching_indices = [index for index, count in collections.Counter(merged_indices).items() if count == len(words)]  # Находим индексы, встречающиеся столько раз, сколько слов в запросе
    return matching_indices


#########################
# Don't change this code
#########################

def get_banners(
        query: str,
        index: dict[str, list[int]],
        banners: list[str]
        ) -> list[str]:
    """
    Extract banners matched to queries
    :param query: query to match
    :param index: word-banner_ids index
    :param banners: list of banners
    :return: list of matched banners
    """
    indices = get_banner_indices_by_query(query, index)
    return [banners[i] for i in indices]

#########################
