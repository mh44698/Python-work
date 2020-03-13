

-- The following SQL statement selects all customers with a City starting with "ber":
SELECT * FROM Customers
WHERE City LIKE 'ber%';

-- The following SQL statement selects all customers with a City containing the pattern "es":
SELECT * FROM Customers
WHERE City LIKE '%es%';

-- The following SQL statement selects all customers with a City starting with any character, followed by "ondon":
SELECT * FROM Customers
WHERE City LIKE '_ondon';

-- The following SQL statement selects all customers with a City starting with "L", followed by any character, followed by "n", followed by any character, followed by "on":
SELECT * FROM Customers
WHERE City LIKE 'L_n_on';

-- The following SQL statement selects all customers with a City starting with "b", "s", or "p":
SELECT * FROM Customers
WHERE City LIKE '[bsp]%';

-- The following SQL statement selects all customers with a City starting with "a", "b", or "c":
SELECT * FROM Customers
WHERE City LIKE '[a-c]%';

-- The two following SQL statements select all customers with a City NOT starting with "b", "s", or "p":
SELECT * FROM Customers
WHERE City LIKE '[!bsp]%';
-- or
SELECT * FROM Customers
WHERE City NOT LIKE '[bsp]%';


