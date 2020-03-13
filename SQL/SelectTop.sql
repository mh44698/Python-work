SELECT TOP number|percent column_name(s)
FROM table_name
WHERE condition;

SELECT TOP 3 * FROM Customers;

SELECT TOP 50 PERCENT * FROM Customers;

SELECT * FROM Customers
WHERE Country='Germany'
LIMIT 3;

