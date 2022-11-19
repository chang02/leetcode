class Solution {
    fun nextPermutation(nums: IntArray): Unit {
        if (nums.size == 1) return

        val lastIndex = nums.size - 1
        if (nums[lastIndex] > nums[lastIndex - 1]) {
            swap(nums, lastIndex - 1, lastIndex)
            return
        }

        var index = lastIndex - 1
        while (index > -1) {
            if (nums[index] < nums[index + 1]) {
                break
            }
            index -= 1
        }

        if (index == -1) {
            sort(nums, 0, lastIndex)
        } else {
            var targetIndex = findNextBiggerIndex(nums, index+1, nums[index])
            swap(nums, index, targetIndex)
            sort(nums, index+1, lastIndex)
        }
    }

    fun swap(nums: IntArray, i: Int, j: Int) {
        val temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    }

    fun sort(nums: IntArray, i: Int, j: Int) {
        nums.sort(i, j + 1)
    }

    fun findNextBiggerIndex(nums: IntArray, fromI: Int, baseNum: Int): Int {
        var min = Integer.MAX_VALUE
        for (i in fromI..(nums.size-1)) {
            if (nums[i] > baseNum && nums[i] < min) {
                min = nums[i]
            }
        }
        for (i in fromI..(nums.size-1)) {
            if (nums[i] == min) return i
        }
        return -1
    }
}