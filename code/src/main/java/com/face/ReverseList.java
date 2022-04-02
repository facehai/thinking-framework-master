package com.face;

/**
 * @Description 链表反转
 * @Date 2022/3/22 10:33 下午
 * @Created by lihai
 */
public class ReverseList {

    /**
    * @Author face
    * @Description 定义链表
    * @Date 10:56 下午 2022/3/22
    **/
    static class ListNode{
        int val;
        ListNode next;
        public ListNode(int val,ListNode next){
            this.val = val;
            this.next = next;
        }
    }

    /**
    * @Author face
    * @Description 迭代反转
    * @Date 10:58 下午 2022/3/22
    **/
    public static ListNode iterate(ListNode head){
        ListNode curr;//当前
        ListNode next;//下一个
        ListNode prev = null;//前一个
        curr = head;
        while (curr!=null){
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    public static void main(String[] args) {
        ListNode node5 = new ListNode(5,null);
        ListNode node4 = new ListNode(4,node5);
        ListNode node3 = new ListNode(3,node4);
        ListNode node2 = new ListNode(2,node3);
        ListNode node1 = new ListNode(1,node2);
        ListNode prev =  iterate(node1);
        System.out.println(prev);
    }
}
