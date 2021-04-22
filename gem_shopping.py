def solution(gems):
    answer = []

    gems_without_dup = set(gems)
    answer_list = []

    for start_gem_idx in range(0, len(gems)):
        gems_without_dup_copy = gems_without_dup.copy()

        for iter_gem_idx in range(start_gem_idx, len(gems)):
            current_gem = gems[iter_gem_idx]
            if current_gem in gems_without_dup_copy:
                gems_without_dup_copy.remove(current_gem)

            if len(gems_without_dup_copy) == 0:
                answer_list.append([start_gem_idx, iter_gem_idx])

    shortest_size = len(gems)
    short_answer_list = []
    for each_answer in answer_list:
        current_size = each_answer[1] - each_answer[0]
        if current_size < shortest_size:
            shortest_size = current_size
            short_answer_list.clear()
            short_answer_list.append([each_answer[0] + 1, each_answer[1] + 1])

    return short_answer_list[0]