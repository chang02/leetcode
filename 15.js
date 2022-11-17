/**
 * @param {number[]} nums
 * @return {number[][]}
 */
 var threeSum = function(nums) {
    if (nums.length < 3) {
        return []
    }
    nums.sort((a, b) => {
        if (a > b) return 1
        if (a === b) return 0
        if (a < b) return -1
    })
    console.log(nums)
    var res = []
    for (var i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] === nums[i-1]) {
            continue
        }
        var k = nums.length - 1
        for (var j = i + 1; j < nums.length - 1; j++) {
            if (j > i + 1 && nums[j] === nums[j-1]) {
                continue
            }
            while(true) {
                if (k <= j) break
                if (k < nums.length-1 && nums[k] === nums[k+1]) {
                    k--
                    continue
                }
                var sum = nums[i] + nums[j] + nums[k]
                if (sum === 0) {
                    console.log(i, j, k)
                    res.push([nums[i], nums[j], nums[k]])
                    k--
                } else if (sum > 0) {
                    k--
                    continue
                } else {
                    break
                }
            }
        }
    }
    return res
};