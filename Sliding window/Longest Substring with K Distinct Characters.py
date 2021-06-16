from collections import deque
hsh = {}
start = 0   
max_len = 0

for end in range(len(s)):
    end_char = s[end]
    if end_char not in hsh:
        hsh[end_char] = 0
    hsh[end_char] += 1

    while len(hsh) > k:
        start_char = s[start]
        hsh[start_char] -= 1
        if hsh[start_char] == 0 :
            del hsh[start_char]
        start += 1
    max_len = max(max_len, end-start+1)

print(max_len)
