class Solution {
    fun searchRange(nums: IntArray, target: Int): IntArray {
        val searched = nums.binarySearch(target, 0, nums.size)
        if (searched < 0) {
            return intArrayOf(-1, -1)
        }

        var minIndex = searched
        var maxIndex = searched

        var minStart = 0
        var minEnd = searched - 1
        while (true) {
            val searched = nums.binarySearch(target, minStart, minEnd + 1)
            if (searched < 0) break
            minIndex = searched
            minEnd = searched - 1
        }

        var maxStart = searched + 1
        var maxEnd = nums.size - 1
        while (true) {
            val searched = nums.binarySearch(target, maxStart, maxEnd + 1)
            if (searched < 0) break
            maxIndex = searched
            maxStart = searched + 1
        }

        return intArrayOf(minIndex, maxIndex)
    }
}