/**
 * @param {string} s
 * @return {number}
 */
 var myAtoi = function(s) {
    const min = (2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2).toString()
    const max = (2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2 - 1).toString()

    var trimmed = s.trim()

    var state = ''
    var isPositive = true
    var onlyNumber = ''
    for (var i = 0; i < trimmed.length; i++) {
        console.log(trimmed[i])
        if (trimmed[i] == ' ') {
            break
        } else if (trimmed[i] == '+' || trimmed[i] == '-') {
            if (state === '') {
                state = 'signChecked'
                if (trimmed[i] == '-') {
                    isPositive = false
                }
            } else if (state === 'signChecked') {
                return 0
            } else if (state == 'number') {
                break
            }
        } else if (!isNaN(trimmed[i])) {
            state = 'number'
            if (trimmed[i] != '0' || onlyNumber.length > 0) {
                onlyNumber += trimmed[i]
            }
        } else if (isNaN(trimmed[i]) && state != 'number') {
            return 0
        } else if (isNaN(trimmed[i]) && state == 'number') {
            break
        }
    }

    console.log(state)
    console.log(onlyNumber)

    if (state != 'number' || onlyNumber === "") {
        return 0
    }
    
    if (isPositive) {
        if (isBigger(max, onlyNumber)) {
            return parseInt(onlyNumber)
        } else {
            return parseInt(max)
        }
    } else {
        if (isBigger(min, onlyNumber)) {
            return parseInt(-1 * onlyNumber)
        } else {
            return parseInt(-1 * min)
        }
    }
};

const isBigger = (a, b) => {
    if (a.length > b.length) {
        return true
    } else if (a.length < b.length) {
        return false
    } else {
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

const firstIndexOf = (s) => {
    var i
    for (i = 0; i < s.length; i++) {
        if (!isNaN(s[i]) || s[i] == '-') {
            return i
        }
    }
    return 0
}

const lastDigitIndexOf = (s) => {
    var i
    for (i = 0; i < s.length; i++) {
        if (isNaN(s[i])) {
            return i - 1
        }
    }
    return i
}