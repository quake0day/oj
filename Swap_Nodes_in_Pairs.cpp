class Solution{
    public:
        ListNode *swapPairs(ListNode *head){
            ListNode *dummy = new ListNode(0);
            dummy->next = head;
            head = dummy;
            while(head) head = swapNodes(head->next);
            head = dummy->next;
            delete dummy;
            return head;
        }

        ListNode *swapNodes(ListNode *&head){
            if(!head || !head->next) return NULL;
            ListNode *tail = head;
            ListNode *nextHead = head->next->next;
            head = head->next;
            head->next = tail;
            tail->next = nextHead;
            return tail;

        }
}

