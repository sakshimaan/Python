#python code to arrange positive and negative nums position

def arrange(arr,n):
    for i in range(1,n):
        if (arr[i]>0):
            continue
    j=i-1
    while(j>=0 and arr[j]>0):
        arr[j+1]=arr[j]
        j=j-1
    arr[j]=arr[i]
       
def print1(arr,n):
    for i in range(1,n):
        print(arr[i],end=" ")
    print()
       
if __name__ == "__main__":
    arr=[-12,11,-13,4,5,-6,8,-4]
    n=len(arr)
    arrange(arr,n)
    print1(arr,n)
