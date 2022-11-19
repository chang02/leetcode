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
    fun swapPairs(head: ListNode?): ListNode? {
        if (head == null) return null
        if (head!!.next == null) return head
        val node1 = ListNode(head!!.next!!.`val`)
        val node2 = ListNode(head!!.`val`)
        node1.next = node2
        var res: ListNode? = node1
        var cur = head!!.next
        var resCur = res!!.next
        while(true) {
            if (cur!!.next != null && cur!!.next!!.next != null) {
                val node1 = ListNode(cur!!.next!!.next!!.`val`)
                val node2 = ListNode(cur!!.next!!.`val`)
                node1.next = node2
                resCur.next = node1
                cur = cur!!.next!!.next
                resCur = resCur!!.next!!.next
            } else if (cur!!.next != null) {
                val node = ListNode(cur!!.next.`val`)
                resCur.next = node
                break
            } else {
                break
            }
        }
        return res

    }
}