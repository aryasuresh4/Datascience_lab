print("Conainers:Tuples")
d={(x,x+1):x for x in range(10)}
print("Dictionary with tuple keys:")
for k,v in d.items():
    print(k,":",v)
t=(5,6)
print("Tuple t:",t)
print(d[t])
print(d[1,2])

//
Conainers:Tuples
Dictionary with tuple keys:
(0, 1) : 0
(1, 2) : 1
(2, 3) : 2
(3, 4) : 3
(4, 5) : 4
(5, 6) : 5
(6, 7) : 6
(7, 8) : 7
(8, 9) : 8
(9, 10) : 9
Tuple t: (5, 6)
5
1

Process finished with exit code 0
