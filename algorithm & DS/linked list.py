class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LINKED_LIST:
   
    def __init__(self):
        self.head=None
   
   
   
    def add(self,data):
        tmp_node=node(data)
        if self.head is None:
            self.head=tmp_node
            
        else:
            curent_head=self.head
            while(curent_head.next!=None):
                curent_head=curent_head.next
            curent_head.next=tmp_node
               
    def IS_EMPTY(self):
        if self.head==None:
            print("List is empty!!!")
            return True
        else:
            return False
    
    
    def PRINT(self):
        if(self.IS_EMPTY()):
            return 0
            
        curent_head=self.head
        while(curent_head is not None):
            print(f"[{curent_head.data}][.]->",end='')
            curent_head=curent_head.next
        print("None")   



    def search(self,info):
        
        if self.IS_EMPTY():
            print("empty")
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


        

            



        
