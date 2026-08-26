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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int cnt = 0;
        ListNode temp = head;

        while (temp!= null) {
            cnt += 1;
            temp = temp.next;
        }

        temp = head;
        cnt = cnt - n;

        if (cnt == 0) {
            head = head.next;
            return head;
        }

        while (cnt > 1) {
            temp = temp.next;
            cnt -= 1;
        }

        temp.next = temp.next.next;
        return head;
        
    }
}