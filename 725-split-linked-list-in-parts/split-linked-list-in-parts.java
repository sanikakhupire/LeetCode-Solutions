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
    public ListNode[] splitListToParts(ListNode head, int k) {
        int cnt = 0;
        ListNode temp = head;
        while (temp != null) {
            cnt += 1;
            temp = temp.next;
        }

        int parts = cnt/k;
        int extra = cnt % k;

        ListNode[] result = new ListNode[k];

        temp = head;

        for (int i = 0; i < k; i++) {
            result[i] = temp;
            int size = parts;

            if (extra > 0) {
                size ++;
                extra --;
            }

            for (int j = 1; j < size; j++) {
                temp = temp.next;
            }

            if (temp != null) {
                ListNode nextPart = temp.next;
                temp.next = null;
                temp = nextPart;
            }
        }
        
        return result;
    }
}