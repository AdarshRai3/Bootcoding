-- Group by : to group the data based of particular column;

-- How to find the number of employees in each department?

Select count(fname),dept from employees group by dept;

-- How to find the average salary given to any department?
Select avg(salary),dept from employees group by dept;

--Combine column 
Select count(fname),avg(salary),dept from employees group by dept;

