def solution(id_list, report, k):
    report_list = {}
    for id in id_list:
        report_list[id] = [set(), int()]

    for each_report in report:
        report_split = each_report.split()
        report_list[report_split[1]][0].add(report_split[0])

    for id in report_list:
        if len(report_list[id][0]) >= k:
            for reporting_id in report_list[id][0]:
                report_list[reporting_id][1] += 1

    answer = []

    for id in id_list:
        answer.append(report_list[id][1])

    return answer

if __name__ == "__main__":
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)