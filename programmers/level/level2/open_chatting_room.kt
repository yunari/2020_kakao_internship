class Solution {
    fun solution(record: Array<String>): Array<String> {
        var name_map = mutableMapOf<String, String>()

        for (elem in record) {
            val splited = elem.split(" ")
            when (splited[0]) {
                "Enter", "Change" -> name_map[splited[1]] = splited[2]
            }
        }

        var answer = arrayListOf<String>()
        for (elem in record) {
            val splited = elem.split(" ")

            when (splited[0]) {
                "Enter" -> answer.add(name_map[splited[1]] + "���� ���Խ��ϴ�.")
                "Leave" -> answer.add(name_map[splited[1]] + "���� �������ϴ�.")
            }
        }

        return answer.toTypedArray()
    }
}

fun main() {
    val sol: Solution = Solution()
    println(sol.solution(arrayOf<String>("Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan")))
}