-- What is a Stored Procedure?
-- A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.

-- So if you have an SQL query that you write over and over again, save it as a stored procedure, and then just call it to execute it.

-- You can also pass parameters to a stored procedure, so that the stored procedure can act based on the parameter value(s) that is passed.

-- Stored Procedure Syntax
CREATE PROCEDURE procedure_name
AS
sql_statement
GO;
EXEC procedure_name;


CREATE PROCEDURE SelectAllCustomers
AS
SELECT * FROM Customers
GO;
EXEC SelectAllCustomers;


