USE emp;
CREATE TABLE employees( id INT PRIMARY KEY, name VARCHAR(100), post VARCHAR(100), salary INT (10));
INSERT INTO employees VALUES (1, "sumit", "manager", 70000);
INSERT INTO employees VALUES (2, "rahul", "assistant manager", 40000);
INSERT INTO employees VALUES (3, "neha", "receptionist", 30000);
INSERT INTO employees VALUES (4, "manish", "electrician", 20000);
INSERT INTO employees VALUES (5, "sunny", "accountant", 50000);
SELECT*FROM employees;
