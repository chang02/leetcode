/**
 * @param {number[]} height
 * @return {number}
 */
 var maxArea = function(height) {
    var i = 0
    var j = height.length - 1
    var max = 0
    while (i < j) {
        max = Math.max(max, (j - i) * Math.min(height[i], height[j]))
        height[i] > height[j] ? j-- : i++
    }
    return max
};