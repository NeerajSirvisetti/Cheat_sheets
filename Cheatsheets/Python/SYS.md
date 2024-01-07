### **`sys` Module Cheat Sheet:**

```python
import sys

# Get Command Line Arguments
script_name = sys.argv[0]
argument1 = sys.argv[1] if len(sys.argv) > 1 else None
```
**Explanation:** Retrieves command line arguments. `sys.argv[0]` is the script name, and subsequent elements are arguments.

---

```python
# Exit the Program
sys.exit()
```
**Explanation:** Exits the program. Can be called with an exit code.

---

```python
# Get Python Version
python_version = sys.version
```
**Explanation:** Retrieves the Python interpreter version.

---

```python
# Get Platform
platform = sys.platform
```
**Explanation:** Retrieves the platform on which the script is running (e.g., 'win32', 'linux').

---

```python
# Set Maximum Recursion Limit
sys.setrecursionlimit(1000)
```
**Explanation:** Sets the maximum recursion depth. Useful for handling deep recursive calls.

---

```python
# Get or Set Default Encoding
default_encoding = sys.getdefaultencoding()
sys.setdefaultencoding('utf-8')
```
**Explanation:** Retrieves or sets the default string encoding used by Unicode-based functions.

---

```python
# Redirect Stdout to a File
with open('output.txt', 'w') as f:
    sys.stdout = f
    print("This goes to the file.")
```
**Explanation:** Redirects standard output to a file temporarily.

---

```python
# Reset Stdout
sys.stdout = sys.__stdout__
```
**Explanation:** Resets standard output to its original state.

---

