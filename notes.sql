-- SQL (Structured Query Language) is a standard language for managing and manipulating relational databases. It is widely used in database management systems such as MySQL, PostgreSQL, Oracle, SQL Server, and SQLite.

-- Table Creation:
-- Tables are used to store data in a structured format. Each table consists of rows and columns.
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50)
);

-- INSERT Statement:
-- The INSERT statement is used to add new records (rows) to a table.
INSERT INTO Employees (EmployeeID, FirstName, LastName, Department)
VALUES (1, 'John', 'Doe', 'IT'),
       (2, 'Jane', 'Smith', 'HR'),
       (3, 'Alice', 'Johnson', 'Finance');

-- SELECT Statement:
-- The SELECT statement is used to retrieve data from one or more tables.
SELECT * FROM Employees;

-- UPDATE Statement:
-- The UPDATE statement is used to modify existing records in a table.
UPDATE Employees
SET Department = 'Marketing'
WHERE EmployeeID = 3;

-- DELETE Statement:
-- The DELETE statement is used to remove records from a table.
DELETE FROM Employees
WHERE EmployeeID = 2;
-- Joins:
-- Joins are used to combine rows from two or more tables based on related columns.
SELECT Employees.FirstName, Employees.LastName, Departments.DepartmentName
FROM Employees
INNER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;

-- Group By and Aggregation:
-- The GROUP BY clause is used to group rows that have the same values into summary rows.
-- Aggregation functions like COUNT(), SUM(), AVG(), MAX(), and MIN() can be used to perform calculations on grouped data.
SELECT Department, COUNT(*) AS NumberOfEmployees
FROM Employees
GROUP BY Department;

-- Subqueries:
-- Subqueries are nested queries that provide a way to perform operations on the results of another query.
SELECT FirstName, LastName, Department
FROM Employees
WHERE Department IN (SELECT DepartmentName FROM Departments WHERE Location = 'New York');

-- Indexes:
-- Indexes are used to improve the speed of data retrieval operations on database tables.
CREATE INDEX idx_LastName ON Employees(LastName);
