### **Scikit-Learn Cheat Sheet:**

**1. Import Scikit-Learn Modules:**
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, mean_squared_error, confusion_matrix
```
**Explanation:** Import commonly used modules from Scikit-Learn.

---

**2. Loading Datasets:**
```python
from sklearn.datasets import load_iris, load_digits, load_boston
iris = load_iris()
digits = load_digits()
boston = load_boston()
```
**Explanation:** Load sample datasets provided by Scikit-Learn.

---

**3. Train-Test Split:**
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
**Explanation:** Split data into training and testing sets.

---

**4. Standardization:**
```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```
**Explanation:** Standardize features to have zero mean and unit variance.

---

**5. Linear Regression:**
```python
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```
**Explanation:** Train a linear regression model and make predictions.

---

**6. Random Forest Classifier:**
```python
model = RandomForestClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```
**Explanation:** Train a random forest classifier and make predictions.

---

**7. Support Vector Classifier (SVC):**
```python
model = SVC()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```
**Explanation:** Train a support vector classifier (SVC) and make predictions.

---

**8. K-Means Clustering:**
```python
model = KMeans(n_clusters=3)
model.fit(X)
cluster_labels = model.labels_
```
**Explanation:** Apply K-means clustering to data.

---

**9. Model Evaluation - Classification:**
```python
accuracy = accuracy_score(y_true, y_pred)
conf_matrix = confusion_matrix(y_true, y_pred)
```
**Explanation:** Evaluate classification model performance using accuracy and confusion matrix.

---

**10. Model Evaluation - Regression:**
```python
mse = mean_squared_error(y_true, y_pred)
```
**Explanation:** Evaluate regression model performance using mean squared error.

---

**11. Hyperparameter Tuning - Grid Search:**
```python
from sklearn.model_selection import GridSearchCV
param_grid = {'C': [0.1, 1, 10], 'gamma': [0.001, 0.01, 0.1]}
grid_search = GridSearchCV(SVC(), param_grid, cv=3)
grid_search.fit(X, y)
best_params = grid_search.best_params_
```
**Explanation:** Perform hyperparameter tuning using Grid Search.

---

**12. Cross-Validation:**
```python
from sklearn.model_selection import cross_val_score
cv_scores = cross_val_score(model, X, y, cv=5)
average_cv_score = np.mean(cv_scores)
```
**Explanation:** Perform cross-validation to assess model performance.

---

**13. Feature Importance (Random Forest):**
```python
feature_importances = model.feature_importances_
```
**Explanation:** Assess feature importance in a random forest model.

---

**14. Save and Load Models:**
```python
import joblib
joblib.dump(model, 'model.pkl')
loaded_model = joblib.load('model.pkl')
```
**Explanation:** Save and load trained models.

---

**15. Pipelines:**
```python
from sklearn.pipeline import make_pipeline
pipeline = make_pipeline(StandardScaler(), SVC())
pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)
```
**Explanation:** Create and use pipelines for streamlined workflows.

---

