### **`os` Module Cheat Sheet:**

### **1. Current Working Directory:**
```python
# Current Working Directory
current_directory = os.getcwd()
```
**Explanation:** Gets the current working directory.

---

### **2. List Files and Directories:**
```python
# List Files and Directories in a Directory
files_and_dirs = os.listdir(current_directory)
```
**Explanation:** Lists all files and directories in the current working directory.

---

### **3. Join Paths:**
```python
# Join Paths
full_path = os.path.join(current_directory, "filename.txt")
```
**Explanation:** Joins paths, handling platform-specific separators.

---

### **4. Check if Path Exists:**
```python
# Check if Path Exists
if os.path.exists(full_path):
    print("Path exists!")
```
**Explanation:** Checks if the specified path exists.

---

### **5. Check if It's a Directory/File:**
```python
# Check if It's a Directory
if os.path.isdir(full_path):
    print("It's a directory!")

# Check if It's a File
if os.path.isfile(full_path):
    print("It's a file!")
```
**Explanation:** Determines if a path points to a directory or a file.

---

### **6. Create and Remove:**
```python
# Create Directory
os.makedirs("new_directory")

# Remove File
os.remove("filename.txt")

# Remove an Empty Directory
os.rmdir("empty_directory")
```
**Explanation:** Creates a directory, removes a file, and removes an empty directory.

---

### **7. Recursively Remove Directory:**
```python
# Recursively Remove Directory and Contents
os.removedirs("parent/child/grandchild")
```
**Explanation:** Recursively removes a directory and its contents.

---

### **8. Rename File or Directory:**
```python
# Rename File or Directory
os.rename("old_name.txt", "new_name.txt")
```
**Explanation:** Renames a file or directory.

---

### **9. Execute System Command:**
```python
# Execute System Command
os.system("ls")
```
**Explanation:** Executes a system command.

---

### **10. Path Manipulation:**
```python
# Path Manipulation
file_path = "/path/to/my/file.txt"
dir_name = os.path.dirname(file_path)
base_name = os.path.basename(file_path)
file_name, file_extension = os.path.splitext(file_path)
```
**Explanation:** Manipulates paths - gets directory name, base name, and splits file name and extension.

---

