/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} m
 * @param {number} n
 * @return {ListNode}
 */
var reverseBetween = function(head, m, n) {
	
	var dummy = new ListNode(0),
		prev,
		cur = dummy,
		next,
		i;
	
	if (m === n || head === null || head.next === null){
		return head;
	}
	
	dummy.next = head; 
	
	i = m - 1;
	
	while (i > 0){
		cur = cur.next;
		i --;
	}
	
	prev = cur; 
	cur = cur.next 
	i = n - m;
	
	while (cur !== null && i > 0){
		next = cur.next;
		if(next){
			cur.next = next.next;
			next.next = prev.next;
			prev.next = next;
		}
		else{
			cur.next = prev.next;
			prev.next = cur;
		}
		i --;
	}
	return dummy.next;
    
};