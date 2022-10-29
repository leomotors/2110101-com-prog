def check_pattern(word: str, pattern: str):
    if len(word) != len(pattern):
        return (False, [])

    used_in_pattern = []

    for i in range(len(word)):
        if word[i] != pattern[i]:
            if pattern[i] == '?':
                used_in_pattern.append(word[i])
            else:
                return (False, [])

    return [True, used_in_pattern]


def match(word: str, pattern: str, include_chars: str, exclude_chars: str):
    ok, used_in_pattern = check_pattern(word, pattern)

    if not ok:
        return False

    used_map = {}

    for used in used_in_pattern:
        if used in exclude_chars:
            return False
        used_map[used] = used_map.get(used, 0) + 1

    for inc in include_chars:
        if used_map.get(inc, 0) <= 0:
            return False
        used_map[inc] -= 1

    return True


exec(input())  # DON'T remove this line
