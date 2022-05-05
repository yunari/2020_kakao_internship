class Solution_adding_YinYang {
    fun solution(absolutes: IntArray, signs: BooleanArray): Int {
        var answer: Int = 0

        for ((idx, elem) in absolutes.withIndex()) {
            if (signs.get(idx)) answer += elem else answer += (elem * -1)
        }

        return answer
    }
}

fun main()
{
    val sol: Solution_adding_YinYang = Solution_adding_YinYang()
    val ret: Int = sol.solution(intArrayOf(4, 7, 12), booleanArrayOf(true,false,true))
    println(ret)
}