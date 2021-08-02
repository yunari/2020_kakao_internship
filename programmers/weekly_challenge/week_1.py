def solution(price, money, count):
    answer = -1

    total_money = 0
    for current_cnt in range(count):
        total_money += price * (current_cnt + 1)

    if (money - total_money) >= 0:
        answer = 0
    else:
        answer = total_money - money

    return answer

def best_like_solution(price, money, count):
    return abs(min(money - sum([price * i for i in range(1, count + 1)]), 0))

if __name__ == "__main__":
    print(best_like_solution(3, 20, 4))