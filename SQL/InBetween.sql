-- The SQL IN Operator
-- The IN operator allows you to specify multiple values in a WHERE clause.

-- The IN operator is a shorthand for multiple OR conditions.

-- IN Syntax

SELECT * FROM Customers
WHERE Country IN ('Germany', 'France', 'UK');

-- Not in

SELECT * FROM Customers
WHERE Country NOT IN ('Germany', 'France', 'UK');

-- BETWEEN Syntax
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;

SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;







