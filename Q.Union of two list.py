# Q.find the union of two list:

l1=[]
n1=int(input("Enter the size of list 1:"))
for i in range(n1):
    num1=int(input("Enter any number: "))
    l1.append(num1)


l2=[]
n2=int(input("Enter the size of list 2:"))
for i in range(n2):
    num2=int(input("Enter any number: "))
    l2.append(num2)


union = list(set().union(l1,l2))
print("The union of two list is: ",union)
