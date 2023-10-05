print ("Containers:Dictonaries")
d=dict()
d={'cat':'cute','dog':'furry'}
print("Dictonary:",d)
print("Is the dictonary has the key 'cat'?",'cat' in d)
d['fish'] ='wet'
print("After adding new entry to 'd':",d)
print ("Get an element monkey:",d.get('monkey','N/A'))
print("Get an element fish:",d.get('fish','N/A'))
del d['fish']
print("After deleting the newly added entry from 'd'",d)
print("Demo of dictionary comprehension:")
squares={x:x*x for x in range (10)}
print("square of integers of range 10:")
for k,v in squares.items():
    print(k,":",v)


//

Containers:Dictonaries
Dictonary: {'cat': 'cute', 'dog': 'furry'}
Is the dictonary has the key 'cat'? True
After adding new entry to 'd': {'cat': 'cute', 'dog': 'furry', 'fish': 'wet'}
Get an element monkey: N/A
Get an element fish: wet
After deleting the newly added entry from 'd' {'cat': 'cute', 'dog': 'furry'}
Demo of dictionary comprehension:
square of integers of range 10:
0 : 0
1 : 1
2 : 4
3 : 9
4 : 16
5 : 25
6 : 36
7 : 49
8 : 64
9 : 81

Process finished with exit code 0
