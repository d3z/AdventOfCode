import re


def set_character_at(s, i, c):
    '''
    >>> set_character_at("test", 1, "u")
    'tust'
    >>> set_character_at("another test", 7, "_")
    'another_test'
    '''
    return s[:i] + c + s[i+1:]


def increment(password):
    '''
    >>> increment("a")
    'b'
    >>> increment("aa")
    'ab'
    >>> increment("abz")
    'aca'
    '''
    def increment_char(p, i):
        c = ord(p[i]) + 1
        if c > ord('z'):
            p = set_character_at(p, i, 'a')
            return increment_char(p, i - 1)
        p = set_character_at(p, i, chr(c))
        return p
    return increment_char(password, len(password)-1)



def is_valid_password(password):
    '''
    >>> is_valid_password("hijklmmn")
    False
    >>> is_valid_password("abbcegjk")
    False
    >>> is_valid_password("aadcchjh")
    False
    >>> is_valid_password("aabcchjk")
    True
    '''
    if re.search(r'i|o|l', password):
        return False
    if not re.search(r'(.)\1.*?(.)\2', password):
        return False
    password = [ord(c) for c in password]
    for i in range(len(password) - 3):
        if password[i] == password[i+1] - 1 and password[i+1] == password[i+2] - 1:
            return True
    return False


def find_next_valid_password(password):
    '''
    >>> find_next_valid_password("abcdefgh")
    'abcdffaa'
    >>> find_next_valid_password("ghijklmn")
    'ghjaabcc'
    '''
    password = increment(password)
    while not is_valid_password(password):
        password = increment(password)
    return password


if __name__ == '__main__':
    import doctest
    doctest.testmod()
