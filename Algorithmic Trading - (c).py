def Max_Profit(A,s,l,x):
  p = 0
  for i in range(s,l):
    for j in range(i+1,l+1):
      if(A[j]>A[i]):
        profit=(A[j]-A[j]*x/100-A[i]-A[i]*x/100) + Max_Profit(A,j+1,l,x)

        p=max(p,profit)
  return p

A=[567,4873,5899,6000] #Example
s=0
l=len(A)-1
print(Max_Profit(A,s,l,5))