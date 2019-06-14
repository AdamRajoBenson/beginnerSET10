p=int(input())
q=list(map(int,input().split()))
for i in range (0,p-1):
    if(q[i]!=i+1):
        print(i)
        break
