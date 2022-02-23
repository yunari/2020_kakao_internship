import re
import itertools


def operator_func(operator, left, right):
    if operator == '+':
        return left + right
    elif operator == '-':
        return left - right
    elif operator == '*':
        return left * right

    return 0


def solution(expression):
    answer = 0

    operators = ['+', '-', '*']
    exp_arr = []
    each_num_str = ""

    for exp_char in expression:
        if exp_char in operators:
            if each_num_str != "":
                exp_arr.append(int(each_num_str))
                each_num_str = ""
            exp_arr.append(exp_char)
        else:
            each_num_str += exp_char
    exp_arr.append(int(each_num_str))

    operator_orders = list(itertools.permutations(operators, 3))

    for operator_order in operator_orders:
        exp_arr_copy = exp_arr[:]
        for operator in operator_order:
            while exp_arr_copy.count(operator) > 0:
                idx = exp_arr_copy.index(operator)
                operator_cal_result = operator_func(operator, exp_arr_copy[idx - 1], exp_arr_copy[idx + 1])
                del exp_arr_copy[idx + 1]
                del exp_arr_copy[idx]
                del exp_arr_copy[idx - 1]
                exp_arr_copy.insert(idx - 1, operator_cal_result)

        cal_result = abs(int(exp_arr_copy[0]))
        if answer < cal_result:
            answer = cal_result

    return answer


###if __name__ == "__main__":
###    print(solution("100-200*300-500+20"))