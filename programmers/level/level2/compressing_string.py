def solution(s):
    if len(s) == 1:
        return 1

    smallest_len = len(s)
    for word_len in range(1, int(len(s) / 2) + 1):
        split_arr = [s[i:i + word_len] for i in range(0, len(s), word_len)]
        split_arr += '0'
        compressed_str = ""
        cnt = 0
        dup_word = ""
        for split_char in split_arr:
            if not dup_word:
                dup_word = split_char
                cnt = 1
            elif dup_word == split_char:
                cnt += 1
            else:
                if cnt == 1:
                    compressed_str += dup_word
                else:
                    compressed_str += str(cnt)
                    compressed_str += dup_word
                dup_word = split_char
                cnt = 1

        if len(compressed_str) < smallest_len:
            smallest_len = len(compressed_str)

    return smallest_len

if __name__ == "__main__":
    solution("aabbaccc")