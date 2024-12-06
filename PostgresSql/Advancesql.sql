-- Group by : to group the data based of particular column;

-- How to find the number of employees in each department?

Select count(fname),dept from employees group by dept;

-- How to find the average salary given to any department?
Select avg(salary),dept from employees group by dept;

--Combine column 
Select count(fname),avg(salary),dept from employees group by dept;

---------------------------------------------
Alter command (it is used to change the structure of the table)

Alter table employees remane to emp;

Alter table emp  rename column emp_id to id;

Alter table emp add column city varchar(50) default 'Noida';

Alter table emp Drop column city;

Alter table emp Alter column city set Data type varchar(50);

Alter table emp Alter column  city set default 'Noida';
-------------------------------------------------------------

-- Check contraints ( use for validation of data by adding constraints)

Alter table emp add constraint mob_no_not_valid check(length(mob)>10);

-----------------------------------------------------------------

---Else is used to get a column value based on conditions; 
Select salary , else 
when salary>=10000 then 'High' 
else 'Low'
end as salary_stats from employees
group by salary;

------------------------------------------------------------------
