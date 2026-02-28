class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LINKED_LIST:
   
    def __init__(self):
        self.head=None
        self.len=0
   
   
   
    def add(self,data):
        tmp_node=node(data)
        if self.head is None:
            self.head=tmp_node
            
        else:
            curent_head=self.head
            while(curent_head.next!=None):
                curent_head=curent_head.next
            curent_head.next=tmp_node
        self.len+=1    
               
    
    def IS_EMPTY(self):
        if self.head==None or self.len==0:
            print("List is empty!!!")
            return True
        else:
            return False
    
    
    
    
    def PRINT(self):
        if(self.IS_EMPTY()):
            self.IS_EMPTY()
            return 0
            
        curent_head=self.head
        while(curent_head is not None):
            print(f"[{curent_head.data}][.]->",end='')
            curent_head=curent_head.next
        print("None")   



   
    def search(self,info):
        
        if self.IS_EMPTY():
            self.IS_EMPTY()
            return 0
       
       
        tmp_node=self.head
        index=0
        while(tmp_node is not None):
            index+=1
            if tmp_node.data == info:
                print(f"the node was detected it is the {index}th node and info was {info}")
                return tmp_node
            tmp_node=tmp_node.next
        print(f"couldnt find the speceifce node info:{info}")   

    
    
    
    def add_f(self,info):

        n_first=node(info)
        tmp_node=self.head
        self.head=n_first
        n_first.next=tmp_node
        self.len+=1
    
    
    
    def del_first(self):
        if self.IS_EMPTY():
            self.IS_EMPTY()
        tmp_node=self.head.next
        self.head=None
        self.head=tmp_node
        self.len-=1
    
    
    
    def add_at(self,index,info):
        if self.IS_EMPTY():
            self.IS_EMPTY()
            return 0
        
        if index==1:
            self.add_f(info=info)#const time 0(1)
            return 1

        if index>self.len:
            if index==((self.len)+1):
                self.add(info)
                return 1
            print("index out of range!!")  
            return 0      

        target_node=node(info)
        tmp_node=self.head
        for i in range(index-2):
            tmp_node=tmp_node.next
        tmp2=tmp_node.next
        tmp_node.next=target_node
        target_node.next=tmp2
        self.len+=1

    
    
    def del_last(self):
        if self.IS_EMPTY():
            self.IS_EMPTY()
            return 0 
        Last_node=self.head
        for i in range(self.len-2):
            Last_node=Last_node.next
        Last_node.next=None    
        self.len-=1
    
    
    
    def del_at(self,index):
        if self.IS_EMPTY():
            self.IS_EMPTY()      
        if index==self.len:
            self.del_last()
            return
        if index==1:
            self.del_first()
            return        
    
        if index > self.len or index <=0:
            print("out of range!!!")
            return
        if index==1:
            self.del_first()
            return
        target_node=self.head
        for _ in range(index-2):
            target_node=target_node.next
        tmp_node=target_node.next.next
        target_node.next=tmp_node
        self.len-=1           






        

            



        
