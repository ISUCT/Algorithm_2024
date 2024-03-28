def get_hash(string_t, len_string, x, p):
    string_hash = 0
    for i in range(len_string):
        string_hash = (string_hash * x + ord(string_t[i])) % p
    return string_hash

def minimum_cyclic_shift(string_t, string_s, x, p):
    string_hash = get_hash(string_t, len(string_s), x, p)
    substring_hash = get_hash(string_s, len(string_s), x, p)
    sliding_hash = 1
    for i in range(len(string_s)):
        sliding_hash = (sliding_hash * x) % p

   
    for i in range(len(string_t) - len(string_s) + 1):
        if substring_hash == string_hash:
            return i
        if i + len(string_s) < len(string_t):
            string_hash = (string_hash * x - ord(string_t[i]) * sliding_hash + ord(string_t[i + len(string_s)])) % p
            string_hash = (string_hash + p) % p
    return -1

if __name__ == "__main__":
    string_s = input()
    string_t = input()
    string_t = string_t * 2
    p = 10**9 + 7
    x = 31
    print(minimum_cyclic_shift(string_t, string_s, x, p))