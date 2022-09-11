class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkList:
    def __init__(self):
        self.head=None
    
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
if __name__=='__main__':
    list1=linkList()

    list1.head=Node(1)
    secound=Node(2)
    third=Node(3)

    list1.head.next=secound
    secound.next=third

    list1.printList()