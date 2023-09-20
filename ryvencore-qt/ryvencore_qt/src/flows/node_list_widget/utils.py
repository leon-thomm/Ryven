import textdistance


def dec(i: int, length: int) -> int:
    if i != 0:
        return i - 1
    else:
        return length - 1

def inc(i: int, length: int) -> int:
    if i != length - 1:
        return i + 1
    else:
        return 0


def sort_nodes(nodes):
    return sorted(nodes, key=lambda x: x.title.lower())


def sort_by_val(d: dict) -> dict:
    return {
        k: v
        for k, v in sorted(
            d.items(),

            # x: (key, value); sort by value
            key=lambda x: x[1]
        )
    }


def search(items: dict, text: str) -> dict:
    """performs the search on `items` under search string `text`"""
    dist = textdistance.sorensen_dice.distance

    distances = {}

    for item, tags in items.items():
        min_dist = 1.0
        for tag in tags:
            min_dist = min(min_dist, dist(text, tag))

        distances[item] = min_dist

    return sort_by_val(distances)
