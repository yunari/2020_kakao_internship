def solution(new_id):
    # 1
    new_id = new_id.lower()

    # 2
    for id_char in new_id:
        if not id_char.isdigit() and not id_char.isalpha() and id_char != "-" and id_char != "_" and id_char != ".":
            new_id = new_id.replace(id_char, "")

    # 3
    idx = 0
    for id_char in new_id:
        if idx == len(new_id) - 1:
            break
        if id_char == "." and new_id[idx + 1] == ".":
            new_id = new_id[:idx] + new_id[idx + 1:]
        else:
            idx += 1

    # 4
    if new_id[0] == ".":
        new_id = new_id[1:]
    if new_id and new_id[-1] == ".":
        new_id = new_id[:-1]

    # 5
    if not new_id:
        new_id = "a"

    # 6
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]

    # 7
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id

if __name__ == "__main__":
    solution("abcdefghijklmn.p")