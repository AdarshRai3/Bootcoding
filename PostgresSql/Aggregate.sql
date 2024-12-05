-- Aggregrate functions are the function that we used to calculate something from the data.

-- count() : to count the number of rows in the table
-- max() : to find the maximum value in the column
-- min(): to find the minimum value in the column
-- avg(): to find the average value in the column
-- sum(): to find the sum of the values in the column  

-- How to find the number of employees?
-- Avg salary given to employees?
-- Employees with max Salary?
-- these are some of the question that we can solve using aggregate function in sql;

Select avg(salary) from employees;
Select max(salary) from employees;
Select min(salary) from employees;
Select count(salary) from employees;
Select sum(salary) from employees;

-- Select aggregatefunction(column_name) from employees;
