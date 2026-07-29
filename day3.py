N=int(input("enter N:"))
sum=0
even=0
odd=0
for i in range(N+1):
    print(i,end=" ")
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
    sum=sum+i
print("\n""SUM:",sum)
print("EVEN:",even)
print("ODD:",odd)
print(N)