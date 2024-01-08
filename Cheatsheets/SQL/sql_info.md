### **MySQL Cheat Sheet for SQL Queries:**

#### **1. SELECT Statements:**
   - **Selecting Specific Columns:**
     ```sql
     SELECT column1, column2, ...
     FROM table_name;
     ```
   - **Selecting All Columns:**
     ```sql
     SELECT *
     FROM table_name;
     ```
   - **Selecting Distinct Values:**
     ```sql
     SELECT DISTINCT column1, column2, ...
     FROM table_name;
     ```
   - **Conditional Selection with WHERE:**
     ```sql
     SELECT column1, column2, ...
     FROM table_name
     WHERE condition;
     ```
   - **Combining Conditions with AND, OR, NOT:**
     ```sql
     SELECT column1, column2, ...
     FROM table_name
     WHERE condition1 AND condition2 OR condition3 ...;
     ```

#### **2. Data Modification:**
   - **Inserting Data with Specified Columns:**
     ```sql
     INSERT INTO table_name (column1, column2, ...)
     VALUES (value1, value2, ...);
     ```
   - **Inserting Data for All Columns:**
     ```sql
     INSERT INTO table_name
     VALUES (value1, value2, ...);
     ```
   - **Updating Existing Records:**
     ```sql
     UPDATE table_name
     SET column1 = value1, column2 = value2, ...
     WHERE condition;
     ```
   - **Deleting Records:**
     ```sql
     DELETE FROM table_name
     WHERE condition;
     ```

#### **3. Query Optimization:**
   - **Limiting Results:**
     ```sql
     SELECT column_name(s)
     FROM table_name
     WHERE condition
     LIMIT index, count;
     ```
   - **Aggregating Functions (e.g., AVG, COUNT, MAX, MIN, SUM):**
     ```sql
     SELECT AVG(column_name) AS average_value
     FROM table_name
     WHERE condition;
     ```

#### **4. String Functions:**
   - **Concatenating Strings:**
     ```sql
     SELECT CONCAT(column1, ' ', column2) AS full_name
     FROM table_name;
     ```
   - **Extracting Substrings:**
     ```sql
     SELECT SUBSTRING(column_name, start_position, length) AS substring
     FROM table_name;
     ```
   - **Changing Case:**
     ```sql
     SELECT UPPER(column_name) AS uppercase
     FROM table_name;
     ```

#### **5. Numeric Functions:**
   - **Calculating Absolute Value:**
     ```sql
     SELECT ABS(column_name) AS absolute_value
     FROM table_name;
     ```
   - **Rounding Numbers:**
     ```sql
     SELECT ROUND(column_name, decimal_places) AS rounded_value
     FROM table_name;
     ```
   - **Finding Minimum and Maximum:**
     ```sql
     SELECT MIN(column_name) AS min_value, MAX(column_name) AS max_value
     FROM table_name;
     ```

#### **6. Pattern Matching:**
   - **Using LIKE Operator:**
     ```sql
     SELECT column_name(s)
     FROM table_name
     WHERE column_name LIKE pattern;
     ```
   - **Using REGEX Operator (RLIKE):**
     ```sql
     SELECT column_name(s)
     FROM table_name
     WHERE column_name REGEXP 'pattern';
     ```

#### **7. Conditional Logic:**
   - **CASE Statement:**
     ```sql
     SELECT
       CASE
         WHEN condition1 THEN result1
         WHEN condition2 THEN result2
         ELSE result
       END AS custom_column
     FROM table_name;
     ```

#### **8. Miscellaneous:**
   - **Counting Rows:**
     ```sql
     SELECT COUNT(*) AS row_count
     FROM table_name;
     ```
   - **Finding Positions:**
     ```sql
     SELECT INSTR(column_name, 'substring') AS position
     FROM table_name;
     ```

