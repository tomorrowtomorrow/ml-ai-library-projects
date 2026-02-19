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
            print(curent_head.next.data)    



test = LINKED_LIST()
test.add(12)
test.add(13)
test.add(14)



