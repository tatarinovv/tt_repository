def pal(s):
    return s == s[::-1]

def mirror(s):
    mirror_map = {
        'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T', 'U': 'U', 'V': 'V',
        'W': 'W', 'X': 'X', 'Y': 'Y', '1': '1', '8': '8',
        'E': '3', '3': 'E', 'J': 'L', 'L': 'J', 'S': '2', '2': 'S', 'Z': '5', '5': 'Z'
    }

    res = ''
    for char in s:
        if char not in mirror_map:
            return False  # Если есть символ без зеркального отображения, возвращаем False
        res += mirror_map[char]
    return res[::-1] == s

def check(s):
    palindrome = pal(s)
    mirrored = mirror(s)

    if palindrome and mirrored:
        return f'"{s}" is a mirrored palindrome.'
    elif palindrome:
        return f'"{s}" is a regular palindrome.'
    elif mirrored:
        return f'"{s}" is a mirrored string.'
    else:
        return f'"{s}" is not a palindrome.'

a = input()
result = check(a)
print(result)
