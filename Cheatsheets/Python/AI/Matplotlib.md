### **Matplotlib Cheat Sheet:**

**1. Import Matplotlib:**
```python
import matplotlib.pyplot as plt
```
**Explanation:** Import Matplotlib and alias it as `plt` for convenience.

---

**2. Basic Line Plot:**
```python
# Basic Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, label='Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Basic Line Plot')
plt.legend()
plt.show()
```
**Explanation:** Creating a basic line plot with labels and a legend.

---

**3. Scatter Plot:**
```python
# Scatter Plot
plt.scatter(x, y, label='Scatter Plot', color='red', marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.legend()
plt.show()
```
**Explanation:** Creating a scatter plot with customization options.

---

**4. Bar Chart:**
```python
# Bar Chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 1, 8, 5]
plt.bar(categories, values, color='green', alpha=0.7)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()
```
**Explanation:** Creating a bar chart with categorical data.

---

**5. Histogram:**
```python
# Histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]
plt.hist(data, bins=5, color='orange', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
```
**Explanation:** Creating a histogram to visualize the distribution of data.

---

**6. Pie Chart:**
```python
# Pie Chart
sizes = [20, 30, 25, 15, 10]
labels = ['A', 'B', 'C', 'D', 'E']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'lightpink'])
plt.title('Pie Chart')
plt.show()
```
**Explanation:** Creating a pie chart to represent proportions.

---

**7. Subplots:**
```python
# Subplots
fig, axs = plt.subplots(2, 2, figsize=(8, 8))
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Subplot 1')
axs[0, 1].scatter(x, y, color='red')
axs[0, 1].set_title('Subplot 2')
axs[1, 0].bar(categories, values, color='green', alpha=0.7)
axs[1, 0].set_title('Subplot 3')
axs[1, 1].hist(data, bins=5, color='orange', edgecolor='black')
axs[1, 1].set_title('Subplot 4')
plt.show()
```
**Explanation:** Creating subplots within a single figure.

---

**8. Customizing Plots:**
```python
# Customizing Plots
plt.plot(x, y, label='Line Plot', linestyle='--', linewidth=2, marker='o', markersize=8, color='purple')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Line Plot')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
```
**Explanation:** Customizing line plot appearance with different styles, markers, and colors.

---

**9. Adding Annotations:**
```python
# Adding Annotations
plt.scatter(x, y, label='Data Points')
plt.text(2, 4, 'Annotation Example', fontsize=10, color='blue', ha='center', va='bottom')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Annotation')
plt.legend()
plt.show()
```
**Explanation:** Adding text annotations to a plot.

---

**10. Saving Plots:**
```python
# Saving Plots
plt.plot(x, y, label='Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Save Plot Example')
plt.legend()
plt.savefig('line_plot.png', dpi=300)
```
**Explanation:** Saving a plot as an image file.

---

