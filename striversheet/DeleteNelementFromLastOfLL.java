public class DeleteNelementFromLastOfLL {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        if(head == null){
            return null;
        }

        if(head.next == null){
            return null;
        }
         
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode fast = dummy;
        ListNode slow = dummy;
        
        for(int i =0;i<=n;i++){
            fast = fast.next;
        }

        while(fast != null){
            fast = fast.next;
            slow = slow.next;
        }
        
        ListNode delNode = slow.next;
        slow.next = slow.next.next;
        return null;
    }
}
