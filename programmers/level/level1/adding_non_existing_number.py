def solution(numbers):
    add_all = 0
    for i in range(0, 10):
        add_all += i

    add_numbers = 0
    for i in numbers:
        add_numbers += i

    return add_all - add_numbers

if __name__ == "__main__":
    solution([1,2,3,4,6,7,8,0])