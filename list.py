print("Containers:Lists")
nums=list(range(5))
print("list 'nums' contains:",nums)
nums[4]="abc"
print("list can contain elements of different types. Example:",nums)
nums.append("xyz")
print("'num' after inserting new element at the end :")
print("sublists:")
print("A slice from index 2 to 4:",nums[2:4])
print("A slice from index 2 to the end:",nums[2:])
print("A slice from the start to index 2:",nums[:2])
print("A slice of the whole list:",nums[:])
nums[4:]=[8,9] # Assign a new sublist to a slice
print("After Assigning  new sublist to 'nums':")
for idx,i in enumerate(nums):
    print('%d:%s'%(idx+1,i))
even_squares=[x**2 for x in nums if x%2 == 0]
print("List of squares of even numbers from 'num':",even_squares)

//
Containers:Lists
list 'nums' contains: [0, 1, 2, 3, 4]
list can contain elements of different types. Example: [0, 1, 2, 3, 'abc']
'num' after inserting new element at the end :
sublists:
A slice from index 2 to 4: [2, 3]
A slice from index 2 to the end: [2, 3, 'abc', 'xyz']
A slice from the start to index 2: [0, 1]
A slice of the whole list: [0, 1, 2, 3, 'abc', 'xyz']
After Assigning  new sublist to 'nums':
1:0
2:1
3:2
4:3
5:8
6:9
List of squares of even numbers from 'num': [0, 4, 64]
