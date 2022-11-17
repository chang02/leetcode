/**
 * @param {number} x
 * @return {number}
 */
 var reverse = function(x) {
    const str = x.toString()
    const min = (2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2).toString()
    const max = (2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2 - 1).toString()
    var reversedStr = ""
    var flag = true
    if (str[0] == "-") {
        flag = false
    }
    if (flag) {
        reversedStr = str.split('').reverse().join('')
        const lastIndex = lastIndexToRemove(reversedStr)
        reversedStr = reversedStr.substring(lastIndex + 1)
        if (compare(max, reversedStr)) {
            return reversedStr
        } else {
            return 0
        }
    } else {
        reversedStr = str.substring(1).split('').reverse().join('')
        const lastIndex = lastIndexToRemove(reversedStr)
        reversedStr = reversedStr.substring(lastIndex + 1)
        if (compare(min, reversedStr)) {
            return "-" + reversedStr
        } else {
            return 0
        }
    }
};

const compare = (a, b) => {
    if (a.length > b.length) {
        return true
    } else if (a.length < b.length) {
        return false
    } else {
        console.log("here")
        for (var i = 0; i < a.length; i++) {
            if (parseInt(a[i]) > parseInt(b[i])) {
                return true
            } else if (parseInt(a[i]) < parseInt(b[i])) {
                return false
            }
        }
        return false
    }
}

const lastIndexToRemove = (s) => {
    var i
    for (i = -1; i < s.length; i++) {
        if (s[i] != '0') {
            return i - 1
        }
    }
}