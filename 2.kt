/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun addTwoNumbers(l1: ListNode, l2: ListNode): ListNode {
        var cur1: ListNode? = l1
        var cur2: ListNode? = l2
        var res: ListNode? = null
        var lastNode: ListNode? = null
        var flag = false
        while (cur1 != null || cur2 != null || flag) {
            if (cur1 == null && cur2 == null && flag) {
                lastNode!!.next = ListNode(1)
                flag = false
                continue
            }
            var value = (cur1?.`val` ?: 0) + (cur2?.`val` ?: 0)
            if (flag) value += 1
            if (value >= 10) {
                value = value - 10
                flag = true
            } else {
                flag = false
            }
            if (res == null) {
                res = ListNode(value)
                lastNode = res
            } else {
                lastNode!!.next = ListNode(value)
                lastNode = lastNode.next
            }

            cur1 = cur1?.next
            cur2 = cur2?.next
        }
        return res!!
    }
}