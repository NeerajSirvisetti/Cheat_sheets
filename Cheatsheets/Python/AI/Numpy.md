### **NumPy Cheat Sheet:**

**1. Import NumPy:**
```python
import numpy as np
```
**Explanation:** Import NumPy and alias it as `np` for convenience.

---

**2. Create NumPy Arrays:**
```python
# From a Python List
arr_list = np.array([1, 2, 3])

# Zeros Array
zeros_arr = np.zeros((3, 4))

# Ones Array
ones_arr = np.ones((2, 3))

# Identity Matrix
identity_matrix = np.eye(3)

# Random Array
random_arr = np.random.rand(2, 2)
```
**Explanation:** Various ways to create NumPy arrays: from a Python list, zeros array, ones array, identity matrix, and a random array.

---

**3. Array Attributes:**
```python
# Shape of an Array
shape = arr_list.shape

# Dimensions of an Array
dimensions = arr_list.ndim

# Data Type of an Array
data_type = arr_list.dtype

# Number of Elements in an Array
num_elements = arr_list.size
```
**Explanation:** Accessing array attributes like shape, dimensions, data type, and the number of elements.

---

**4. Array Indexing and Slicing:**
```python
# Accessing Elements
element = arr_list[0]

# Slicing
slice_arr = arr_list[1:3]
```
**Explanation:** Indexing and slicing NumPy arrays.

---

**5. Array Operations:**
```python
# Element-wise Addition
sum_arr = arr_list + 2

# Element-wise Multiplication
prod_arr = arr_list * 3

# Dot Product
dot_product = np.dot(arr_list, arr_list)
```
**Explanation:** Basic operations on NumPy arrays like addition, multiplication, and dot product.

---

**6. Universal Functions (Ufuncs):**
```python
# Square Root
sqrt_arr = np.sqrt(arr_list)

# Exponential
exp_arr = np.exp(arr_list)

# Sine and Cosine
sin_arr = np.sin(arr_list)
cos_arr = np.cos(arr_list)
```
**Explanation:** Common mathematical functions applied element-wise using Ufuncs.

---

**7. Reshaping and Transposing:**
```python
# Reshape Array
reshaped_arr = arr_list.reshape((1, 3))

# Transpose Array
transposed_arr = arr_list.T
```
**Explanation:** Changing the shape of an array using `reshape` and transposing with `T`.

---

**8. Array Concatenation and Splitting:**
```python
# Concatenate Arrays
concatenated_arr = np.concatenate((arr_list, arr_list))

# Split Array
split_arr = np.split(arr_list, 3)
```
**Explanation:** Combining arrays with `concatenate` and splitting arrays with `split`.

---

**9. Statistical Operations:**
```python
# Mean
mean_value = np.mean(arr_list)

# Median
median_value = np.median(arr_list)

# Standard Deviation
std_dev = np.std(arr_list)
```
**Explanation:** Calculating statistical measures like mean, median, and standard deviation.

---

**10. Boolean Indexing:**
```python
# Boolean Indexing
bool_index = arr_list[arr_list > 2]
```
**Explanation:** Using boolean arrays for indexing.

---

**11. Broadcasting:**
```python
# Broadcasting
broadcasted_arr = arr_list + np.array([10, 20, 30])
```
**Explanation:** Performing operations on arrays of different shapes using broadcasting.

---

**12. Linear Algebra:**
```python
# Matrix Multiplication
mat_mul = np.matmul(arr_list, arr_list.T)

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(mat_mul)
```
**Explanation:** Performing linear algebra operations using NumPy's `linalg` module.

---

**13. File I/O:**
```python
# Save Array to File
np.save('saved_array.npy', arr_list)

# Load Array from File
loaded_arr = np.load('saved_array.npy')
```
**Explanation:** Saving and loading NumPy arrays to/from files.

---

**14. Random Module:**
```python
# Generate Random Numbers
random_numbers = np.random.rand(3, 2)

# Random Integer
random_int = np.random.randint(1, 10, size=(2, 3))
```
**Explanation:** Using the random module for generating random arrays and integers.

---

**15. Universal Constants:**
```python
# Pi
pi_value = np.pi

# Euler's Number
euler_number = np.e
```
**Explanation:** Accessing universal constants like pi and Euler's number.

---

