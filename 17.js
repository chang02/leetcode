var letterCombinations = function(digits) {
    const digitLetterMap = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }
    const l = digits.split('').map((digit) => {
        return digitLetterMap[digit]
    })
    return l.reduce((p, c) => {
        return merge(p, c)
    }, [])
};

const merge = (l, r) => {
    console.log(l)
    console.log(r)
    if (l.length == 0) return r
    var res = []
    l.forEach((le) => {
        r.forEach((re) => {
            res.push(le+re)
        })
    })
    return res
}
