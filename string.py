print("Demo of basic data types:string")
s="hello"
t="world"
print("string1:",s)
print("string2:",t)
d=s+" "+t
print("string concatenation:",d)
print("capitalize:",d.capitalize())
print("converted to upper case:",s.upper())
print("right justify a string:",s.rjust(7))
print("string at center:",s.center(7))
print("After replacing l with ell:",s.replace('l','(ell)'))
print("string after striping leading and trailing white spaces:",'world'.strip())


output:
Demo of basic data types:string
string1: hello
string2: world
string concatenation: hello world
capitalize: Hello world
converted to upper case: HELLO
right justify a string:   hello
string at center:  hello 
After replacing l with ell: he(ell)(ell)o
string after striping leading and trailing white spaces: world
