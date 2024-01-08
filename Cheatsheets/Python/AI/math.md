### **Statistics, Probability, and Math Cheat Sheet with Snippets:**

#### **1. Descriptive Statistics:**
   - **Mean (Average):**
     ```python
     import numpy as np
     dataset = [1, 2, 3, 4, 5]
     mean_value = np.mean(dataset)
     ```
   - **Median:**
     ```python
     median_value = np.median(dataset)
     ```
   - **Mode:**
     ```python
     from scipy.stats import mode
     mode_value = mode(dataset).mode[0]
     ```

#### **2. Probability Basics:**
   - **Probability of an Event:**
     ```python
     favorable_outcomes = 3
     total_outcomes = 6
     probability = favorable_outcomes / total_outcomes
     ```
   - **Complement Rule:**
     ```python
     complement_probability = 1 - probability
     ```

#### **3. Probability Distributions:**
   - **Discrete Random Variables:**
     - Example: Rolling a fair six-sided die.
   - **Continuous Random Variables:**
     - Example: Measuring the height of people.
   - **Probability Mass Function (PMF):**
     - Example: Binomial distribution PMF.
   - **Probability Density Function (PDF):**
     - Example: Normal distribution PDF.

#### **4. Common Probability Distributions:**
   - **Uniform Distribution:**
     - Example: Generating random numbers uniformly.
   - **Normal Distribution:**
     - Example: Generating random numbers from a normal distribution.
   - **Binomial Distribution:**
     - Example: Probability of getting exactly 3 heads in 5 coin flips.
   - **Poisson Distribution:**
     - Example: Number of emails received in an hour.

#### **5. Central Limit Theorem:**
   - **Central Limit Theorem (CLT):**
     ```python
     sample_mean = np.mean(sample)
     sample_std = np.std(sample, ddof=1)
     z_score = (sample_mean - population_mean) / (sample_std / np.sqrt(sample_size))
     ```

#### **6. Hypothesis Testing:**
   - **Null Hypothesis (\(H_0\)):**
     ```python
     from scipy.stats import ttest_1samp
     t_stat, p_value = ttest_1samp(sample_data, popmean=expected_mean)
     ```
   - **Alternative Hypothesis (\(H_1\)):**
     ```python
     if p_value < alpha:
         print("Reject Null Hypothesis")
     ```
   - **p-value:**
     - Compare with significance level (\(\alpha\)).
   - **Significance Level (\(\alpha\)):**
     - Commonly set at 0.05.

#### **7. Confidence Intervals:**
   - **Confidence Interval:**
     ```python
     from scipy.stats import t
     margin_of_error = t.ppf(1 - alpha / 2, df) * (sample_std / np.sqrt(sample_size))
     confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
     ```

#### **8. Linear Algebra Basics:**
   - **Matrix Multiplication:**
     ```python
     import numpy as np
     C = np.dot(A, B)
     ```
   - **Transpose of a Matrix:**
     ```python
     A_transpose = A.T
     ```
   - **Eigenvalues and Eigenvectors:**
     ```python
     eigenvalues, eigenvectors = np.linalg.eig(matrix)
     ```

#### **9. Calculus Basics:**
   - **Derivative:**
     ```python
     from sympy import symbols, diff
     x = symbols('x')
     f = x**2
     f_prime = diff(f, x)
     ```
   - **Integral:**
     ```python
     from sympy import integrate
     definite_integral = integrate(f, (x, a, b))
     ```
   - **Chain Rule:**
     ```python
     g_prime = diff(g, x)
     f_prime = diff(f, g) * g_prime
     ```
   - **Partial Derivative:**
     ```python
     from sympy import symbols, diff
     x, y = symbols('x y')
     f = x**2 + y**2
     partial_derivative_x = diff(f, x)
     ```

#### **10. Best Practices and Tips:**
   - **Use of Statistical Software:**
     - R, Python (NumPy, SciPy, Statsmodels), MATLAB, etc.
   - **Understanding Assumptions:**
     - Before applying statistical tests, understand and check assumptions.
   - **Visualization:**
     - Use visualizations for better understanding of data distributions.

