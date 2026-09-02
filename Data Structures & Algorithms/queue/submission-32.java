// Singly Linked List Node
class ListNode {
    int val;
    ListNode prev;
    ListNode next;

    public ListNode(int val) {
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}

// Linked List implementation of Double Ended Queue
class Deque {
    private ListNode front;
    private ListNode rear;
    private int size;

    public Deque() {
        this.front = null;
        this.rear = null;
        this.size = 0;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void append(int value) {
        ListNode newNode = new ListNode(value);
        if (isEmpty()) {
            front = rear = newNode;
        } else {
            newNode.next = front;
            front.prev = newNode;
            front = newNode;
        }
        size++;
    }

    public void appendleft(int value) {
        ListNode newNode = new ListNode(value);
        if (isEmpty()) {
            front = rear = newNode;
        } else {
            newNode.prev = rear;
            rear.next = newNode;
            rear = newNode;
        }
        size++;
    }

    public int pop() {
        if (isEmpty()) {
            return -1;
        }
        int removedValue = front.val;
        front = front.next;
        if (front != null) {
            front.prev = null;
        } else {
            rear = null; // If deque is now empty
        }
        size--;
        return removedValue;
    }

    public int popleft() {
        if (isEmpty()) {
            return -1;
        }

        int removedValue = rear.val;
        rear = rear.prev;
        if (rear != null) {
            rear.next = null;
        } else {
            front = null; // If deque is now empty
        }
        size--;

        return removedValue;
    }
}
