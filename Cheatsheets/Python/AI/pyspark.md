### **PySpark Cheat Sheet:**

**1. Import PySpark Modules:**
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.clustering import KMeans
```
**Explanation:** Import commonly used modules from PySpark.

---

**2. Create a Spark Session:**
```python
spark = SparkSession.builder.appName("mySparkSession").getOrCreate()
```
**Explanation:** Initialize a Spark session.

---

**3. Load Data into PySpark DataFrame:**
```python
df = spark.read.csv("path/to/data.csv", header=True, inferSchema=True)
```
**Explanation:** Load data into a PySpark DataFrame.

---

**4. Display DataFrame:**
```python
df.show()
```
**Explanation:** Display the contents of a DataFrame.

---

**5. Data Exploration:**
```python
df.printSchema()
df.describe().show()
```
**Explanation:** Explore the structure and summary statistics of the DataFrame.

---

**6. Selecting and Filtering Data:**
```python
df.select("column_name").show()
df.filter(col("age") > 25).show()
```
**Explanation:** Select and filter data in a DataFrame.

---

**7. Grouping and Aggregating:**
```python
df.groupBy("category").agg(avg("value"), count("id")).show()
```
**Explanation:** Group and aggregate data in a DataFrame.

---

**8. Feature Engineering:**
```python
assembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")
df_transformed = assembler.transform(df)
```
**Explanation:** Create features for machine learning models using VectorAssembler.

---

**9. Linear Regression:**
```python
lr = LinearRegression(featuresCol="features", labelCol="label")
model = lr.fit(train_data)
predictions = model.transform(test_data)
```
**Explanation:** Train a linear regression model in PySpark.

---

**10. Random Forest Classifier:**
```python
rf = RandomForestClassifier(featuresCol="features", labelCol="label")
model = rf.fit(train_data)
predictions = model.transform(test_data)
```
**Explanation:** Train a random forest classifier in PySpark.

---

**11. Model Evaluation:**
```python
evaluator = BinaryClassificationEvaluator(rawPredictionCol="rawPrediction", labelCol="label")
auc = evaluator.evaluate(predictions)
```
**Explanation:** Evaluate machine learning model performance.

---

**12. K-Means Clustering:**
```python
kmeans = KMeans(featuresCol="features", k=3)
model = kmeans.fit(df_transformed)
clustered_data = model.transform(df_transformed)
```
**Explanation:** Apply K-means clustering in PySpark.

---

**13. Save and Load Models:**
```python
model.save("path/to/model")
loaded_model = KMeansModel.load("path/to/model")
```
**Explanation:** Save and load machine learning models in PySpark.

---

**14. SQL Queries on DataFrame:**
```python
df.createOrReplaceTempView("my_table")
result = spark.sql("SELECT * FROM my_table WHERE age > 25")
```
**Explanation:** Run SQL queries on a PySpark DataFrame.

---

**15. RDD Operations:**
```python
rdd = df.rdd
mapped_rdd = rdd.map(lambda row: (row["name"], row["age"] * 2))
```
**Explanation:** Perform operations using Resilient Distributed Datasets (RDDs).

---

