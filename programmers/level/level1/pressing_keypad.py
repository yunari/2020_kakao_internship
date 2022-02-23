key_coordinate = {0: [1, 0], 1: [0, 3], 2: [1, 3], 3: [2, 3], 4: [0, 2], 5: [1, 2],
6: [2, 2], 7: [0, 1], 8: [1, 1], 9: [2, 1], '*': [0, 0], '#': [2, 0]}

def get_distance(current_coord, destination_coord):
    x_distance = abs(current_coord[0] - destination_coord[0])
    y_distance = abs(current_coord[1] - destination_coord[1])

    return x_distance + y_distance

def get_which_finger_to_use(number, left_hand_loc, right_hand_loc, left_handed, left_first_try, right_first_try):
    if number == 1 or number == 4 or number == 7:
        left_hand_loc[0] = number
        return "L"
    elif number == 3 or number == 6 or number == 9:
        right_hand_loc[0] = number
        return "R"

    left_coordinate = []
    right_coordinate = []
    destination_coordinate = key_coordinate[number]

    if left_first_try[0]:
        left_coordinate = key_coordinate['*']
    else:
        left_coordinate = key_coordinate[left_hand_loc[0]]

    if right_first_try[0]:
        right_coordinate = key_coordinate['#']
    else:
        right_coordinate = key_coordinate[right_hand_loc[0]]

    left_distance = get_distance(left_coordinate, destination_coordinate)
    right_distance = get_distance(right_coordinate, destination_coordinate)

    if left_distance > right_distance:
        right_hand_loc[0] = number
        return "R"
    elif left_distance < right_distance:
        left_hand_loc[0] = number
        return "L"
    elif left_handed:
        left_hand_loc[0] = number
        return "L"
    else:
        right_hand_loc[0] = number
        return "R"

def solution(numbers, hand):
    answer = ''
    left_first_try = [True]
    right_first_try = [True]
    left_handed = True if str(hand) == 'left' else False

    left_hand_loc = [0]
    right_hand_loc = [0]

    for number in numbers:
        result_finger = get_which_finger_to_use(number, left_hand_loc, right_hand_loc, left_handed, left_first_try, right_first_try)

        if result_finger == "L":
            left_first_try[0] = False
        else:
            right_first_try[0] = False

        answer += result_finger

    return answer