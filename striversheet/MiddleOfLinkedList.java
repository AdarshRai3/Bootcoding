public class MiddleOfLinkedList {
    // public class ListNode {
    //     *     int val;
    //     *     ListNode next;
    //     *     ListNode() {}
    //     *     ListNode(int val) { this.val = val; }
    //     *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    //     * }

    public ListNode middleNode(ListNode head) {
       ListNode fast = head;
       ListNode slow = head;
       while(fast != null && fast.next!=null){
        fast = fast.next.next;
        slow = slow.next;
       }
       return slow;
    }

    //In this question for finding the middle of the linked list we use the approach of fast and slow pointers in which we have one fast pointer which move by two and one slow pointer which move by one as the fast pointer reaches null ot fast.next = null , slow will point at the mid - point 
    //Time Complexity : O(N/2)
    //Space Complexity:O(1)
    //In the brute force approach we have to have find the length of linked list and then use mid=(left+(right-left)/2)
}
