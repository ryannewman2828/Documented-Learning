public class AddTwoNumbers_2 {

    /**
     * Theres no real trick to this one. I iterate through both linked lists while adding the numbers together and
     * construct the new linked list. A carry over flag is used for when we need to carry the 1.
     */
    
    static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode root = null;
        ListNode temp = null;
        boolean carry = false;

        while (l1 != null || l2 != null) {
            int val = 0;

            if (l1 != null) {
                val += l1.val;
                l1 = l1.next;
            }

            if (l2 != null) {
                val += l2.val;
                l2 = l2.next;
            }

            if (carry) {
                val++;
                carry = false;
            }

            if (val >= 10) {
                val -= 10;
                carry = true;
            }

            if (root == null) {
                root = new ListNode(val);
                temp = root;
            } else {
                temp.next = new ListNode(val);
                temp = temp.next;
            }
        }

        if (carry) {
            temp.next = new ListNode(1);
        }

        return root;
    }
}
