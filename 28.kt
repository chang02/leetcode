class Solution {
    fun strStr(haystack: String, needle: String): Int {
        if (needle.length > haystack.length) return -1
        var flag = false

        for (i in 0..(haystack.length-needle.length)) {
            for (j in needle.indices) {
                if (haystack[i + j] != needle[j]) {
                    break
                }
                if (j == needle.length - 1) {
                    flag = true
                }
            }
            if (flag == true) {
                return i
            }
        }
        return -1
    }
}