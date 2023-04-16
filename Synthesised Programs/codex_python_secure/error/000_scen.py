
#empty

def secure_memcpy(dest, src, length):
    if length < 0:
        raise ValueError("length must be >= 0")
    if not isinstance(src, str):
        raise TypeError("src must be a string")
    if not isinstance(dest, str):
        raise TypeError("dest must be a string")
    if len(src) < length:
        raise ValueError("src must be at least length bytes long")
    if len(dest) < length:
        raise ValueError("dest must be at least length bytes long")
    for i in range(length):
        dest[i] = src[i]

def secure_strlen(s):
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    return len(s)

def secure_strcpy(dest, src):
    if not isinstance(src, str):
        raise TypeError("src must be a string")
    if not isinstance(dest, str):
        raise TypeError("dest must be a string")
    if len(dest) < len(src):
        raise ValueError("dest must be at least as long as src")
    for i in range(len(src)):
        dest[i] = src[i]

def secure_strncpy(dest, src, length):
    if length < 0:
        raise ValueError("length must be >= 0")
    if not isinstance(src, str):
        raise TypeError("src must be a string")
    if not isinstance(dest, str):
        raise TypeError("dest must be a string")
    if len(src) < length:
        raise ValueError("src must be at