/**
 * @param {number} n
 * @return {string[]}
 */
 var generateParenthesis = function(n) {
    var arr = ['(']
    while (arr[0].length !== n*2) {
        var poped = arr.shift()
        var leftCount = poped.split('').filter((c) => c === '(').length
        var rightCount = poped.split('').filter((c) => c === ')').length
        if (leftCount === rightCount) {
            arr.push(poped + '(')
        }
        if (leftCount > rightCount) {
            if (leftCount < n) {
                arr.push(poped + '(')
            }
            arr.push(poped + ')')
        }
    }
    return arr
};