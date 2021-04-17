#program to find second max element
n=int(input("Enter length of list :- "))
list1=[]
for i in range(0,n):
    value=int(input("Enter elements of your list :- "))
    list1.append(value)
print("Your list is :- ",list1)
#lets make first two numbers as max one and max two
max1=max(list1[0],list1[1])
max2=min(list1[0],list1[1])
for i in range(2,n):
    if list1[i]>max1:
        max2=max1
        max1=list1[i]
       
    elif list1[i]>max2:
        max1!=list1[i]
        max2=list1[i]
       
print("Second max element is :- ",max2)
