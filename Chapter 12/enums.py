'''
## Python `enumerate()` Function

The `enumerate()` function adds a **counter** to an iterable and returns it as an `enumerate` object, which can be directly used in loops.

---

### Syntax

```
enumerate(iterable, start=0)
```

- `iterable`: any iterable (list, string, tuple, etc.)
- `start`: the starting index (default is 0)

---

### Basic Example

```
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

**Output:**
```
0 apple
1 banana
2 cherry
```

---

### Without vs With `enumerate()`

```
# Without enumerate
i = 0
for fruit in fruits:
    print(i, fruit)
    i += 1
```

```
# With enumerate
for i, fruit in enumerate(fruits):
    print(i, fruit)
```
--- 

### Custom Starting Index

```
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

**Output:**
```
1. apple
2. banana
3. cherry
```
'''

l = [1,3,2,4,5,7,6,9,8,0]

for i, item in enumerate(l, start = 1):
    print(f"{i}. {item}")