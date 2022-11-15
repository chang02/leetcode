/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
 var fourSum = function(nums, target) {
    var sorted = nums.sort(function(a,b) {
        if (a > b) return 1
        if (a === b) return 0
        if (a < b) return -1
    })
    var res = []
    for (var i = 0; i < sorted.length-3; i++) {
        if (i > 0 && sorted[i-1] === sorted[i]) continue
        for (var j=i+1; j < sorted.length-2; j++) {
            if (j > i+1 && sorted[j-1] === sorted[j]) continue
            var l = sorted.length - 1
            for (var k=j+1; k < sorted.length-1; k++) {
                if (k > j+1 && sorted[k-1] === sorted[k]) continue
                while(k < l) {
                    if (l < sorted.length-1 && sorted[l] == sorted[l+1]) {
                        l--
                        continue
                    }
                    var sum = sorted[i] + sorted[j] + sorted[k] + sorted[l]
                    if (sum > target) {
                        l -= 1
                        continue
                    } else if (sum === target) {
                        res.push([sorted[i], sorted[j], sorted[k], sorted[l]])
                        break
                    } else {
                        break
                    }
                }
            }
        }
    }
    return res
};