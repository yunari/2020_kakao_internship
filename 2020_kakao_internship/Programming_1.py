def solution(s: str):
    answer = 0
    num_dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
               "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    str_answer = str()
    num_word = str()
    for one_char in s:
        if one_char.isnumeric():
            str_answer += one_char
            continue
        num_word += one_char
        if num_word in num_dic:
            str_answer += str(num_dic[num_word])
            num_word = ""

    answer = int(str_answer)
    return answer