N=int(input("enter N:"))
total_sum=0
c1=0
c2=0
print("Numbers:")
for i in range(1,N+1):
    print(i,end=" ")
    total_sum+=i
    average=total_sum/2
    if i%2==0:
        c1=c1+1
    else:
        c2+=1
print('\nSUM:',total_sum)
print("Average:",average)
print("even count:",c1)
print("odd count:",c2)
if N%2==0:
    print("largest even:",N)
else:
    print("largest even:",N-1)
for i in range(1,N+1):
    print("smallest odd:",i)
    break
