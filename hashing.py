def quizhash(s) -> int:
    hash_value = 0
    for ch in s:
        hash_value = (hash_value * 31 + ord(ch)) % 10007
    return hash_value
