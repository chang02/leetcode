/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 var threeSumClosest = function(nums, target) {
    if (nums.length < 3) {
        return []
    }
    nums.sort((a, b) => {
        if (a > b) return 1
        if (a === b) return 0
        if (a < b) return -1
    })
    var closest = null
    for (var i = 0; i < nums.length - 2; i++) {
        var k = nums.length - 1
        for (var j = i + 1; j < nums.length - 1; j++) {
            while(true) {
                if (k <= j) break
                var sum = nums[i] + nums[j] + nums[k]
                if (closest === null) closest = sum
                if (sum === target) {
                    return target
                } else if (sum > target) {
                    closest = closer(target, closest, sum)
                    k--
                    continue
                } else {
                    if (k === nums.length - 1) {
                        closest = closer(target, closest, sum)
                        break
                    }
                    else {
                        closest = closer(target, closest, sum)
                    }
                    break
                }
            }
        }
    }
    return closest
};

const closer = (target, a, b) => {
    if (distance(a, target) > distance(b, target)) {
        return b
    } else {
        return a
    }
}

const distance = (a, b) => {
    if (a === b) return 0
    if (a > b) return a-b
    if (b > a) return b-a
}