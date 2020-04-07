n=int(input("Enter the number of elements \n"))
#the number of element in or the number of different wt with their respective value

weight=[]
profit=[]
cost=[]

print("Enter the weight and the profit ")
for i in range(n):
    weight.append(int(input()))
    profit.append(int(input()))
capacity=int(input("Enter the capacity of the knapsack\n"))
#i.e the maximum wt a knapsack that it can hold and we havr to maximize profit at
#that weight

#dessigned a cost matrix accordingly
#the number of rows is equal to n+1 and column is capacity +1

for i in range(n+1):
    cost.append([0]*(capacity+1))
    
        
#here i refers to the number of element i.e number of items to be inserted into the knapsack
#j is refer to the weight of the total element and it should be smaller than the weight at i-1 position because it is the ,maximum capacity the we can take and is shown by the weight array
    

for i in range(n+1):
    for j in range(capacity+1):
        if i==0 or j==0: 
            cost[i][j]=0
        elif j<weight[i-1]: #i.e the present maximum weight is smaller then the current weight than we cannot take the object in the knapsack
            cost[i][j]=cost[i-1][j]
        elif j>=weight[i-1]: #the present weight should be equual to or it should be grater than the maximum size so that we can put into our knapsack
            cost[i][j]=max(profit[i-1]+cost[i-1][j-weight[i-1]],cost[i-1][j])

for i in cost:
    print(i)
    
