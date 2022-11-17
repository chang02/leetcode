/**
 * @param {number} num
 * @return {string}
 */
 var intToRoman = function(num) {
    var cur = num
    var res = ""
    var devideBy1000 = parseInt(cur / 1000)
    if (devideBy1000 > 0) {
        console.log(1)
        res += "M".repeat(devideBy1000)
        cur -= devideBy1000 * 1000
    }
    if (cur >= 900) {
        console.log(2)
        res += "CM"
        cur -= 900
    }
    if (cur >= 500) {
        console.log(3)
        res += "D"
        cur -= 500
    }
    if (cur >= 400) {
        console.log(4)
        res += "CD"
        cur -= 400
    }
    var devideBy100 = parseInt(cur / 100)
    if (devideBy100 > 0) {
        console.log(5)
        res += "C".repeat(devideBy100)
        cur -= devideBy100 * 100
    }
    if (cur >= 90) {
        console.log(6)
        res += "XC"
        cur -= 90
    }
    if (cur >= 50) {
        console.log(7)
        res += "L"
        cur -= 50
    }
    if (cur >= 40) {
        console.log(8)
        res += "XL"
        cur -= 40
    }
    var devideBy10 = parseInt(cur / 10)
    if (devideBy10 > 0) {
        console.log(9)
        res += "X".repeat(devideBy10)
        cur -= devideBy10 * 10
    }
    if (cur == 9) {
        console.log(10)
        res += "IX"
        cur -= 9
    }
    if (cur >= 5) {
        console.log(11)
        res += "V"
        cur -= 5
    }
    if (cur == 4) {
        res += "IV"
        cur -= 4
    }
    if (cur > 0) {
        res += "I".repeat(cur)
        cur = 0
    }
    return res
};