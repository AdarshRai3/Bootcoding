public class LLSorted{
     
    //First step is to findMid  
    private ListNode findMid(ListNode head){
        if(head == null || head.next == null){
            return head;
        }

        ListNode slow = head;
        ListNode fast =head.next;

        while(fast!=null && fast.next !=null){
             slow = slow.next;
             fast = fast.next.next;
        }
        return slow;
    }

    private ListNode mergeTwoSortedLL(ListNode L1, ListNode L2){
        ListNode dummy = new ListNode(-1);
        ListNode temp = dummy;

        while(L1 != null && L2 != null){
            if(L1.val<=L2.val){
                temp.next=L1;
                L1=L1.next;
            }else{
                temp.next=L2;
                L2=L2.next;
            }
            temp = temp.next;
        }

        if(L1!=null){
            temp.next = L1;
        }else{
            temp.next = L2;
        }

        return dummy.next;
    }
    public ListNode sortList(ListNode head) {
       if(head == null || head.next == null){
        return head;
       }   

       ListNode mid = findMid(head);

       ListNode right = mid.next;
       mid.next = null;
       ListNode left =head;

       left = sortList(left);
       right=sortList(right);

       return mergeTwoSortedLL(left , right);
    }
}