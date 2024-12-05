-- clauses : these are the words that we used to give certain conditions to the sql queries;
-- for example there are different types of clauses.
-- -where
-- -distinct
-- -limit
-- -like
-- -in/ Not in  
-- -between
-- -order by (Asc/Desc)

Select * from Students where rollnos between 101 and 103;
Select * from Students order by rollnos desc;
Select * from Students where dept in ('IT','HR');
Select distinct name from Students;
Select * from Students where name like 'A%';

-- Where is used to select where we want to make changes or read data.
-- Order by is used to sort the data in ascending or descending order using 'Asc' and 'Desc'
-- Distinct is used to remove duplicate values.
-- Limit is used to limit the number of rows to be returned.
-- Like is used to search for a pattern in a column.
-- In is used to select rows where the value of a column is in a list of values.
-- Not in is used to select rows where the value of a column is not in a list of values.

-- Relational operators (=, <, >, <=, >=, !=)
-- Logical operators (AND, OR, NOT)