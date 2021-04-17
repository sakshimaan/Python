#python code to check whether the given string is palindrome or not
def check(string):
    n=len(string)
    first=0
    mid=(n-1)//2
    last=n-1
    flag=1
    while(first<mid):
        if (string[first]==string[last]):
            first=first+1
            last=last-1
        else:
            flag=0
            break;
    if flag==1:
            print("String is palindrome")
    else:
            print("String is not palindrome")
   
   
string=str(input("Enter a string to check whether it is palindrome or not :- "))
#string='abcddcba'
print(check(string))
