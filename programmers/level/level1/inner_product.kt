class Solution_inner_product {
    fun solution(a: IntArray, b: IntArray): Int =
        a.foldIndexed(0) { idx, answer, elem -> answer + (elem * b[idx])}
}

fun main() {
    val sol: Solution_inner_product = Solution_inner_product()
    println(sol.solution(intArrayOf(1,2,3,4), intArrayOf(-3,-1,0,2)))
}