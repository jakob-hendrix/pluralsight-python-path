# General Notes

## Basic Language Stuff

### Collections

#### Str - strings

- Sequences of Unicode code points (not quite characters).
- imumutable

```python

# multi-line quotes
"""I am
a single
string"""

# Universal newline support
c = "I am\na single\n string

# Raw strings - wysiwyg
path = r'C:\Users\'
print(path) # C:\Users\

```

#### Bytes

```python
b'data' # is a byte

# You need to encode('utf8') strings into bytes and decode('utf8') the reverse

```

#### List

```python
a = [1, 9, 8]
b = ["apple", "pear" ]
c = []
c.append("test")

```

#### Dict - maps keys to values

```python
d = { 'alice': '111-222-3333', 'bob': "", }
e = {}

```

## Modularity

### Functions

```python
def square(x):
    return x * x

square(5)   # 25
```

- Implicit `return` returns `None`.
- Level of code
  - Python module - convenient import with API
  - Python script - convenient execution from the command line
  - Python program - perhaps composed of many modules

#### Naming Special Functions

Many language features have trailing and leading "__" - pronouced "dunder" (double underscore). Example: `__name__` is called **"dunder name"**

`__name__` is a way to detect if a module is imported or being executed. If it is run as a script, "__name__" will be set to "__main__"

### Shebangs

#!/usr/bin/env python
#!/usr/bin/env python3


## Objects and Types

- the python object model
- named ref to objects
- value vs identiy equait y
- passing args and retuyrning values
- pythons's type system
- scopes to limite name access
- everything is an object

- `id()` - returns a unique id for an object
- `is` operator - tests for equality of objects (do they reference the same object)

- Assignment only ever bionds objects to names. It never copies by value.
- Value-equality and identiy equality are fundamentally different. Value equality can be contorlled by an object.
- - Function args are transfered using "pass-by-object-reference" - refs to objs are copied, not the objects themselves

```python
# Default param - must come last in the signature
def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

```

- Python will generally not perform implicit type coversions

### Scopes

4 scopes
     - local - inside the current function
     - enclosing - inside enclosng functions
     - global/module - top level of the module
     - built-in - in the special builtins module

- Scopes to not correspod the sourc code blocks (indentation)
- References are destoryed once the scope is closed
- Local variables can "shdow" global variables - unless you use the `global` keyword

## Collections


### str (strings)

Use `str.join()` instead of concatenation for efficiency.

```python
colors = ';'.join(['r','b','g'])  # 'r;b;g'
colorItems = colors.split(';')    # ['r', 'b', 'g']
''.join(colorItems)               # 'rbg'
```

`partition` is a a way to unpack a string into a tuple/

```python
"unforgetable".partition('forget')  # ('un', 'forget', 'able')
departure, _, arrival = "London:Edinburgh".partition(':')
departure   # 'London'
arrival     # 'Edinburgh'
# '_' is often used as a name to hold dummy or unusued values. Many tools support this and will suppress unused variable warnings
```

There are multiple ways to format strings.

```python
# Python 3+
"The age of {0} is {1}".format('Jim', 32)

# PEP 496 - 3.6+ - literal string interpolation or "f-strings"
f"one plus one is {1+1}"

f'Math constants: pi={math.pi:.3f}"   # formats to 1000ths
```

### list

```python
# negative indices are 1-based
a = [1, 2, 3, 4]
a[0]      # 1
a[3]      # 3
a[-1]     # 3 == a[len(a) - 1]

# slicing
a[1:3]    # [2, 3] - the end point is 1 beyond the end of the desired range
a[1:-1]   # [2, 3] - all but the first and last
a[2:]     # [3, 4] - all elements from the 3rd element to the end
a[:2]     # [1, 2] all elements of the list up to, but no including the 3rd
b = a[:]  # this makes a new list object nstead of passing around labels, but the objects inside *are not copies*, they reference the saem objects
a is b    # false
a == b    # true
```

- Shallow copy - a copy of a collection, but not a copy of the elements
- deep copies - look at the copy module in the python standard

#### Searching

```python
# index(search_value) returns the index
mylist = [1, 2, 3]
mylist.index(2)     # 1
mylist.index(99)    # ValueError
```

#### Removing

```python
mylist = [1, 2, 3, 'fox']

del mylist[2]             # [1, 2, 'fox']
mylist.remove('fox')      # [1, 2]
```

#### Inserting

```python
mylist = [1, 2, 3]
mylist.insert(1, 'fox')   # [1, 'fox', 2, 3]
```

### dict

```python
myDict = { "Jakob": "apjwh", "Steve": "apsjm" }
```

Each key-value pair is an item - no duplicate keys.
Keys must be immutable. Values may be mutable.

```python
# Dict constructor can convert some types into dicstions
myList = [ ('a', 1), (2, 'test') ]
myDict = dict(myList)

for key in myDicst.keys():
    print(key)

for value in myDict.values():
    print(value)

# tuple unpacking works nicely since dict.items() returns tuples
for key, value in myDict.items():
    print(f"{key} => {value}")
```

Copying is shallow by default.

### tuple

- immutable sequences of arbitrary objects

```python
t = ("Norway", 4.953, 3)
t       # ('Norway', 4.953, 3)
t[0]    # 'Norway'
len(t)  # 3
for item in t:
    print item
# Nested tuples
a = ((1,2), 'Norway', ('test', 999))
a[0][1]   # 2

```

Returning multiple results as a tuple is ofter combined with the wonderful **tuple unpacking** - a destructuring opertion that unpacks data structures into named references

```python
def minmax(items):
    return min(items), max(items)
lower, upper = minmax([83,33,84,32,85,31,86])
lower # 31
upper # 86

# Makes it quite easy to swap the value of 2 variables
a = 'jelly'
b = 'bean'
a, b = b, a
# First, packs into a tuple on the right,
# Second unpack the tuple on the left, reusing the names a and b

```

The tuple constroctor allows you to make a tuple from an existing collection.

```python
tuple([1,2,3])          # (1, 2, 3)
tuple('abc')            # ('a', 'b', 'c')
5 in (3, 4, 5, 6)       # True
42 not in (1, 2, 3, 4)  # True
```

### range

- print a sequence of integers

```python
# range(stop), range(start,stop), range(start,stop,step)
range(5)            # implicit range(0,5). Prints 0,1,2,3,4 (stop value -1)
list(range(5,10))   # [5, 6, 7, 8, 9]
list(range(0,10,2))   # [0, 2, 4, 6, 8]
```

### set

Unordered collection of unique items. Sets are mutable, but set items must be imutable

```python
p = {6, 28, 496}
type(p) # <class 'set'>
```

Set items are unique. This means sets can be used to remove duplicates.

set.add()
set.remove()
set.discard()

#### Set algebra

Operations

- union - AND/OR
- intersections - AND
- difference - in first, not in second
- symmetric_difference - XOR

Relation between sets

- issubset
- issuperset
- isdisjoint

### protocols

Sort of like interfaces

## Exceptions

Exception spectrum - normal to DEATH. Python uses exceptions very frequently as a part of control flow.

```python
# Handling errors - try-except

try:
    # some code
except KeyError:
    # handle excception of type KeyError
except (TypeError, IOError)
    # Handle multiple exceptions with a tuple
```

Use standard exceptions if possible.

- ValueError - invalid argument
- sequence protocols shoulds raise IndexError for out-of-bound indexing

### OS-specific code

- Windows: `msvcrt`
- Linux/Mac: `tty`, `termios`, `sys`
