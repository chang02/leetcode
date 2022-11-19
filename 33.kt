class Solution {
    fun search(nums: IntArray, target: Int): Int {
        var start = 0
        var end = nums.size - 1

        while (true) {
            if (start > end) break
            if (end - start < 5) {
                return findIndex(nums, start, end, target)
            }
            var index = (end - start) / 2 + start
            if (nums[index] == target) return index
            if (isPivotOnLeft(nums, start, end, index)) {
                val searched = nums.binarySearch(target, index, end + 1)
                if (searched < 0) {
                    end = index - 1
                } else {
                    return searched
                }
            }
            if (!isPivotOnLeft(nums, start, end, index)) {
                val searched = nums.binarySearch(target, start, index + 1)
                if (searched < 0) {
                    start = index + 1
                } else {
                    return searched
                }
            }
        }
        return -1
    }

    fun isPivotOnLeft(nums: IntArray, start: Int, end: Int, index: Int): Boolean {
        if (nums[start] > nums[index]) return true
        else return false
    }

    fun findIndex(nums: IntArray, start: Int, end: Int, target: Int): Int {
        for (i in start..end) {
            if (nums[i] == target) return i
        }
        return -1
    }

}