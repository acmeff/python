# brute force
def word_parity(binary_word):
    result = 0
    while binary_word:
        result ^= binary_word & 1
        binary_word >>= 1
    return result
