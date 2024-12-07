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
-----------------------------------------------------------------

-- Relationship in Sql  

-- In sql we have 3 types of relationship
-- 1.1 One to One
-- 1.2 One to Many
-- 1.3 Many to Many


-- One to One relationship is used when one table contains one record of another table
-- EX: One customer can have one address.
-- One to Many relationship is used when one table contains multiple records of another table  
-- EX: One customer can have own multiple cars.
-- Many to Many relationship is used when one table contains multiple records of another table and another table contains multiple records of another table
-- EX: Many customers can own many models of cars.
-- One book can have two authors and many books can have one author.

-----------------------------------------------------------------
-- Primary key : It is a unique identifier for a row in a table, it is used to identify a row in a table.
-- Unique key: It ensure that the column must have unique values used for mobile no and email columns where we want that two customers cannot have same email or phone number
-- Foreign key : It is primary key of one table which is used a key in other table to establis a relationship between two tables.
-------------------------------------------------------------------
Create table customers(
    id serial primary key,
    name varchar(50),
    mobile_no varchar(10) unique,
)

Create table orders(
    id serial primary key,
    order_date date,
    order_price deciamal(10,2),
    customer_id int,
    Foreign key(customer_id) references customers(id),
)

Insert into customers values(1,'Mayur','1234567890');
Insert into customers values(2,'Shreyas','1234567891');
Insert into customers values(3,'Adarsh','1234567892'); 

Insert into orders values(1,'2022-01-01',100.00,1);
Insert into orders values(2,'2022-01-02',200.00,2);
Insert into orders values(3,'2022-01-03',300.00,3);
---------------------------------------------------------------