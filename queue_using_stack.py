'''class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
 
    
    def enQueue(self, x):
        self.s1.append(x)
 
    
    def deQueue(self):
 
        
        if len(self.s1) == 0 and len(self.s2) == 0:
            return -1
 
        
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
 
        else:
            return self.s2.pop()
 
    
if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
 
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    ###time complexity->
            push operation O(N)
            pop operation   O(1)
            ###space complexity-> O(N)
 
'''

 
'''class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
 
    def enQueue(self, x):
         
        
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
 
        
        self.s1.append(x)
 
        
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
 
    
    def deQueue(self):
         
            
        if len(self.s1) == 0:
            return -1;
     
        
        x = self.s1[-1]
        self.s1.pop()
        return x
 

if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
 
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    ###time complexity->
            push operation  O(1)
            pop operation  O(N)
            ###space complexity-> O(N)
 

'''
class Queue:
    def __init__(self):
        self.s = []  
    def enQueue(self, data):
        self.s.append(data) 
    def deQueue(self): 
        if len(self.s) <= 0:
            return -1 
        x = self.s[len(self.s) - 1]
        self.s.pop()
          
        if len(self.s) <= 0:
            return x 
        item = self.deQueue()
          
        self.s.append(x)
         
        return item
     

if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
     
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())

    ###time complexity->
            push operation O(1)
            pop operation   O(N)
            ###space complexity-> O(N)
 
