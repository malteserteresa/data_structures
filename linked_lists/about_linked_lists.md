Linked lists are an ordered array but instead of using an index use a
pointer to the next element.

Pointers in Python?
Python doesn't have pointers for many reasons, probably mainly because
Python champions usability over speed, and memory management can be
challenging especially for beginners. 

In C you have a location in memory and a value. In python you have a
PythonObject (CPython struc) with a value, a pointer to a type and a reference
count. 

```
x = 100
```
When executing the above line in python we create an object, assign a type, 
value and point x to the object and increase its reference counter by 1. x
does not own the allocated memory but references it, the PythonObject owns it.

Simulate Pointers in Python
