rank_info = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

def solution(lottos, win_nums):
    answer = []
    match_cnt = 0

    for num in lottos:
        if win_nums.count(num):
            match_cnt += 1

    answer.append(rank_info[match_cnt])

    match_cnt += lottos.count(0)
    answer.insert(0, rank_info[match_cnt])

    return answer

if __name__ == "__main__":
    solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])