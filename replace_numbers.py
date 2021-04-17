print("python program to replace first number with last number")
length=int(input("Enter the length of your list :- "))
#declare a list
list1=[]
for i in range(0,length):
    value=int(input("Enter list element "))
    list1.append(value)

print("Your given input list is :- ",list1)

#Now we have to exchange 1st and last element
#so for this I'll fetch these element using for loop and then swap eachother
#for i in list1:
#   temp=list1[0]
#   list1[0]=list1[length-1]
#   list1[length-1]=temp
   
#print(list1)
#we can do this without for loop also
def swapping(list1):
    temp=list1[0]
    list1[0]=list1[length-1]
    list1[length-1]=temp
    return list1
print(swapping(list1))
