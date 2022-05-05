class Solution {
    fun isPrimeNumber(number: Int): Boolean {
        if (number == 0 || number == 1)
            return false
        if (number == 2)
            return true
        for (i in 3..number - 1) {
            if (number % i == 0)
                return false
        }
        return true
    }

    fun solution(nums: IntArray): Int {
        var result: Int = 0

        for ((idx1, elem1) in nums.withIndex()) {
            for ((idx2, elem2) in nums.slice(idx1 + 1..nums.size - 1).withIndex()) {
                for (elem3 in nums.slice(idx1 + idx2 + 2..nums.size - 1)) {
                    if (isPrimeNumber(elem1 + elem2 + elem3)) result++
                }
            }
        }

        return result
    }
}

fun main() {
    val sol: Solution = Solution()
    println(sol.solution(intArrayOf(1,2,7,6,4)))
}