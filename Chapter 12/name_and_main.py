'''
## What is `if __name__ == "__main__"` in Python?

This line is used to ensure that **certain code only runs when the file is executed directly**, and **not when it is imported** as a module.

---

### How it works:

- Every Python file has a special built-in variable called `__name__`.
- When a file is **run directly**, Python sets `__name__ = "__main__"`.
- When the file is **imported** into another file, `__name__` is set to the **module name** (i.e., the filename).

---

### Example:

**File: `math_utils.py`**

```
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(2, 3))  # Only runs when file is run directly
```

**Terminal:**

```
$ python math_utils.py
# Output: 5 
```

But if you import it elsewhere:

```
import math_utils

# This won't print anything automatically.
# You need to call math_utils.add() explicitly.
```

---

### Why use it?

- Prevents **unintended code execution** when importing.
- Makes the script both **runnable and reusable** as a module.
- Helps structure your code, similar to a `main()` function in C or Java.

---

### Tip:
Use this block to put test code, CLI parsing, or function calls that should only happen during direct execution.

```
if __name__ == "__main__":
    # Test or run your main logic here
    main()
```
'''

from module import helloWorld
