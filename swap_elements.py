print("program to swap two elements")
#lets take a string values list
n=int(input("Enter the length of your list:- "))
list1=[]
for i in range(0,n):
    value=input("Enter string values of your list :- ")
    list1.append(value)
   
print("Your given list is :- ",list1)
pos1=int(input("Enter 1st position which word you want to swap :- "))
pos2=int(input("Enter 2nd position to which you are swapping :- "))

def swapping(list1,pos1,pos2):
    list1[pos1],list1[pos2]=list1[pos2],list1[pos1]
    return list1

print("List After swapping is :- ",swapping(list1,pos1,pos2))

#program to swap two elements
#lets take a string values list
n=int(input("Enter the length of your list:- "))
list1=[]
for i in range(0,n):
    value=input("Enter string values of your list :- ")
    list1.append(value)
   
print("Your given list is :- ",list1)
pos1=int(input("Enter 1st position which word you want to swap :- "))
pos2=int(input("Enter 2nd position to which you are swapping :- "))

def swapping(list1,pos1,pos2):
    list1[pos1],list1[pos2]=list1[pos2],list1[pos1]
    return list1

print("List After swapping is :- ",swapping(list1,pos1,pos2))

