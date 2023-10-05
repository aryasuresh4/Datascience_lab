print("Containers:Sets")
num1={100,110,120}
print("Set 'num1':",num1)
num1.add(90)
print("'num1' after inserting 90:",num1)
num1.update([50,60,70])
print("'num1' after inserting multiple elements:",num1)
num1.remove(60)
print("'num1' after removing 60:",num1)
print("Set comprehension and set operations: ")
n1={x for x in range(10)}
print("n1=",n1)
n2={x for x in range(10) if x%2!=0}
print("n2=",n2)
print("n1 union n2:",n1|n2)
print("n1 intersection n2:",n1&n2)
print("n1 difference n2: ",n1-n2)

//

Containers:Sets
Set 'num1': {120, 100, 110}
'num1' after inserting 90: {120, 90, 100, 110}
'num1' after inserting multiple elements: {100, 70, 110, 50, 120, 90, 60}
'num1' after removing 60: {100, 70, 110, 50, 120, 90}
Set comprehension and set operations: 
n1= {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
n2= {1, 3, 5, 7, 9}
n1 union n2: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
n1 intersection n2: {1, 3, 5, 7, 9}
n1 difference n2:  {0, 2, 4, 6, 8}

Process finished with exit code 0
