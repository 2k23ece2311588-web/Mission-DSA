class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k
        self.queue = [0] * k  
        self.head = 0         
        self.count = 0       

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        
       
        rear_index = (self.head + self.count) % self.capacity
        self.queue[rear_index] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
       
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue. If the queue is empty, return -1.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue. If the queue is empty, return -1.
        """
        if self.isEmpty():
            return -1
        
        
        rear_index = (self.head + self.count - 1) % self.capacity
        return self.queue[rear_index]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.capacity
