-- Query the names of all American cities in CITY with populations larger than 120000. The CountryCode for America is USA.
SELECT NAME FROM CITY WHERE COUNTRYCODE='USA' AND POPULATION>120000;

-- Query all columns for a city in CITY with the ID 1661.
SELECT * FROM CITY
WHERE ID = 1661;

-- Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.
SELECT * FROM CITY
    WHERE COUNTRYCODE = 'JPN';

SELECT CITY, STATE FROM STATION;

-- Query a list of CITY names from STATION with even ID numbers only. You may print the results in any order, but must exclude duplicates from your answer.
SELECT DISTINCT CITY FROM STATION
    WHERE ID % 2 = 0

--find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
--ORACLE
select count (city) - count(distinct city) from station;

--Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
SELECT * FROM( ( SELECT * FROM ( select CITY, LENGTH(CITY) K FROM STATION WHERE LENGTH(CITY) = ( SELECT MIN(LENGTH(CITY)) FROM STATION ) ORDER BY CITY ASC ) WHERE ROWNUM=1 ) UNION (SELECT * FROM ( select CITY, LENGTH(CITY) K FROM STATION WHERE LENGTH(CITY) = ( SELECT MAX(LENGTH(CITY)) FROM STATION ) ORDER BY CITY ASC ) WHERE ROWNUM=1 ) );


-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
SELECT DISTINCT city FROM station WHERE city REGEXP "^[aeiou].*";


--Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
SELECT DISTINCT CITY 
FROM STATION 
WHERE LOWER(SUBSTR(CITY,LENGTH(CITY),1)) IN ('a','e','i','o','u');










