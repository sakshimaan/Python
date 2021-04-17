print("Code To Reverse A Linked List")
#lets define a linked list elements head,previous,current and next
#creating a class node and a constructor
class Node:
    #creating constructor to initialise the node object
    def __init__(self,data):
        self.data=data
        self.next=None
     #in class linked list we will define all functions as reverse,push and print  
class linkedlist:
    def __init__(self):
        self.head=None
       
    def reverse(self):
        prev=None
        current=self.head
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
   
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
       
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
       

#define a list and pust elements to that list...also we have to define push(),linkedlist() and print() function
list1 = linkedlist()
arr=[11,32,53,24,55,36,27,28,29]
n=len(arr)
for i in range(n):
    list1.push(arr[i])
print("Original list is :- ")
list1.printlist()
list1.reverse()
print("\nReverse list is :- ")
list1.printlist()
