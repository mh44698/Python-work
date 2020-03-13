LIKE

SELECT * FROM Customers
WHERE CustomerName LIKE 'a%';

SELECT * FROM Customers
WHERE CustomerName LIKE '%or%';
-- Like where r is in the second position
SELECT * FROM Customers
WHERE CustomerName LIKE '_r%';
-- The following SQL statement selects all customers with a CustomerName that starts with "a" and are at least 3 characters in length:
SELECT * FROM Customers
WHERE CustomerName LIKE 'a__%';

-- Starts with a ends with o
SELECT * FROM Customers
WHERE ContactName LIKE 'a%o';

-- Does not start with a
SELECT * FROM Customers
WHERE CustomerName NOT LIKE 'a%';
