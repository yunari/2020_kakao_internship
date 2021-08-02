def is_partition_exist_between_participants(participant_idx_1, participant_idx_2, partition_idxes, manhattan_dis):
    if manhattan_dis == 1:
        return False

    if participant_idx_1[0] == participant_idx_2[0]:
        for col_idx in range(min(participant_idx_1[1], participant_idx_2[1]) + 1, max(participant_idx_1[1], participant_idx_2[1])):
            partition_idx = [participant_idx_1[0], col_idx]
            if partition_idx not in partition_idxes:
                return False
    elif participant_idx_1[1] == participant_idx_2[1]:
        for row_idx in range(min(participant_idx_1[0], participant_idx_2[0]) + 1, max(participant_idx_1[0], participant_idx_2[0])):
            partition_idx = [row_idx, participant_idx_1[1]]
            if partition_idx not in partition_idxes:
                return False
    else:
        partition_1 = [participant_idx_1[0], participant_idx_2[1]]
        if partition_1 not in partition_idxes:
            return False
        partition_2 = [participant_idx_2[0], participant_idx_1[1]]
        if partition_2 not in partition_idxes:
            return False
    return True

def is_manhattan_distance_over_2(coord_1, coord_2):
    manhattan_distance = abs(coord_1[0] - coord_2[0]) + abs(coord_1[1] - coord_2[1])
    if (manhattan_distance > 2):
        return True, manhattan_distance
    return False, manhattan_distance

def solution(places):
    answer = []

    for place in places:
        participant_idxes = []
        partition_idxes = []

        for row_idx, row in enumerate(place):
            for col_idx, col in enumerate(row):
                if col == "P":
                    participant_idxes.append([row_idx, col_idx])
                elif col == "X":
                    partition_idxes.append([row_idx, col_idx])

        close_participant_exist = 1
        for comparing_idx, comparing_participant_idx in enumerate(participant_idxes):
            for iterating_participant_idx in participant_idxes[comparing_idx + 1:]:
                manhattan_dis = is_manhattan_distance_over_2(comparing_participant_idx, iterating_participant_idx)
                if manhattan_dis[0] == False:
                    if is_partition_exist_between_participants(comparing_participant_idx, iterating_participant_idx, partition_idxes, manhattan_dis[1]) == False:
                        close_participant_exist = 0
                        break
            if close_participant_exist == 0:
                break

        answer.append(close_participant_exist)

    return answer

if __name__ == "__main__":
    print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))