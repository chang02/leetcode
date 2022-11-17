class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        var startIndex = 0
        var res = 0
        var duplicatedSet = mutableSetOf<Char>()
        for (i in 0..s.length-1) {
            if (!duplicatedSet.add(s[i])) {
                if (i - startIndex > res) {
                    res = i-startIndex
                }
                val nextStartIndex = s.indexOf(s[i], startIndex) + 1
                for (j in startIndex..nextStartIndex-1) {
                    duplicatedSet.remove(s[j])
                }
                duplicatedSet.add(s[i])
                startIndex = s.indexOf(s[i], startIndex) + 1
                continue
            }
        }
        if (s.length - startIndex > res) {
            res = s.length-startIndex
        }
        return res
    }
}