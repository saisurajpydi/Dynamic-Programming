"""
Q1: Balancing Parenthesis: Given a string of parenthesis you have to print the minimum number of deletions that can be made so to balance the parenthesis.
"""
n = input()
stack = []
op = 0
cl = 0
dele = 0
for i in range(len(n)):
    if(n[i] == "("):
        op += 1
        stack.append(n[i])
    if(n[i] == ")"):
        cl += 1
    if(n[i] == ")" and len(stack) != 0 ):
        stack.pop(len(stack)-1)
    if(cl > 0 and op == 0):
        dele += 1
    if( i == len(n) - 1 ):
        dele += abs(op-cl)
print("the no of deletions are" , dele)
print(stack)