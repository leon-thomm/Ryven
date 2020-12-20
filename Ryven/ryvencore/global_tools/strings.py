def get_longest_line(s: str):
    lines = s.split('\n')
    lines = [line.replace('\n', '') for line in lines]
    longest_line_found = ''
    for line in lines:
        if len(line) > len(longest_line_found):
            longest_line_found = line
    return line


def shorten(s: str, max_chars: int, line_break: bool = False):
    """Ensures, that a given string does not exceed a given max length. If it would, its cut in the middle."""
    l = len(s)
    if l > max_chars:
        insert = ' . . . '
        if line_break:
            insert = '\n'+insert+'\n'
        insert_length = len(insert)
        left = s[:round((max_chars-insert_length)/2)]
        right = s[round(l-((max_chars-insert_length)/2)):]
        return left+insert+right
    else:
        return s