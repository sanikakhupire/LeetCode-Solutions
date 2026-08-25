/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        ListNode odd = head;
        if (head == null || head.next == null || head.next.next == null) {
            return head;
        }
        ListNode even = head.next;
        ListNode temp = head.next;
        while (temp!= null && temp.next != null) {
            odd.next = temp.next;
            temp.next = odd.next.next;
            temp = temp.next;
            odd = odd.next;
        }
        odd.next = even;

        return head;
    }
}