BASE62 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encode_for_shorten(val: int, alpha: str=BASE62) -> str:
    if val == 0:
        return alpha[0]

    arr = []
    while val:
        val, tmp = divmod(val, 62)
        arr.append(alpha[tmp])
    arr.reverse()

    return ''.join(arr)


def decode_for_original(encoded: str, alpha: str=BASE62) -> str:
    print(encoded)

    base = len(alpha)
    encoded_str_len = len(encoded)
    num = 0

    index = 0
    for c in encoded:
        power = (encoded_str_len - (index + 1))
        num += alpha.index(c) * (base ** power)
        index += 1

    print(num)

    return num
