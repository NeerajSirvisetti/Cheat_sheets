### **1. Database Creation:**
   - **Create Database:**
     ```sql
     CREATE DATABASE dbname;
     ```
     This SQL statement creates a new database with the specified name (`dbname`).

   - **Use Database:**
     ```sql
     USE dbname;
     ```
     Switches to the specified database (`dbname`) for subsequent operations.

### **2. Table Operations:**
   - **Create Table:**
     ```sql
     CREATE TABLE tablename (
       column1 datatype,
       column2 datatype,
       ...
     );
     ```
     Creates a table named `tablename` with specified columns and data types.

   - **Primary Key:**
     ```sql
     CREATE TABLE tablename (
       id INT PRIMARY KEY,
       ...
     );
     ```
     Defines a primary key (`id`) for the table.

   - **Auto-increment Primary Key:**
     ```sql
     CREATE TABLE tablename (
       id INT AUTO_INCREMENT PRIMARY KEY,
       ...
     );
     ```
     Creates an auto-increment primary key.

   - **Foreign Key:**
     ```sql
     CREATE TABLE orders (
       order_id INT PRIMARY KEY,
       product_id INT,
       FOREIGN KEY (product_id) REFERENCES products(product_id)
     );
     ```
     Establishes a foreign key relationship between tables.

### **3. Data Manipulation:**
   - **Insert Data:**
     ```sql
     INSERT INTO tablename (column1, column2, ...)
     VALUES (value1, value2, ...);
     ```
     Adds new records to the table.

   - **Update Data:**
     ```sql
     UPDATE tablename
     SET column1 = value1, column2 = value2, ...
     WHERE condition;
     ```
     Modifies existing records based on a specified condition.

   - **Delete Data:**
     ```sql
     DELETE FROM tablename
     WHERE condition;
     ```
     Removes records from the table based on a condition.

### **4. Querying Data:**
   - **SELECT Statement:**
     ```sql
     SELECT column1, column2, ...
     FROM tablename
     WHERE condition;
     ```
     Retrieves data from the table based on specified criteria.

   - **JOIN Tables:**
     ```sql
     SELECT *
     FROM orders
     JOIN customers ON orders.customer_id = customers.customer_id;
     ```
     Combines data from multiple tables using JOIN operations.

   - **Filtering and Sorting:**
     ```sql
     SELECT *
     FROM products
     WHERE category = 'Electronics'
     ORDER BY price DESC;
     ```
     Filters and orders the results of a query.

   - **Aggregate Functions:**
     ```sql
     SELECT AVG(price) AS avg_price, COUNT(*) AS num_products
     FROM products;
     ```
     Performs aggregate calculations on the data.

### **5. Indexing:**
   - **Create Index:**
     ```sql
     CREATE INDEX index_name
     ON tablename (column1, column2, ...);
     ```
     Improves query performance by creating an index on specified columns.

   - **Unique Index:**
     ```sql
     CREATE UNIQUE INDEX unique_index
     ON tablename (column);
     ```
     Creates a unique index to enforce uniqueness on specified columns.

### **6. Views:**
   - **Create View:**
     ```sql
     CREATE VIEW viewname AS
     SELECT column1, column2, ...
     FROM tablename
     WHERE condition;
     ```
     Defines a virtual table based on the result of a SELECT query.

   - **Updateable Views:**
     ```sql
     CREATE VIEW viewname AS
     SELECT column1, column2, ...
     FROM tablename
     WITH CHECK OPTION;
     ```
     Creates a view that allows updates.

### **7. Transactions:**
   - **Start Transaction:**
     ```sql
     START TRANSACTION;
     ```
     Begins a transaction.

   - **Commit Transaction:**
     ```sql
     COMMIT;
     ```
     Saves changes made during the transaction.

   - **Rollback Transaction:**
     ```sql
     ROLLBACK;
     ```
     Undoes changes made during the transaction.

### **8. Security:**
   - **User Management:**
     ```sql
     CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
     GRANT ALL PRIVILEGES ON dbname.* TO 'username'@'localhost';
     ```
     Creates a new user and grants privileges.

   - **Revoke Privileges:**
     ```sql
     REVOKE INSERT ON dbname.tablename FROM 'username'@'localhost';
     ```
     Removes privileges from a user.

### **9. Constraints:**
   - **Check Constraint:**
     ```sql
     CREATE TABLE tablename (
       age INT CHECK (age >= 18)
     );
     ```
     Enforces a condition on a column.

   - **Unique Constraint:**
     ```sql
     CREATE TABLE tablename (
       email VARCHAR(255) UNIQUE
     );
     ```
     Ensures uniqueness of values in a column.

### **10. Backup and Restore:**
   - **Backup Database:**
     ```sql
     mysqldump -u username -p dbname > backup.sql
     ```
     Exports the database to a SQL file.

   - **Restore Database:**
     ```sql
     mysql -u username -p dbname < backup.sql
     ```
     Imports a SQL file to restore the database.

### **11. Stored Procedures:**
   - **Create Procedure:**
     ```sql
     DELIMITER //
     CREATE PROCEDURE sp_name()
     BEGIN
       -- Procedure logic goes here
     END //
     DELIMITER ;
     ```
     Defines a stored procedure.

   - **Call Procedure:**
     ```sql
     CALL sp_name();
     ```
     Invokes a stored procedure.

### **12. Triggers:**
   - **Create Trigger:**
     ```sql
     CREATE TRIGGER trigger_name
     BEFORE INSERT ON tablename
     FOR EACH ROW
     BEGIN
       -- Trigger logic goes here
     END;
     ```
     Defines a trigger that automatically executes when a specified event occurs.

